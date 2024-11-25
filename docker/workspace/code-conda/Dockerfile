# syntax=docker/dockerfile:1

# We inherit from an ubuntu image that is modified to support long-running services
# consisting of multiple processes. To learn how to define a background services, 
# consult https://github.com/phusion/baseimage-docker
FROM daemontus/workspace-base-conda:latest

# Install VSCode server.
ARG vscode_version=1.95.2
RUN wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v${vscode_version}/openvscode-server-v${vscode_version}-linux-x64.tar.gz
RUN tar -xzf openvscode-server-v${vscode_version}-linux-x64.tar.gz
RUN mv openvscode-server-v${vscode_version}-linux-x64 /usr/local/vscode
RUN chmod -R a+w /usr/local/vscode

# Register vscode as an always-on service.
RUN mkdir /etc/service/vscode
COPY vscode.service.sh /etc/service/vscode/run
RUN chmod +x /etc/service/vscode/run
EXPOSE 8001

# Add an init script that ensures VSCODE_DATA folders exist before vscode starts.
RUN mkdir -p /etc/my_init.d
COPY 02_init_science.sh  /etc/my_init.d/02_init_science.sh
RUN chmod +x /etc/my_init.d/02_init_science.sh
