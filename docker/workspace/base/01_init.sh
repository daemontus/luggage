#!/bin/sh

# Create the workspace user if she does not exist.
id -u $WORKSPACE_USER >/dev/null 2>&1 || useradd -u 1000 -g workspace -s /bin/bash -m $WORKSPACE_USER

# If an SSH key is provided, copy it to the user's .ssh folder
# and then erase the key.
if [ "$PRIVATE_KEY" != "" ]; then 
	echo "Found private key. Saving to ~/.ssh/workspace"

	# Copy the public and private key
	mkdir -p /home/$WORKSPACE_USER/.ssh
	echo "$PUBLIC_KEY" > /home/$WORKSPACE_USER/.ssh/workspace.pub
	echo "-----BEGIN OPENSSH PRIVATE KEY-----" > /home/$WORKSPACE_USER/.ssh/workspace
	echo "$PRIVATE_KEY" >> /home/$WORKSPACE_USER/.ssh/workspace
	echo "-----END OPENSSH PRIVATE KEY-----" >> /home/$WORKSPACE_USER/.ssh/workspace

	# Add the key through ssh config
	# This code ensures that subsequent restarts of the container won't repeat the line again.
	LINE="IdentityFile ~/.ssh/workspace"
	FILE="/home/${WORKSPACE_USER}/.ssh/config"
	touch $FILE
	grep -qF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"	

	# Auto-start ssh agent on user login
	LINE="eval \`ssh-agent -s\`"
	FILE="/home/${WORKSPACE_USER}/.bashrc"
	touch $FILE
	grep -qF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"	

	# Erase keys
	export PRIVATE_KEY=""
	export PUBLIC_KEY=""

	# Fix permissions for created files.
	chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.ssh/
	chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.ssh/config
	chmod 600 /home/$WORKSPACE_USER/.ssh/workspace
	chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.ssh/workspace
	chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.ssh/workspace.pub
else
	echo "No private key found."
fi