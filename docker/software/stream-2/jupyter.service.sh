#!/bin/sh
# Jupyter will not use the defulat shell of our user, but one specified in $SHELL.
export SHELL=/bin/bash
export PATH="/opt/venv/bin:$PATH"
exec python3.7 -m jupyter notebook --config=config.py >> /var/log/jupyter.log 2>&1