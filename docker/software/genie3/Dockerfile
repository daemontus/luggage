# syntax=docker/dockerfile:1
FROM daemontus/workspace-base:latest

# Update apt cache, just to be safe.
RUN apt-get update --yes

# Install Python
RUN apt-get install --yes --no-install-recommends \
	python3 \
	python3-dev \
	python3-pip

# Install jupyter notebooks
RUN pip install notebook

# Ensure notebook directory exists (in case we are not attached to a volume).
RUN mkdir -p /root/notebook

# Enable Jupyter notebook on port 8000.
RUN mkdir /etc/service/jupyter
COPY jupyter.service.sh /etc/service/jupyter/run
COPY jupyter.config.py /etc/service/jupyter/config.py
RUN chmod +x /etc/service/jupyter/run
EXPOSE 8000

# Copy GENIE3 sources and examples.
COPY ./package /root/notebook/genie3-source
COPY ./data.txt /root/notebook/example/data.txt
COPT ./example.ipynb /root/notebook/example/example.ipynb
COPT ./GENIE3_python_doc.pdf /root/notebook/example/instructions.pdf

RUN pip install /root/notebook/genie3-source
