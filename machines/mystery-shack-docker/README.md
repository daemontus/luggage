# Mystery shack docker host

These files are expected to be placed in the `/root` directory.

For the rest of the setup process follow these instructions:


 - Setup docker VM:
 	- name docker, id 101;
 	- enable guest agent
 	- 6 CPUs, 98304MB of RAM
 	- 128GB disk, stored in vm-data, ssd emulation
 	- debian 12.1 as install ISO.
 - Install debian in docker VM:
 	- Install (instead of graphical install)
 	- hostname:mystery-shack-docker, domain:empty
 	- username/password as everywhere else
 	- full disk as one partition
 	- deselect desktop env./GNOME; select SSH server
 - Setup debian in docker VM:
 	- ssh as user, then go to root shell using `su`
 	- apt install net-tools wget curl git sudo magic-wormhole screen htop build-essential
 	- Allow sudo for user: /usr/sbin/usermod -aG sudo daemontus
 	- Install tailscale and disable key expiry
 	- Make sure guest agent is running (systemctl status qemu-guest-agent)
 	- Install docker engine and docker compose
 	- Move download_vs_code.sh and startup.sh to /root (chmod +x)
 	- Download VS code and create a startup.service that runs startup.sh
 		- https://dannyda.com/2023/07/30/how-to-run-execute-start-script-on-system-boot-start-up-in-linux-debian-ubuntu-kali-linux-fedora-redhat-rocky-linux-etc/
 	- systemctl reboot (reset to enable startup script)
 	- systemctl status startup.service to see if VSCode is running
 	- Now we have VS Code running at http://mystery-shack-docker:8000
 	- Generate a new SSH key and add it to github
 		- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
 	- Clone https://github.com/daemontus/luggage to your home folder.
 	- Install NFS driver and setup shares to zavazadlo:
 		- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-debian-11
 		- Add the following to /etc/fstab:
 			```
 			zavazadlo:/mnt/user/ws-daemontus-hdd    /nfs/ws-daemontus-hdd   nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
			zavazadlo:/mnt/user/ws-daemontus-ssd    /nfs/ws-daemontus-ssd   nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
			zavazadlo:/mnt/user/ws-students         /nfs/ws-students        nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
 			```
 		- Run the following to mount NFS only *after* tailscale is started:
 			- https://forum.tailscale.com/t/mount-share-only-if-connected-to-tailscale/3027/8
 			- systemctl add-wants nfs-mountd.service tailscaled.service
 		- To re-mount everything once the VM is running, use `sudo mount -a`.
 	- Copy latest compose.yml to /root and run `docker compose up` to test all services
 	- Then, create /lib/systemd/system/docker-compose.service and use:
 		```
 		[Unit]
		Description=Docker Compose Application Service
		Requires=docker.service
		After=docker.service
		StartLimitIntervalSec=60

		[Service]
		WorkingDirectory=/root      
		ExecStart=/usr/bin/docker compose up
		ExecStop=/usr/bin/docker compose down
		TimeoutStartSec=0
		Restart=on-failure
		StartLimitBurst=3

		[Install]
		WantedBy=multi-user.target
 		```
 	- Afterwards, run `systemctl daemon-reload` and `systemctl enable docker-compose.service`
 	- At this point, everything should basically work. However, rebooting the machine can sometimes take a long time 
 	because some of the file connections do not always close properly and we need to wait a few minutes before
 	the system kills them.
 	- Also, if you need to update a particular service, you can run `docker compose up -d --no-deps <SERVICE>`. This will only restart *that* container only.