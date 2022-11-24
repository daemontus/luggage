# Workspaces

Workspaces are virtual docker environments that each user can configure according to their liking. In theory, every workspace can be unique. We have "baseline" images that a user can start with.

When running an image derived from one of the base images, ensure that:
 
 - The variable `WORKSPACE_USER` provides the name of the user that main services should run as (ideally, the user should exist, but if not, is created on startup).
 - If you want to execute something as the workspace user during startup, place it in `~/.init.sh`.
 - If variables `PRIVATE_KEY` and `PUBLIC_KEY` are provided, an SSH key `workspace` is created in the users directory on startup (you have to load it manually to your ssh agent though). Afterwards, the variables are erased to prevent leaking secrets.