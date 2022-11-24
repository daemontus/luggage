#!/bin/sh
# The $VSCODE_DATA directory is used to store vscode configuration that should be persisted between restarts.
# Note that the internal directories used by vscode must initially exist. This is currently done by
# the init.sh script.
exec /sbin/setuser $WORKSPACE_USER /usr/local/vscode/bin/openvscode-server \
	--port=8001 \
	--host=0.0.0.0 \
	--without-connection-token \
	--user-data-dir=$VSCODE_DATA/user \
	--extensions-dir=$VSCODE_DATA/extensions \
	--server-data-dir=$VSCODE_DATA/server \
	>> /var/log/vscode.log 2>&1