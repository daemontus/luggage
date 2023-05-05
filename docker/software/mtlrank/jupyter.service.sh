#!/bin/sh
# Jupyter will not use the defulat shell of our user, but one specified in $SHELL.
export SHELL=/bin/bash
exec conda run -n MTLRank jupyter notebook --config=config.py >> /var/log/jupyter.log 2>&1