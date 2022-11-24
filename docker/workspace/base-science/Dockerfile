# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM phusion/baseimage:jammy-1.0.1
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Everything here applies to the root user's home.
USER root
WORKDIR ~

# Create a workspace group where the workspace user should be placed.
RUN groupadd -g 1000 workspace

#  (1) 	Update apt cache, just to be safe.
RUN apt-get update --yes

#  (2) 	Install texlive. This is the first step, because it takes forever and 
#		will be rarely updated.
RUN apt-get install --yes --no-install-recommends \
	texlive-full

#  (3)	Install general quality of life utilities.
RUN apt-get install --yes --no-install-recommends \
	git \
	wget \
	curl \
	htop \
	sudo

#  (4) 	Install build essentials (make, gcc, etc.). 
RUN apt-get install --yes --no-install-recommends \
	build-essential \
	pkg-config \
	cmake \
	make \
	gcc

#  (5)	Install "scientific" packages (blas, lapac, and fortran).
RUN apt-get install --yes --no-install-recommends \
	liblapack-dev \
	libopenblas-dev \
	gfortran

#  (6)	Install R language.
RUN apt install --yes --no-install-recommends \
	r-base \
	r-base-dev

#  (7) 	Install Python language with pip package manager.
RUN apt-get install --yes --no-install-recommends \
	python3 \
	python3-pip \
	python3-venv \
	python3-dev

#  (8) 	Install node.js and npm package manager.
RUN apt install --yes --no-install-recommends \
	nodejs \
	npm

#  (9)	Install Python dependencies (including jupyter lab).
COPY requirements.python.txt .
RUN pip3 install -r requirements.python.txt

#  (10) Install R dependencies (mainly IRkernel - depedns on jupyter lab).
COPY requirements.R.txt .
RUN Rscript requirements.R.txt

#  (11) Install VSCode server
ARG vscode_version=1.73.0
RUN wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v${vscode_version}/openvscode-server-v${vscode_version}-linux-x64.tar.gz
RUN tar -xzf openvscode-server-v${vscode_version}-linux-x64.tar.gz
RUN mv openvscode-server-v${vscode_version}-linux-x64 /usr/local/vscode
RUN chmod -R a+w /usr/local/vscode

#  (12) Copy lab config and register jupyter lab as an always-on service.
RUN mkdir /etc/service/jupyter
COPY jupyter.service.sh /etc/service/jupyter/run
COPY jupyter.config.py /etc/service/jupyter/config.py
RUN chmod +x /etc/service/jupyter/run

#  (13) Register vscode as an always-on service.
RUN mkdir /etc/service/vscode
COPY vscode.service.sh /etc/service/vscode/run
RUN chmod +x /etc/service/vscode/run

#  (14) Add the root initialization script, which also triggers 
#		the user init script in ~/.init.sh
RUN mkdir -p /etc/my_init.d
COPY init.sh  /etc/my_init.d/02_init.sh
RUN chmod +x /etc/my_init.d/02_init.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*