# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM daemontus/workspace-base:latest

# Update apt cache, just to be safe.
RUN apt-get update --yes

#	Install Python language (without pip; we'll use conda).
RUN apt-get install --yes --no-install-recommends \
	python3 \
	python3-dev

#	Install R language.
RUN apt install --yes --no-install-recommends \
	r-base \
	r-base-dev

WORKDIR /root
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh -O miniconda.sh
RUN chmod +x miniconda.sh
RUN ./miniconda.sh -b -p $HOME/miniconda
ENV PATH="${PATH}:/root/miniconda/bin"