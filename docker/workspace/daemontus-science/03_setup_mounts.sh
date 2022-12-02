#!/bin/sh

# The point of this script is to simply create `projects` and `archive`
# directories if they don't exist (not mounted). Or, if they exist (mounted
# from the outside), give the ownership of them to the workspace user so 
# that they can actually access them.

# Technically, this is not necessary on Unraid, as Unraid will 
# automatically mount folders with read-write acess for everyone
# in the container, but other implementations don't do it by default.

mkdir -p /home/$WORKSPACE_USER/projects
mkdir -p /home/$WORKSPACE_USER/archive

chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/projects
chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/archive