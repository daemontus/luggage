# Docker DNSMASQ

This is a direct fork of the [opsxcq/docker-dnsmasq](https://github.com/opsxcq/docker-dnsmasq) image. There are no functional changes for now, but we describe how to set it up on Unraid to resolve a domain to the correct local server address. For more information, see either the [dnsmasq documentation](https://wiki.archlinux.org/title/Dnsmasq) or the original [repository](https://github.com/opsxcq/docker-dnsmasq) of this docker image.

### Unraid setup

 1. Create a `appdata/dnsmasq` directory on your Unraid server.
 2. Add a `dns.conf` file to `appdata/dnsmasq` with your configuration (example configuration is given below).
 3. Create an empty `dns.log` file in `appdata/dnsmasq`.

   > Assuming you plan to log all queries and your `appdata` space is limited (e.g. because it is cache only), you may want to create the log file in some other array-backed directory. Note that `dnsmasq` will not clean up the log file regularly!

 3. Setup a new docker container with the following settings (or use `unraid-infra-dnsmasq.xml` template):

   - Network type is set to bridge with a fixed IP address of your choosing.
   - Map path `appdata/dnsmasq/dns.conf` to `/etc/dnsmasq.conf`.
   - Map path `appdata/dnsmasq/dns.log` to `/var/log/dsnmasq.log`.
   - Map port 53 to port 53, both TCP and UDP.

 4. Set the docker container to autostart, and then set your DNS server address on your router to your container IP address.

An example configuration file:

```bash
# Uncomment to log all DNS queries:
# log-queries
# Place to save logs (even if you are not logging queries):
log-facility=/var/log/dnsmasq.log
# Don't use hosts nameservers.
no-resolv
# Fallback to Cloudflare and Google for DNS.
server=1.1.1.1
server=8.8.8.8
# List of custom host-ip mappings. 
# Don't forget to list *all* subdomains that are in use.    
address=/sub.domain.com/192.168.86.10
```

Other notes:
 - In advanced container settings, you can set the container icon to the [logo.png](https://github.com/daemontus/luggage/raw/main/docker/dnsmasq/logo.png) from this repository.
 - If you plan to log all queries, clean up the log files regularly! Otherwise they will accumulate indefinitely.
 - Even if you don't want to log everything all the time, it might be a good idea to enable logging at first to verify that everything is working as expected.
