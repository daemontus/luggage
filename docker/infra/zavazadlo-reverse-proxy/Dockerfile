FROM nginx:1.24.0

COPY nginx.conf /etc/nginx/nginx.conf
COPY snippets/proxy.conf /etc/nginx/snippets/proxy.conf
COPY snippets/authelia-location.conf /etc/nginx/snippets/authelia-location.conf
COPY snippets/authelia-authrequest.conf /etc/nginx/snippets/authelia-authrequest.conf

COPY sites/auth.conf /etc/nginx/sites/auth.conf
COPY sites/sw.mtlrank.conf /etc/nginx/sites/sw.mtlrank.conf
COPY sites/sw.celloracle.conf /etc/nginx/sites/sw.celloracle.conf
COPY sites/ws.daemontus.code.conf /etc/nginx/sites/ws.daemontus.code.conf
COPY sites/ws.daemontus.lab.conf /etc/nginx/sites/ws.daemontus.lab.conf