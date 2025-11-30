## Initial setup

 - Set hostname to `kokoska` in "System".
 - Set root password and add SSH keys in "Administration". Test that SSH access works.
 - Set up static DHCP: 	
 	- AC:15:A2:4A:91:DE (Obyvacka.lan) | 192.168.2.100
 	- 9C:53:22:4D:D7:88 (Izba.lan) | 192.168.2.101 	
 	- 08:F9:E0:56:A4:9C (prusa-mk4.lan) | 192.168.2.135
 - Setup `tailscale` using the [official guide](https://openwrt.org/docs/guide-user/services/vpn/tailscale/start). Make sure to disable expiry and run with `tailscale up --advertise-exit-node --stateful-filtering=false`.
 - Configure the IPv6 settings:
 	- IPv6 static address: 2001:4de8:fa2b::4:645:2/112
 	- IPv6 gateway: 2001:4de8:fa2b::4:645:1
 	- IPv6 routed prefix: 2001:4de8:fa2b:1080::/60
 	- DNS: 2606:4700:4700::1111 (Cloudflare) / 2001:4860:4860::8888 (Google) 	

## Omada controller

To run the controller, use the provided `docker-compose.yml` file (`docker compose up -d`). For the sake of simplicity, the compose file is just copied to the router at this point (without cloning the whole repository).

To upgrade the controller, update the version in the `docker-compose.yml` file (ALWAYS CHECK THE REPOSITORY FOR BREAKING CHANGES) and then run:

```
docker-compose pull
docker-compose up --force-recreate --build -d
docker image prune -f
```

Once the controller is running, make sure to enable [fast roaming](https://www.tp-link.com/us/support/faq/4304/).

## Power spec

#### Switch/PoE

[TP-LINK](https://www.tp-link.com/uk/business-networking/poe-switch/tl-sg1005lp/)

53.5V, 0.81A ~ 43W, up to 40W on PoE

Devices:
	- Switch itself (4.12W).
	- 2x Wifi access point (up to 10W each).
		* [TP-LINK](https://www.tp-link.com/us/business-networking/omada-sdn-access-point/eap615-wall/)
		* Can passthrough up to 13W PoE, but we don't use it right now.

Overall should be 24W/43W.

#### Pico PSU

[AliExpress](https://www.aliexpress.com/item/32816006065.html?spm=a2g0o.order_list.order_list_main.21.47c41802PKFL67#nav-review)

12V input. Currently an old adapter from Synology: 12V, 4.16A ~ 50W.

PSU max load (see spec sheet):
	- 20-30W on 5V
	- 60-96W on 12V

Devices:
	- NanoPi RS5 (<10W peak over 5V, 4-6W typical).
		* [Wiki](https://wiki.friendlyelec.com/wiki/index.php/NanoPi_R5S).
		* Needs a very sketchy custom USB-C 5V cable.
	- 2x 3.5" HDD (5V, 0.7A, 3.5W; 12V, 0.55A 6.6W).
		* Alternatively, a 2.5" drive, (5V, 1.1A, 5.5W, but some sources show less).

Overall, should be ~17-20W/20W on 5V and ~14W/60W on 12V. Together, less than 40W/50W w.r.t. the AC/DC adapter.

## Adding SATA/USB drives

If you want to use a SATA/USB disk, you probably need to add support for `ext4`, such as outlined [here](https://openwrt.org/docs/guide-user/storage/usb-drives). Also, [this](https://phoenixnap.com/kb/linux-format-disk) and [this](https://wiki.archlinux.org/title/Parted) is useful to read about how to partition the drive.

Afterwards, you can setup a mount point in the admin `System -> Mount Points -> Add -> Save and apply`. In this case, we are mounting it to `/mnt/hdd`.

Also, the OpenWRT page has a ton of info about how to spin down a drive to save power. Just note that spindown is not supported by default, you have to install it.

#### Add a new user just for sharing

Ideally, create a new user:

```
opkg install shadow-useradd
useradd --system sharing
id -u sharing
```

#### Create NFS share

If you then want to setup an NFS share, read about it [here](https://openwrt.org/docs/guide-user/services/nas/nfs_configuration). Just make sure to properly set an IP/mask for the share so that it is only accessible from the local network (`192.168.2.0/24`).

Then, in `/etc/exports`, set up the share:
```
/mnt/hdd        192.168.2.0/24(rw,insecure,async,no_subtree_check,all_squash,anonuid=999,anongid=0)
```

Here, `anonuid` and `anongid` are set to match the ID and group ID of the new `sharing` user. Hence everything read/written on this share over the network should belong to `sharing`.

Finally, use `service nfsd reload` to restart the NFS service.

Afterwards, you can mount this share (on linux) by running as `root`:

```
mkdir /mnt/hdd
mount -t nfs kokoska:/mnt/hdd /mnt/hdd
```

However, for some reason this will not be always write-able/accessible on macOS. Hence you probably also want to configure SMB.

#### Create SMB share

You can mostly follow [this guide](https://openwrt.org/docs/guide-user/services/nas/samba_configuration). At some point, you'll probably need to use `samba4` instad of `samba`. Also, the note about `security = user` in "share level access" section is outdated.

This is what `/etc/config/samba4` should look like in the end:

```
config samba
        option workgroup 'WORKGROUP'
        option charset 'UTF-8'
        option name 'Kokoska'
        option description 'Kokoska'
        option homes '1'

config 'sambashare'
        option 'name' 'HDD'
        option 'path' '/mnt/hdd'
        option read_only 'no'
        option guest_ok 'yes'
```

Furthermore, in `/etc/samba/smb.cont.template`, you should update/uncomment the following:

```
# This enables guest login for any user, as long as it is enabled for the share in question.
security = user
map to guest = Bad Password
# Remap group/owner of all file transfers to our sharing user.
force group = root
force user = sharing
```

Finally, restart samba service: `service samba4 restart`.