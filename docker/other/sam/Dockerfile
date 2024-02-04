FROM nginx:1.24.0


COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir /www
COPY index.html /www/index.html
COPY static/favicon.ico /www/static/favicon.ico
COPY static/style.css /www/static/style.css