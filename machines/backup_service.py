# This Python script is supposed to act as a template for a backup
# service that can dynamically pull files from another computer for
# long term backup. It also sends the output of the backup procedure
# to a specified list of email addresses.
# 
# It assumes you have SSH access to the computer in question and that
# somewhere on that computer there is a list of directories that should
# be backed up. Under the hood, it uses `rsync` to move the files.

# On the target machine, you should ideally create a new user that only
# has read access to the relevant files. But on Unraid this is not that
# easy, so we mostly just accept the risk of having write access too.
# At the very least, you should create a user that is not root.
# Something like:
# 	groupadd backups -g SOME_GROUP_ID
#   useradd -g backups backups
#   mkdir /mnt/user/backups_user
#   usermod -d /mnt/user/backups_user backups
# Then, add the user to nano /etc/ssh/sshd_config and copy the public
# key to /mnt/user/backups_user/.ssh/authorized_keys for SSH access.
# Don't forget to change the permissions on .ssh (chmod 700 .ssh and
# chmod 600 .ssh/authorized_keys). Also make sure that the new user is
# the owner of the .ssh folder and everything in it.
# Also, on unraid, you might want to comment out `export HOME=/root`
# in `/etc/profile`.

# Finally, you might actually want to use root if you are backing up some
# private data that cannot be accessed by the backups user.

# You can then add this script to cron to run periodically every Sunday
# at 3am:
# 0 3 * * 0 root python3 /mnt/hdd/backups/zavazadlo.py >> /mnt/hdd/backups/zavazadlo.log 2>&1

import fcntl
import os
import smtplib
import subprocess
import sys
from datetime import datetime
from email.mime.text import MIMEText
from pathlib import Path


# The following are configuration variables that you should fill before
# starting the service. Here, we give some reasonable defaults that are
# used in our case.

MACHINE_URL = 'root@zavazadlo'
REMOTE_LIST_FILE = '/mnt/user/appdata/backup-locations.txt'
LOCAL_BACKUP_DIR = '/mnt/hdd/backups/zavazadlo'
SEND_REPORT_TO = 'daemontus@gmail.com'
# Currently, only gmail senders are supported, but you can configure this quite easily.
GMAIL_USER = 'daemontus@gmail.com'
# Don't keep the app password in the script. Provide it either through the
# BACKUP_GMAIL_APP_PASSWORD environment variable, or put it in a file (chmod 600)
# readable only by the user running the backup.
GMAIL_APP_PASSWORD_FILE = '/root/.backup_gmail_app_password'

# Fail instead of hanging forever when the remote machine is off or unreachable.
SSH_OPTIONS = [
	'-o', 'BatchMode=yes',
	'-o', 'ConnectTimeout=30',
	'-o', 'ServerAliveInterval=30',
	'-o', 'ServerAliveCountMax=6',
]
# How many trailing lines of an rsync log to include in the report for failed locations.
LOG_TAIL_LINES = 15


def load_app_password():
	password = os.environ.get('BACKUP_GMAIL_APP_PASSWORD')
	if password:
		return password
	return Path(GMAIL_APP_PASSWORD_FILE).read_text().strip()


def send_report(subject, body):
	"""Send an email report. Never raises: a mail failure must not hide the backup result."""
	try:
		msg = MIMEText(body)
		msg['Subject'] = subject
		msg['From'] = GMAIL_USER
		msg['To'] = SEND_REPORT_TO
		with smtplib.SMTP('smtp.gmail.com', 587, timeout=60) as smtp:
			smtp.starttls()
			smtp.login(GMAIL_USER, load_app_password())
			smtp.send_message(msg)
	except Exception as e:
		print(f"Failed to send report email ({subject!r}): {e}", file=sys.stderr)


def fail(message):
	print(f"ERROR: {message}", file=sys.stderr)
	send_report('!!! Backup error', message)
	sys.exit(1)


def tail(path, lines=LOG_TAIL_LINES):
	try:
		return ''.join(Path(path).read_text(errors='replace').splitlines(keepends=True)[-lines:])
	except OSError:
		return '(log unavailable)\n'


