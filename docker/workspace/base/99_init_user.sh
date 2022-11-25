#!/bin/sh

# Run init script as main user if it exists
if [ -f “/home/$WORKSPACE_USER/.init.sh” ]; then 
	su - $WORKSPACE_USER -c /home/$WORKSPACE_USER/.startup.sh
fi