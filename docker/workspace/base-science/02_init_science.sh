#!/bin/sh

# Make sure VSCode has a place for configuration data.

if [ "$VSCODE_DATA" != "" ]; then 
	echo "Creating VSCode data folders in $VSCODE_DATA."
	mkdir -p $VSCODE_DATA/user
	mkdir -p $VSCODE_DATA/extensions
	mkdir -p $VSCODE_DATA/server
	chown $WORKSPACE_USER:workspace $VSCODE_DATA/user
	chown $WORKSPACE_USER:workspace $VSCODE_DATA/extensions
	chown $WORKSPACE_USER:workspace $VSCODE_DATA/server
else
	echo "VSCode data path not specified. Configuration will not persist."
fi

# Add root folder to Jupyter lab config.
# In theory, we should be able to just use --notebook-dir option when starting jupyter lab,
# but the latex extension seems to ignore this and requires both notebook dir and root dir.

echo "c.ServerApp.notebook_dir = '/home/$WORKSPACE_USER/'" >> /etc/service/jupyter/config.py
echo "c.ServerApp.root_dir = '/home/$WORKSPACE_USER/'" >> /etc/service/jupyter/config.py