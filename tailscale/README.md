# Native Tailscale setup for Unraid

This folder contains everything that you need to install Tailscale natively on Unraid. As opposed to the [community docker](https://forums.unraid.net/topic/90719-support-tailscale-support-thread/), a native install should be running perpetually even when the docker engine or the drive array is down. **This is essentially a verbatim adaptation of [this gist](https://gist.github.com/shayne/25e194e068751e281937ef68edefb99b), just with slightly clearer documentation.**

 > Normally, you would do these steps over SSH. But you can also do them through the online terminal in the Unraid admin panel (one of the menu items in the top-right corner).

 1. Create a `/boot/config/tailscale` folder.
 2. Copy `install.sh`, `start.sh` and `update.sh` into `/boot/config/tailscale`.
 3. Add the following to the existing `/boot/config/go` script:

 ```
# Start Tailscale on boot.
bash /boot/config/tailscale/install.sh
bash /boot/config/tailscale/start.sh
 ```
 4. Run `bash /boot/config/tailscale/update.sh` to download the latest Tailscale version and start the daemon for the first time.
 5. Login normally through `tailscale up`.
 6. Restart Unraid and run `tailscale status` to verify that (a) Tailscale is now running and (b) you are still logged in.
 7. [Optional: Key expiration] Go to your Tailscale console and disable key expiration for your Unraid machine. Otherwise you will lose access in three months and will need to login again.
 8. [Optional: Automatic updates] Install *User Scripts* Unraid plugin. Then create a new script into which you copy the contents of the `update.sh` file. Set this script to run periodically (e.g. one a week). Alternatively, run `update.sh` manually when you want to update.

**Important:** When using docker, tailscale tends to screw up DNS settings for containers on custom networks. (See also https://github.com/tailscale/tailscale/issues/12108 and https://www.reddit.com/r/docker/comments/1do20m6/docker_container_randomly_losing_ability_to/) To fix this, you should run `tailscale up --stateful-filtering=false`. This should be a permanent setting that persists across restarts, but not sure what's going to happen with this in the future.