def sync_location(location, backup_dir):
	"""Returns (rsync exit code, log path)."""
	# For files, we don't do anything. For folders, we want the original
	# path to end with /, but not the local one.
	local_path = Path(f"{backup_dir}{location.rstrip('/') or '/'}")
	local_path.mkdir(parents=True, exist_ok=True)
	log_path = backup_dir / f"rsync_{location.replace('/', '_')}.log"

	# -a means directory is processed recursively and permissions are preserved.
	# -z means the transfer uses compression.
	# -v is just verbose to print the list of transferred files.
	# -W means "copy whole files", which avoids diffing, which is often costly for large files.
	#    Typically, the file is either completely changed or very small anyway.
	# -s (--protect-args) stops the remote shell from re-splitting paths with spaces/globs.
	# --delete means files removed on remote machine are removed here too.
	# You can add -n to perform a dry run of the backup.
	command = [
		'rsync', '-azvWs', '--delete',
		'-e', 'ssh ' + ' '.join(SSH_OPTIONS),
		f"{MACHINE_URL}:{location}", str(local_path),
	]
	with open(log_path, 'w') as log:
		return subprocess.run(command, stdout=log, stderr=subprocess.STDOUT).returncode, log_path


def main():
	backup_dir = Path(LOCAL_BACKUP_DIR)
	backup_dir.mkdir(parents=True, exist_ok=True)

	# Prevent overlapping runs (e.g. last week's backup still going) from
	# running rsync --delete over the same directories concurrently.
	lock_file = open(backup_dir / '.backup.lock', 'w')
	try:
		fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
	except OSError:
		fail("Another backup run is still in progress.")

	start_time = datetime.now()
	print("Starting backup at", start_time)

	list_path = backup_dir / 'backup-locations.txt'
	# subprocess.run with an argument list: no shell, so no quoting problems.
	status = subprocess.run(
		['scp', '-q', *SSH_OPTIONS, f"{MACHINE_URL}:{REMOTE_LIST_FILE}", str(list_path)]
	).returncode
	if status != 0:
		fail(f"Failed to retrieve backup locations (scp exit code {status}).")

	results = []
	failures = 0
	for location in list_path.read_text().splitlines():
		location = location.strip()
		if not location:
			continue
		if location.startswith('#'):
			results.append(f"[Skipped] {location}")
			print(f"Skipping location `{location[1:].strip()}`.")
			continue
		if not location.startswith('/') or '..' in location.split('/'):
			# A bad line should not prevent the other locations from being backed up.
			results.append(f"[INVALID] {location}")
			failures += 1
			continue

		print(f"Synchronizing location {location}")
		try:
			# Note: os.system() returned a wait status (exit code << 8), so the
			# old `status == 23` check could never match. subprocess gives the real code.
			status, log_path = sync_location(location, backup_dir)
		except Exception as e:
			results.append(f"[ERR] {location}: {e}")
			failures += 1
			continue

		if status == 0:
			results.append(f"[OK] {location}")
		elif status in (23, 24):
			# 23 = partial transfer (some files unreadable), 24 = files vanished during transfer.
			results.append(f"[PARTIAL] ({status}) {location}\n{tail(log_path)}")
			failures += 1
		else:
			results.append(f"[ERR] ({status}) {location}\n{tail(log_path)}")
			failures += 1

	duration = datetime.now() - start_time
	print("Backup completed at:", datetime.now())
	print("Total duration:", duration)

	report = '\n'.join(results)
	if failures:
		send_report('!!! Backup finished with errors',
			f"Backup job finished in {duration} with {failures} problem(s).\n\n{report}")
		sys.exit(3)
	send_report('Backup success', f"Backup job completed successfully in {duration}.\n\n{report}")


if __name__ == '__main__':
	try:
		main()
	except SystemExit:
		raise
	except Exception as e:
		# Make sure an unexpected crash is also reported instead of dying silently in the cron log.
		fail(f"Backup crashed: {e!r}")
