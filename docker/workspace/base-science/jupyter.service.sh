#!/bin/sh
exec /sbin/setuser $WORKSPACE_USER jupyter lab --config=config.py >> /var/log/jupyter.log 2>&1