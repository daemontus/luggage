# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM daemontus/workspace-base:latest

#	Install Python language (without pip; we'll use conda).
RUN install_clean python3 python3-dev python3-pip python3-venv

#	Install R language.
RUN install_clean r-base r-base-dev

# 	Install conda.
WORKDIR /root
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py312_24.9.2-0-Linux-x86_64.sh -O miniconda.sh
RUN chmod +x miniconda.sh
RUN ./miniconda.sh -b -p $HOME/miniconda
ENV PATH="${PATH}:/root/miniconda/bin"
# Allow everyone to run conda
RUN chmod a+rx /root

# 	As long as people use bash as their default shell, they should have conda available.
RUN conda init bash