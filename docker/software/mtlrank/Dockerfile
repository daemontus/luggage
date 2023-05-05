# Our default conda environment
FROM daemontus/workspace-base-conda:latest

RUN git clone --depth=1 --branch v1.0.0 https://github.com/alexQiSong/MTLRank.git

WORKDIR ./MTLRank

RUN conda env create -f MTLRANK_env.yml

RUN mkdir /etc/service/jupyter
COPY jupyter.service.sh /etc/service/jupyter/run
COPY jupyter.config.py /etc/service/jupyter/config.py
RUN chmod +x /etc/service/jupyter/run
EXPOSE 8000
