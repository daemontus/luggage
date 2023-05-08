# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM daemontus/workspace-base:latest

# Update apt cache, just to be safe.
RUN apt-get update --yes

#  (1) 	Install texlive. This is the first step, because it takes forever and 
#		will be rarely updated.
RUN apt-get install --yes --no-install-recommends \
	texlive-full

#  (2) 	Install build essentials (make, gcc, clang, etc.). 
RUN apt-get install --yes --no-install-recommends \
	build-essential \
	pkg-config \
	cmake \
	make \
	gcc \
	clang

#  (3)  Install default version of Java.
RUN apt-get install --yes --no-install-recommends \
	default-jdk

#  (4)	Install "scientific" packages (blas, lapac, and fortran).
RUN apt-get install --yes --no-install-recommends \
	liblapack-dev \
	libopenblas-dev \
	gfortran

#  (5)	Install R language.
RUN apt install --yes --no-install-recommends \
	r-base \
	r-base-dev

#  (6) 	Install Python language with pip package manager.
RUN apt-get install --yes --no-install-recommends \
	python3 \
	python3-pip \
	python3-venv \
	python3-dev

#  (7) 	Install node.js and npm package manager.
RUN apt install --yes --no-install-recommends \
	nodejs \
	npm

#  (8)	Install Python dependencies (including jupyter lab).
COPY requirements.python.txt .
RUN pip3 install -r requirements.python.txt

#  (9) Install R dependencies (mainly IRkernel - depedns on jupyter lab).
COPY requirements.R.txt .
RUN Rscript requirements.R.txt

#  (10) Install VSCode server.
ARG vscode_version=1.73.0
RUN wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v${vscode_version}/openvscode-server-v${vscode_version}-linux-x64.tar.gz
RUN tar -xzf openvscode-server-v${vscode_version}-linux-x64.tar.gz
RUN mv openvscode-server-v${vscode_version}-linux-x64 /usr/local/vscode
RUN chmod -R a+w /usr/local/vscode

#  (11) Copy lab config and register jupyter lab as an always-on service.
RUN mkdir /etc/service/jupyter
COPY jupyter.service.sh /etc/service/jupyter/run
COPY jupyter.config.py /etc/service/jupyter/config.py
RUN chmod +x /etc/service/jupyter/run
EXPOSE 8000

#  (12) Register vscode as an always-on service.
RUN mkdir /etc/service/vscode
COPY vscode.service.sh /etc/service/vscode/run
RUN chmod +x /etc/service/vscode/run
EXPOSE 8001

#  (13) Add an init script that ensures VSCODE_DATA folders exist before vscode starts,
# 		and that jupyter lab is configured properly.
RUN mkdir -p /etc/my_init.d
COPY 02_init_science.sh  /etc/my_init.d/02_init_science.sh
RUN chmod +x /etc/my_init.d/02_init_science.sh

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*