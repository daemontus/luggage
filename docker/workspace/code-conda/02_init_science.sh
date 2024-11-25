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
	chown $WORKSPACE_USER:workspace $VSCODE_DATA
else
	echo "VSCode data path not specified. Configuration will not persist."
fi
