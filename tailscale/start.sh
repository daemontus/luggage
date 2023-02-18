#!/bin/bash

# /boot/config/tailscale/start.sh

# Run the tailscale daemon in a new background session.
# The daemon will use /boot/config/tailscale to store its state.

exec >/tmp/tailscaled.log 2>&1
setsid /usr/sbin/tailscaled -statedir=/boot/config/tailscale/ &