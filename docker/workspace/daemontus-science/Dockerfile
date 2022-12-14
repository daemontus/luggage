# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM daemontus/workspace-base-science:latest

# Register my defualt username and create the main docker user.
ARG workspace_user=daemontus
ENV WORKSPACE_USER=$workspace_user
RUN useradd -u 1000 -g workspace -s /bin/bash -m $WORKSPACE_USER

# Update apt cache, just to be safe.
RUN apt-get update --yes

# ASP, SMT are just for general science stuff.
# libssl is for rust/cargo/tarpaulin
# uuid is for R/bigmemory which we need for scBoolSeq
RUN apt-get install --yes --no-install-recommends \
	z3 \
	gringo \
	libssl-dev \
	uuid-dev \
	graphviz \
	clang \
	jq

USER ${workspace_user}
# Install stable Rust as local user (it should update path, but not in here, 
# so we have to use the whole binary path).
ARG rust_version=1.65.0
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain ${rust_version}
RUN /home/$WORKSPACE_USER/.cargo/bin/cargo install cargo-make
RUN /home/$WORKSPACE_USER/.cargo/bin/cargo install cargo-tarpaulin

# Go back to root.
USER root

# Install my R dependencies.
COPY requirements.R.txt .
RUN Rscript requirements.R.txt

# Install my Python dependencies.
COPY requirements.python.txt .
RUN pip3 install -r requirements.python.txt

# rpy2 and scBoolseq are a bit special :(
# There seems to be a cffi version mismatch *somewhere* in the Python
# build tools and these commands fix it for some reason. Go figure...
RUN pip3 install pip --upgrade
RUN pip3 install setuptools --upgrade
RUN pip3 install wheel --upgrade
RUN pip3 install cffi==1.15.1
RUN pip3 install rpy2==3.5.6
RUN pip3 install scBoolSeq==0.8.3

# Copy the user startup script (does nothing right now).
COPY startup.sh /home/$WORKSPACE_USER/.startup.sh
RUN chmod +x /home/$WORKSPACE_USER/.startup.sh
RUN chown $WORKSPACE_USER:workspace /home/$WORKSPACE_USER/.startup.sh

# Turns out, we should also move the ownership of directories that
# we plan to bind our external data to to the workspace user.
# On Unraid, something like this happens automatically, but its
# not a default anywhere else.
RUN mkdir -p /etc/my_init.d
COPY 03_setup_mounts.sh  /etc/my_init.d/03_setup_mounts.sh
RUN chmod +x /etc/my_init.d/03_setup_mounts.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# I keep this here as an extra step because it's probably going 
# to change often.
RUN pip3 install biodivine_aeon==0.2.0a0
