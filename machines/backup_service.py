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

import os
import sys
import smtplib
from datetime import date, datetime
from email.mime.text import MIMEText
from pathlib import Path


# The following are configuration variables that you should fill before
# starting the service. Here, we give some reasonable defaults that are
# used in our case.

MACHINE_URL = 'root@zavazadlo'
REMOTE_LIST_FILE = '/mnt/user/backups_user/backup-locations.txt'
LOCAL_BACKUP_DIR = '/mnt/hdd/backups/zavazadlo'
SEND_REPORT_TO = 'daemontus@gmail.com'
# Currently, only gmail senders are supported, but you can configure this quite easily.
GMAIL_USER = 'daemontus@gmail.com'
GMAIL_APP_PASSWORD = 'SECRET'


def handle_error(message = None):
	if message is None:
		message = "Unknown backup error"
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(GMAIL_USER, GMAIL_APP_PASSWORD)

	# Mailing info
	# Account Information
	today = date.today()  # Get current time/date
	now = datetime.now() # Get current time

	# Creates the text, subject, 'from', and 'to' of the message.
	#msg = MIMEText('actual public IP: %s' %  public_ip)
	msg = MIMEText(message)
	msg['Subject'] = '!!! Backup error'
	msg['From'] = GMAIL_USER
	msg['To'] = SEND_REPORT_TO
	# Send the message
	smtpserver.sendmail(GMAIL_USER, [SEND_REPORT_TO], msg.as_string())
	# Closes the smtp server.
	smtpserver.quit()

def handle_success(locations, duration):	
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	smtpserver.login(GMAIL_USER, GMAIL_APP_PASSWORD)

	# Mailing info
	# Account Information
	today = date.today()  # Get current time/date
	now = datetime.now() # Get current time

	# Creates the text, subject, 'from', and 'to' of the message.
	#msg = MIMEText('actual public IP: %s' %  public_ip)
	msg = MIMEText(f"Backup job completed successfully in {duration}.\n\n{locations}")
	msg['Subject'] = 'Backup success'
	msg['From'] = GMAIL_USER
	msg['To'] = SEND_REPORT_TO
	# Send the message
	smtpserver.sendmail(GMAIL_USER, [SEND_REPORT_TO], msg.as_string())
	# Closes the smtp server.
	smtpserver.quit()

start_time = datetime.now()
print("Starting backup at", start_time)

status = os.system(f"scp \"{MACHINE_URL}:{REMOTE_LIST_FILE}\" \"{LOCAL_BACKUP_DIR}/backup-locations.txt\"")

if status != 0:
	handle_error("Failed to retrieve backup locations.")
	sys.exit(1)

results = ""
backup_locations = Path(f"{LOCAL_BACKUP_DIR}/backup-locations.txt").read_text()
for location in backup_locations.splitlines():
	location = location.strip()
	if location.startswith('#'):
		results += f"[Skipped] {location}\n"
		print(f"Skipping location `{location[1:]}`.")
		continue
	if not location.startswith('/'):
		handle_error(f"Invalid `{location}`.")
		sys.exit(2)
	print(f"Synchronizing location {location}")
	# -a means directory is processed recursively and permissions are preserved.
	# -z means the transfer uses compression.
	# -v is just verbose to print the list of transferred files.
	# -W means "copy whole files", which avoids diffing, which is often costly for large files.
	#    Typically, the file is either completely changed or very small anyway.
	# --delete means files removed on remove machine are removed here too.	
	# You can add -n to perform a dry run of the backup.	
	local_path = f"{LOCAL_BACKUP_DIR}{location}"
	# For files, we don't do anything. For folders, we want the original 
	# path to ends with /, but not the local one.
	if local_path.endswith('/'):
		local_path = local_path[:-1]
	location_id = location.replace('/', '_')

	status = os.system(f"mkdir -p {local_path}")
	if status != 0:
		handle_error(f"Cannot create target dir for {location}")
		sys.exit(2)
	
	status = os.system(f"rsync -azvW --delete \"{MACHINE_URL}:{location}\" \"{local_path}\" &> \"{LOCAL_BACKUP_DIR}/rsync_{location_id}.log\"")
	if status == 0:
		results += f"{status} [OK] {location}\n"	
	elif status == 23:
		results += f"{status} [PARTIAL] {location}\n"
	else:
		results += f"{status} [ERR] {location}\n"

end_time = datetime.now()
duration = end_time - start_time
print("Backup completed at:", end_time)
print("Total duration:", duration)

handle_success(results, duration)