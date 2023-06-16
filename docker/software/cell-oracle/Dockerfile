# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM daemontus/workspace-base:latest

# Update apt cache, just to be safe.
RUN apt-get update --yes

#  (1) 	Some packages that we'll be installing are built from source, 
# 		hence we need GCC to install them (also why we need python3-dev).
RUN apt-get install --yes --no-install-recommends \
	build-essential \
	gcc

#  (2) 	Install Python language with pip package manager.
RUN apt-get install --yes --no-install-recommends \
	python3 \
	python3-pip \
	python3-venv \
	python3-dev

WORKDIR /root

#  (3)	Install Python dependencies (including jupyter notebook).
COPY requirements.python.txt .
# Some transitive dependency has a wrong requirements list, hence these two need to be installed
# specifically *before* we try to install Cell Oracle.
RUN pip3 install numpy cython
RUN pip3 install -r requirements.python.txt

#  (4)	Enable Jupyter notebook on port 8000.
RUN mkdir /etc/service/jupyter
COPY jupyter.service.sh /etc/service/jupyter/run
COPY jupyter.config.py /etc/service/jupyter/config.py
RUN chmod +x /etc/service/jupyter/run
EXPOSE 8000

#  (5)	Ensure notebook directory exists (if we are not attached to a volume).
RUN mkdir -p /root/notebook

#  (6)	Should validate that Cell Oracle is successfully installed.
COPY check.py .
RUN python3 check.py

#  (7) Install BEDtools which are used in some pre-processing steps.
RUN apt-get install bedtools

RUN apt-get update --yes
RUN apt install -y --no-install-recommends software-properties-common dirmngr
# Add the keys
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
# add the R 4.0 repo from CRAN -- adjust 'focal' to 'groovy' or 'bionic' as needed
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"

#  (8)	Install R language. 
# 		This is not required by Cell Oracle, but is used in some pre-processing steps.
RUN apt install --yes --no-install-recommends \
	r-base \
	r-base-dev \
	r-base-core \
	r-recommended

RUN apt install --yes --no-install-recommends \
	libfreetype6-dev \
	libpng-dev \
	libtiff5-dev \
	libjpeg-dev \
	libharfbuzz-dev \
	libfribidi-dev \
	libfontconfig1-dev \
	libxml2-dev

RUN apt install --yes --no-install-recommends \
	libudunits2-dev

RUN apt install --yes --no-install-recommends \
	libgdal-dev \
	gdal-bin

RUN apt install --yes --no-install-recommends \
	libcairo2-dev

RUN apt install --yes --no-install-recommends \
	cmake \
	xorg \
	xorg-dev

#  (9) Install R dependencies (including IRkernel for use with jupyter).
#COPY requirements.R.txt .
COPY requirements.0.R.txt .
RUN Rscript requirements.0.R.txt

COPY requirements.1.R.txt .
RUN Rscript requirements.1.R.txt

COPY requirements.2.R.txt .
RUN Rscript requirements.2.R.txt

COPY requirements.3.R.txt .
RUN Rscript requirements.3.R.txt