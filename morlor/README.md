# Morlor Cloud Gateway

Morlor is a small VM running in Hetzner cloud responsible for routing requests from "the open internet" towards our servers.

## Services



## VM Setup

Right now, we don't really have an automated provisioning/setup script, because the actual setup is extremely simple:

 1. Create a Hetzner VM with Debian Trixie and a pre-configured SSH key.
 2. Install `docker` based on official instructions.
 3. Clone the `luggage` repository into the `/root` folder.