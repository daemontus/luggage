# Docker containers

This folder has the relevant docker files that are used to run `luggage` and the associated services. Each container should have:

 - A `README.md` explaining what the container does and how to configure it.
 - A `Makefile` that builds and pushes the container to the account of the current user (use `make all`).
 - An `unraid-*.xml` template file with sensible defaults for running the container. 

 > Unraid templates typically have some sensible default hardware limits (CPU, RAM). You may need to adjust these to your hardware.

 > You can add/remove Unraid templates in `/boot/config/plugins/dockerMan/templates-user`.

Overall, the resources are currently structured as follows:

 - Folder `infra` has all our images related to "infrastructure" (things needed to run things):
    - `dnsmasq`: A for of an existing docker image that runs local a DNS resolver.
 	- `zavazadlo-authelia`: Manages access to non-public services through passwords/2FA on `zavazadlo`.
 	- `zavazadlo-reverse-proxy`: Routes traffic on the `unsigned-short.com` domain to the correct docker images on `zavazadlo`.
 - Folder `software` has various environments that enable specific tools that are otherwise not "stable enough" to run in a general up-to-date container.
 - Folder `workspace` has general-purpose workspace images that run software that can be regularly updated in one shared container.