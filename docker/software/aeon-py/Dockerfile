# syntax=docker/dockerfile:1
FROM daemontus/workspace-base:latest

# Update apt cache, just to be safe.
RUN apt-get update --yes

# Some of the Python dependencies have C dependencies that
# need to be built somehow.
RUN apt-get install --yes --no-install-recommends \
	build-essential \
	pkg-config \
	cmake \
	make \
	gcc \
	clang

RUN apt-get install --yes --no-install-recommends \
	python3 \
	python3-dev \
	python3-pip

# Install jupter notebooks
RUN pip install notebook

# Ensure notebook directory exists (in case we are not attached to a volume).
RUN mkdir -p /root/notebook

# Enable Jupyter notebook on port 8000.
RUN mkdir /etc/service/jupyter
COPY jupyter.service.sh /etc/service/jupyter/run
COPY jupyter.config.py /etc/service/jupyter/config.py
RUN chmod +x /etc/service/jupyter/run
EXPOSE 8000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt