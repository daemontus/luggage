# Base workspace image

The base docker is responsible for the essential functionality of our workspace images:

 - It is based on [phusion](https://github.com/phusion/baseimage-docker), a reasonably minimal Ubuntu image that is designed to continuously run *some* services.
 - It installs some missing utilities: `git`, `wget`, `curl`, and `htop`.
 - It assumes `WORKSPACE_USER` specifies the "main" user of this workspace. Every service running in the derived images should run as this user.
 - If the `WORKSPACE_USER` does not exist, the user is created as the first step.
 - If a `PRIVATE_KEY` and `PUBLIC_KEY` is provided, an SSH key is created as `~/.ssh/workspace` (it is not automatically activated though).
 - Finally, at startup, the container will run `~/.startup.sh` (if it exists).


