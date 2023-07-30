#!/bin/bash

vscode_version=1.80.1
wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v${vscode_version}/openvscode-server-v${vscode_version}-linux-x64.tar.gz
tar -xzf openvscode-server-v${vscode_version}-linux-x64.tar.gz
mv openvscode-server-v${vscode_version}-linux-x64 /usr/local/vscode
chmod -R a+w /usr/local/vscode