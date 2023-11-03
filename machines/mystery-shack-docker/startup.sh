#!/bin/bash

# Global git config
# exec su -c 'git config --global user.name "Samuel Pastva"' daemontus
# exec su -c 'git config --global user.email "sam.pastva@gmail.com"' daemontus


exec su -c 'cd ~ && /usr/local/vscode/bin/openvscode-server \
	--port=8000 \
	--host=0.0.0.0 \
	--without-connection-token \
	>> /home/daemontus/vscode.log 2>&1' daemontus