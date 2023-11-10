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

RUN pip3 install scipy==1.11.3 numpy==1.26.1 tqdm==4.66.1

# Downalod fa2
RUN git clone https://github.com/bhargavchippada/forceatlas2.git
WORKDIR ./forceatlas2
# Note that this is not the recommended method, but the recommended method is broken.
RUN pip install .
WORKDIR ..

# Download SCENIC.
RUN git clone https://github.com/aertslab/scenicplus
WORKDIR ./scenicplus
RUN git reset --hard e4bdd9f5b7fea1a43d5cb55e2ccb3c221fe7d279

# These are the official dependencies of SCENIC+. Unfortunately, a lot of them
# are just git repositories and almost nothing has a fixed version specified, so
# this will probably break at some point. But for the initial version, this 
# should be good enough.
RUN pip3 install -r requirements.txt

# Some other optional dependencies.
RUN pip3 install louvain==0.8.1

# Install the actual SCENIC package.
RUN pip3 install -e .