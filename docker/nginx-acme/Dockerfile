FROM nginx:1.29.1

RUN echo "deb [signed-by=/etc/apt/keyrings/nginx-archive-keyring.gpg] https://nginx.org/packages/mainline/debian/ bookworm nginx" > /etc/apt/sources.list.d/nginx.list &&\
    apt-get update && \
    apt-get install -y --no-install-recommends nginx-module-acme && \
    rm -rf /var/lib/apt/lists/*