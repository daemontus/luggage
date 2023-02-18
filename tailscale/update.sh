#!/bin/bash
set -x

# check latest version against what's installed
VER=$(curl -sL https://api.github.com/repos/tailscale/tailscale/releases/latest |  jq -r ".tag_name" | cut -c 2-)
if [ "$VER" = "$(tailscale version | head -n1)" ]; then
    echo "$VER already installed, exiting..."
    exit 0
fi

# download latest version, restart daemon
curl -fsSL -o /boot/config/tailscale/tailscale_static.tgz "https://pkgs.tailscale.com/stable/tailscale_${VER}_amd64.tgz"
if [ $? -eq 0 ]; then
    pkill tailscaled
    sleep 1
    /usr/sbin/tailscaled -cleanup
    bash /boot/config/tailscale/install.sh
    bash /boot/config/tailscale/start.sh
fi