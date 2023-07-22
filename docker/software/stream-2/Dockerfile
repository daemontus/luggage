# syntax=docker/dockerfile:1
FROM daemontus/workspace-base:latest


# Update apt cache, just to be safe.
RUN apt-get update --yes

RUN apt-get install --yes --no-install-recommends \
	python3 \
	python3-dev \
	python3-pip

RUN apt-get install --yes --no-install-recommends \
	r-base \
	r-base-dev

RUN apt-get install --yes --no-install-recommends \
	build-essential \
	pkg-config \
	cmake \
	make \
	gcc \
	clang

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update --yes
RUN apt-get install --yes --no-install-recommends \
	python3.7 \
	python3.7-venv \
	python3.7-dev

# Create and activate a python3.7 venv
RUN python3.7 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

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

# Download STREAM.
RUN wget https://github.com/pinellolab/STREAM/archive/refs/tags/v1.1.zip
RUN unzip v1.1.zip

# These are the dependencies specified by the official conda recipe, fixed to versions
# used by the published docker image.
# Also there are a few extra dependencies which were not fixed but help making the whole
# thing work.
RUN pip install \
	umap-learn==0.4.3 \
    numpy==1.17.5 \
    scipy==1.4.1 \
    scikit-learn==0.23.1 \
    matplotlib==3.2.1 \
    seaborn==0.11.0 \
    plotly==4.8.1 \
    statsmodels==0.11.1 \
    anndata==0.6.22.post1 \
    python-slugify==4.0.0 \
    shapely==1.7.0 \
    networkx==2.1 \
    gunicorn==20.0.4 \
    rpy2==2.9.4 \
    numba==0.49.1 \
    tzlocal==2.1 \
    pandas==1.0.4

# Install STREAM.
RUN pip install ./STREAM-1.1

# Install "mainstream" R dependencies.
RUN apt-get install --yes --no-install-recommends \
	r-cran-igraph \
	r-cran-devtools \
	r-cran-ggforce \
	r-cran-systemfonts \
	r-cran-ggsci \
	r-cran-cowplot \
	r-cran-vctrs \
	r-cran-rcpp \
	r-cran-rcppeigen \
	r-cran-ggplot2 \
	r-cran-quantreg

# Install special R dependencies.
COPY install.R .
RUN Rscript install.R