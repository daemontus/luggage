FROM daemontus/workspace-base-conda:latest

ENV SHELL bash

RUN conda config --add channels defaults
RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda

RUN apt-get update && apt-get install gsl-bin libgsl0-dev -y && apt-get clean

#Install stream package
RUN conda install conda-forge::mamba -y
RUN mamba install python=3.7

# This still has some deprecation warnings and a few plots don't work, but at least it runs.
RUN mamba install stream=1.1 pandas=1.0.5 networkx=2.1 jupyter jupyterlab tzlocal -y && conda clean --all -y
RUN Rscript -e 'install.packages("stringi",repos="https://cloud.r-project.org/")'

##steps to sync with master on github
# RUN packagepath=$(python -c "import stream; print(stream.__path__[0])") && rm -rf ${packagepath}*
# RUN git clone https://github.com/pinellolab/STREAM.git && cd STREAM && python setup.py install && cd .. && rm -Rf STREAM

#run_test
#RUN python -c "import stream; print(stream.__version__)"
#RUN stream_run_test

RUN mkdir /etc/service/jupyter
COPY jupyter.service.sh /etc/service/jupyter/run
COPY jupyter.config.py /etc/service/jupyter/config.py
RUN chmod +x /etc/service/jupyter/run
EXPOSE 8000

RUN mkdir -p /root/notebook
