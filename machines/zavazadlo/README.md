This is a very incomplete file, basically just with some useful notes.

### Share setup

(These are mostly recommendations that we don't need to follow exactly, because they can't always be enforced)

`appdata`: Cache only, stores data for docker containers and other "applications" that are running on the device.

`Archive`: Backups and other "cold storage". Limited to Disk 2 and Disk 3 (2x4TB), with write cache.

`backups_user`: Home folder of the backups user. This is currently mostly unused, except for storing the list of backup locations.

`domains` and `isos`: VM data, currently unused.

`Media`: Mostly for movies, shows and music. Data should be on Disk 4 and Disk 5 (5TB+3TB USB drives) since it is primarily static (so write speed should not matter), but if these fill up, we can expand to Disk 2 and Disk 3.

`Personal`: Stuff like photos, documents and general "data". Similar to archive, but should be for stuff that is actually used from time to time. Currently limited to Disk 1 to limit fragmentation, but can expand to Disk 2 and Disk 3 if needed.

`seafile`: Internal data for Seafile storage. Currently limited to Disk 1 (can expand to Disk 2 and Disk 3 if needed, but hopefully we won't come to that).

`system`: Cache only, docker data and essential VM data (VMs are disabled though).

`ws-daemontus-hdd`: Holds "scientific data". Ideally should be moved away in the near future.

`ws-daemonuts-ssd`: Holds "scientific data". Ideally should be moved away in the near future.

### Immich

The setup is based on the official tutorial for docker compose on [unraid](https://immich.app/docs/install/unraid/).
The only change was the addition of resource limits (16/8/4GBs of RAM and 3 CPUs; server only needs 8, microservices and machine learning take 16, redis and postgres take 4).
The official [reverse proxy](https://immich.app/docs/administration/reverse-proxy) guide and 
[OAuth](https://immich.app/docs/administration/oauth) guide worked without major issues.

### Docker config

Everything should be in these docker compose files, which are deployed using using compose unraid plugin. Some of these files require secrets from `.env` files; These are stored on 1Password.