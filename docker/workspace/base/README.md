# \[Docker\] Workspace (base)

The base docker is responsible for the essential functionality of our workspace images:

 - It is based on [phusion](https://github.com/phusion/baseimage-docker), a reasonably minimal Ubuntu image that is designed to continuously run services that we specify.
 - It installs some missing utilities: `nano`, `git`, `wget`, `curl`, `sudo`, and `htop`.
 - It assumes `WORKSPACE_USER` specifies the "main" user of this workspace (group `2000`). Every larger service running in the derived images should run as this user. 
 - However, it is also possible to not have the `WORKSPACE_USER` and let everything run as `root`. This is discouraged for more complex deployments though.
 - If the `WORKSPACE_USER` does not exist, the user is created as the first step. If the user requires non-trivial setup, it is recommended to create the user in a derived docker image that also performs this setup.
 - If a `PRIVATE_KEY` and `PUBLIC_KEY` is provided, an SSH key is created as `~/.ssh/workspace` and added to the SSH agent (obviously, this does not work if `WORKSPACE_USER` is not provided).
 - Finally, at startup, the container will run `~/.startup.sh` (if it exists).
 - If `ALLOW_SUDO=yes`, the `WORKSPACE_USER` will have sudo rights. Just keep in mind that any installed software is wiped when the docker image is restarted.

### Build and publish

```
docker build -t $USERNAME/workspace-base .
docker push $USERNAME/workspace-base
```


### Mount ownership

By default, mounts to outside filesystems will be owned by `root` which makes some software (like jupyter) malfunction if running as `WORKSPACE_USER`. As such, the container will transfer the ownership of all files in `/home/$WORKSPACE_USER/` to the workspace user on startup. This means that anything that should be accessible through services like jupyter and vscode can be mounted into the home directory and will work automatically (more complex arrangements have to be handled manually).