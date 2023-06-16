# For reasons unbeknownst to both gods and men, building the official distribution
# from source, as well as the 0.12.0 version, produces completely different results
# in some tutorial examples. I am suspecting a breaking change in some Python 
# dependency, but who knows... At some point, this could become a major problem, but
# for now we can just use the existing image 
FROM kenjikamimoto126/celloracle_ubuntu:0.10.15

ENV DEBIAN_FRONTEND=noninteractive

EXPOSE 8888

RUN apt-get update --yes
RUN apt-get install --yes --no-install-recommends \
	libxml2-dev \
	libcurl4-openssl-dev \
	libssl-dev \
	libfontconfig1-dev \
	libharfbuzz-dev \
	libfribidi-dev \
	libfreetype6-dev \
	libpng-dev \
	libtiff5-dev \
	libjpeg-dev \
	cmake


RUN apt install -y --no-install-recommends software-properties-common dirmngr
# Add the keys
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
# add the R 4.0 repo from CRAN -- adjust 'focal' to 'groovy' or 'bionic' as needed
RUN add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"

RUN apt install --yes --no-install-recommends \
	r-base \
	r-base-dev \
	r-base-core \
	r-recommended

COPY requirements.0.R .
RUN Rscript requirements.0.R

RUN apt install --yes --no-install-recommends \
	libcairo2-dev \
	xorg \
	xorg-dev \
	libudunits2-dev \
	libgdal-dev \
	gdal-bin

COPY requirements.1.R .
RUN Rscript requirements.1.R

SHELL ["/bin/bash", "-c"]

COPY requirements.2.R .

RUN . "$HOME/miniconda/etc/profile.d/conda.sh" \
 	&& export PATH="$HOME/miniconda/bin:${PATH}" \
 	&& conda activate celloracle_env \
 	&& Rscript requirements.2.R

CMD . "$HOME/miniconda/etc/profile.d/conda.sh" \
	&& cd /root/notebook \
 	&& export PATH="$HOME/miniconda/bin:${PATH}" \
 	&& conda activate celloracle_env \
 	&& jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root --no-browser --NotebookApp.token='' --NotebookApp.password=''
