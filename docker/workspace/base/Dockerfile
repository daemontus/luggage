# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:noble-1.0.0
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Everything here applies to the root user's home.
USER root

# Create a workspace group where the workspace user should be placed.
# But let the child docker images initialize the actual user.
RUN groupadd -g 2000 workspace

# Clean install is a special utility provided by phusion which cleans up 
# installation data, but still uses apt.
RUN install_clean git wget curl htop nano screen sudo

#  Copy the initialization scripts.
RUN mkdir -p /etc/my_init.d
COPY 01_init.sh  /etc/my_init.d/
COPY 99_init_user.sh  /etc/my_init.d/
RUN chmod +x /etc/my_init.d/01_init.sh
RUN chmod +x /etc/my_init.d/99_init_user.sh