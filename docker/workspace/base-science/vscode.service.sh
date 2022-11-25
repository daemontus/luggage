#!/bin/sh
# If VSCODE_DATA is available, start it with persistable storage, otherwise use defaults.
if [ "$VSCODE_DATA" != "" ]; then 
	exec /sbin/setuser $WORKSPACE_USER /usr/local/vscode/bin/openvscode-server \
		--port=8001 \
		--host=0.0.0.0 \
		--without-connection-token \
		--user-data-dir=$VSCODE_DATA/user \
		--extensions-dir=$VSCODE_DATA/extensions \
		--server-data-dir=$VSCODE_DATA/server \
		>> /var/log/vscode.log 2>&1
else
	exec /sbin/setuser $WORKSPACE_USER /usr/local/vscode/bin/openvscode-server \
		--port=8001 \
		--host=0.0.0.0 \
		--without-connection-token \
		>> /var/log/vscode.log 2>&1
fi