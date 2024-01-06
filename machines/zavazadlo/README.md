This is a very incomplete file, basically just with some useful notes.

### Immich

The setup is based on the official tutorial for docker compose on [unraid](https://immich.app/docs/install/unraid/).
The only change was the addition of resource limits (16/8/4GBs of RAM and 3 CPUs; server only needs 8, microservices and machine learning take 16, redis and postgres take 4).
The official [reverse proxy](https://immich.app/docs/administration/reverse-proxy) guide and 
[OAuth](https://immich.app/docs/administration/oauth) guide worked without major issues.
