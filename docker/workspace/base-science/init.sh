#!/bin/sh

# Create the workspace user if she does not exist.
id -u somename >/dev/null 2>&1 || useradd -u $WORKSPACE_USER -g workspace -s /bin/bash -m $WORKSPACE_USER

# Copy the provided ssh key to its rightful place.
if [ -z $PRIVATE_KEY ]; then 
	mkdir -p /home/$WORKSPACE_USER/.ssh
	echo "$PUBLIC_KEY" > /home/$WORKSPACE_USER/.ssh/workspace.pub
	echo "-----BEGIN OPENSSH PRIVATE KEY-----" > /home/$WORKSPACE_USER/.ssh/workspace
	echo "$PRIVATE_KEY" >> /home/$WORKSPACE_USER/.ssh/workspace
	echo "-----END OPENSSH PRIVATE KEY-----" >> /home/$WORKSPACE_USER/.ssh/workspace
	export PRIVATE_KEY=""
	export PUBLIC_KEY=""
	chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.ssh/
	chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.ssh/workspace
	chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.ssh/workspace.pub
fi

# Make sure VSCode has a place for configuration data.
mkdir -p $VSCODE_DATA/user
mkdir -p $VSCODE_DATA/extensions
mkdir -p $VSCODE_DATA/server
chown $WORKSPACE_USER:workspace $VSCODE_DATA/user
chown $WORKSPACE_USER:workspace $VSCODE_DATA/extensions
chown $WORKSPACE_USER:workspace $VSCODE_DATA/server

# Run init script as main user if it exists
if [ -f “/home/$WORKSPACE_USER/.init.sh” ]; then 
	su - $WORKSPACE_USER -c /home/$WORKSPACE_USER/.init.sh
fi