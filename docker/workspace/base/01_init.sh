#!/bin/sh

# Create the workspace user if she does not exist.
id -u somename >/dev/null 2>&1 || useradd -u $WORKSPACE_USER -g workspace -s /bin/bash -m $WORKSPACE_USER

# If an SSH key is provided, copy it to the user's .ssh folder
# and then erase the key.
if [ "$PRIVATE_KEY" != "" ]; then 
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