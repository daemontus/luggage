# Luggage infrastructure config

> **Version two is currently under construction. A lot of content here is still "version one" that is being slowly migrated to the new configuration scheme.**

This is (will be?) "version two" of my current personal cloud infrastructure configuration. Compared to version one, the aim is to reduce friction when deploying and overall improve encapsulation and/or reduce blast radius of individual services.

Some usability goals:
 * If possible every service must be accessible using a single unified login.
 * Every user-facing service must be accessible from the whole internet.
 * Meanwhile, every management interface is strictly restricted to VPN access.

Some general goals:
 * The source of truth for every single setting must be stored in git.
 * All secrets must be stored in a password manager or a single `.secrets` file present on the relevant machine.
 * For configuration that involves secrets, the repository must contain information how to generate it using the `.secrets` file.

Some known downsides:
 * At the moment, the admin (me) can ultimately access all the stored data if they choose to. This has unfortunate privacy implications that are hard to solve efficiently (i.e. even if the data is encrypted, the server needs to be able to access it for some tasks).

## Infrastructure overview

**Morlor** Public IPv4 addresses are in short supply, meaning ISPs are now asking non-trivial prices just for the privilage of having a public address (5-10 EUR/month). To deal with this, we now need a small cloud VM that will route traffic from the internet towards our server(s). This is a bit wasteful, but for point-to-point traffic (e.g. TV and Plex server on two "friendly networks"), or LAN-to-LAN traffic (e.g. a seafile client on the same network as seafile server), we should be able to offload some of this traffic to direct IPv6 or Tailscale connections. For everything else, we have Morlor to facilitate and bridge connections. Also, Morlor provides a suite of basic services that are simply useful to have on a managed hardware with high availability guarantees (e.g. our authentication provider).

Lessons learned: 
 * If you have a public IPv4 address (I don't), don't bother with this. 
 * This is still cheaper than buying just the address from a residential ISP.
 * Upfront cost is zero, because it is a managed cloud VM.
 * Repeating cost is ~4 EUR/month (Hetzner), including 10TB of traffic.
 * Other cloud providers tend to have higher bandwidth cost.
 * Depending on your usage patterns, higher bandwidth cost may not be an issue (e.g. streaming a substantial amount of movies and TV shows between two households is still just 0.5TB).

**Kokoska and Veternik** These are managed routers that sit on top of each of our local networks (we have two locations right now). They allow us to (1) perform various routing tricks to avoid sending every piece of data through morlor (some of this could be done through DNS, but a surprising amount of people have custom DNS overrides); (2) run Tailscale subnet routers to federate each local network into one large subnet (important for devices that don't support tailscale, such as TVs); (3) run reverse proxies that are location-specific and actually serve the intercepted morlor traffic to correct hosts; (4) run any other IoT/management software that is only relevant for the local devices.

Lessons learned:
 * You can get very far with a "basic" ISP provided router. 
 * Still, it gets frustrating quickly once you find a thing that is possible in theory but doesn't work on your device.
 * Upfront cost: I am currently quite happy with a FriendlyElec NanoPi R5S that costs ~100e/device. 
 * They do seem powerful enough for even moderately complex tasks and will hopefully run "forever". 
 * You can go much cheaper if you only want 1Gbit (NanoPi R3S can be had for 30-50e). 
 * The point is to have two network interfaces that you can run at full speed, docker support, and OpenWRT.
 * Repeating cost is primarily electricity, which at 5W amounts to ~5 EUR/year.
 * Other network equipement (mainly wifi access points) will add a lot of extra power consumption, but that's unrealted.

**Luggage** Primarily a storage server, but luggage also runs some applications that directly depend on said storage. This helps with latency and even old hardware can run a modest RAID array very well, so there is a lot of extra slack to run other services.

Lessons learned:
 * Don't be *too afraid* of USB HDDs, but their write performance is terrible, so use them for non-critical read-heavy applications.
 * Virtually any 64-bit-era CPU with 2 cores that can run linux will do.
 * Power consumption is a non-trivial factor. However, buying new hardware just for the power consumption is rarely worth it.
 * Upfront cost: Ideally zero, but you can get a full DDR4-era office PC on marketplace for ~200 EUR, DDR3-era PCs go for even less.
 * Repeating cost: At 50W, the electricity cost are ~40 EUR/year.

 **Mystery shack** This is a true "compute node" with high performance CPU and a lot of RAM. Since it is only needed from time-to-time, it is mostly powered off.



**Inspiration for different software that we can run: https://selfh.st/apps/ **