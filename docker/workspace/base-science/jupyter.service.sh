#!/bin/sh
exec /sbin/setuser $WORKSPACE_USER jupyter lab --config=config.py --notebook-dir=~/ >> /var/log/jupyter.log 2>&1