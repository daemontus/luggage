# Docker DNSMASQ

This is a direct fork of the [opsxcq/docker-dnsmasq](https://github.com/opsxcq/docker-dnsmasq) image. There are no functional changes for now, but we describe how to set it up on Unraid to resolve our domain to the correct server address. For more information, see either the [dnsmasq documentation](https://wiki.archlinux.org/title/Dnsmasq) or the original [repository](https://github.com/opsxcq/docker-dnsmasq) of this docker image.

### Unraid setup

 1. Create a `appdata/dnsmasq` directory on your Unraid server.
 2. Add a `dns.conf` file to `appdata/dnsmasq` with your configuration (example configuration is given below).
 3. Create an empty `dns.log` file in `appdata/dnsmasq`.

   > Alternatively, assuming you plan to log all queries and your `appdata` space is limited (e.g. because it is cache only), you may want to create the log file in some other array-backed directory. The log file should not grow too large, but it can still accumulate over time. 

 3. Setup a new docker container with the following settings:

   - Network type is set to bridge with a fixed IP address.
   - Map path `appdata/dnsmasq/dns.conf` to `/etc/dnsmasq.conf`.
   - Map path `appdata/dnsmasq/dns.log` to `/var/log/dsnmasq.log`.
   - Map port 53 to port 53, both TCP and UDP.
   - If you want to, you can set a log url to the `logo.png` in this repository.

 4. Start the docker container and set your DNS server address in your router to your container IP address.


An example configuration file:

```bash
# Log all DNS queries.
log-queries
log-facility=/var/log/dnsmasq.log
# Don't use hosts nameservers.
no-resolv
# Fallback to Cloudflare and Google for DNS.
server=1.1.1.1
server=8.8.8.8
# List of custom host-ip mappings. 
# Don't forget to list *all* subdomains.    
address=/sub.domain.com/192.168.86.10
```