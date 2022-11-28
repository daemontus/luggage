# \[Docker\] Workspace (base)

The base docker is responsible for the essential functionality of our workspace images:

 - It is based on [phusion](https://github.com/phusion/baseimage-docker), a reasonably minimal Ubuntu image that is designed to continuously run services that we specify.
 - It installs some missing utilities: `nano`, `git`, `wget`, `curl`, and `htop`.
 - It assumes `WORKSPACE_USER` specifies the "main" user of this workspace. Every service running in the derived images should run as this user.
 - If the `WORKSPACE_USER` does not exist, the user is created as the first step (but it is recommended that you create the user while making the derived image).
 - If a `PRIVATE_KEY` and `PUBLIC_KEY` is provided, an SSH key is created as `~/.ssh/workspace` and added to the SSH agent.
 - Finally, at startup, the container will run `~/.startup.sh` (if it exists).

### Build and publish

```
docker build -t $USERNAME/workspace-base .
docker push $USERNAME/workspace-base
```