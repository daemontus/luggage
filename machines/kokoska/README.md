## Omada controller

To run the controller, use:

```
docker run -d \
  --name omada-controller \
  --restart unless-stopped \
  --ulimit nofile=4096:8192 \
  --net host \
  -e MANAGE_HTTP_PORT=8088 \
  -e MANAGE_HTTPS_PORT=8043 \
  -e PGID="508" \
  -e PORTAL_HTTP_PORT=8088 \
  -e PORTAL_HTTPS_PORT=8843 \
  -e PORT_ADOPT_V1=29812 \
  -e PORT_APP_DISCOVERY=27001 \
  -e PORT_DISCOVERY=29810 \
  -e PORT_MANAGER_V1=29811 \
  -e PORT_MANAGER_V2=29814 \
  -e PORT_TRANSFER_V2=29815 \
  -e PORT_RTTY=29816 \
  -e PORT_UPGRADE_V1=29813 \
  -e PUID="508" \
  -e SHOW_SERVER_LOGS=true \
  -e SHOW_MONGODB_LOGS=false \
  -e SSL_CERT_NAME="tls.crt" \
  -e SSL_KEY_NAME="tls.key" \
  -e TZ=Etc/UTC \
  -v omada-data:/opt/tplink/EAPController/data \
  -v omada-logs:/opt/tplink/EAPController/logs \
  mbentley/omada-controller:5.13
```

To upgrade the controller, find the ID of the container through `docker ps`. Then run `docker stop -t 360 $ID` and `docker rm $ID`. Then update the version in the command above and run it (or consult the container documentation to see if there are any new steps you need to take before you upgrade).

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