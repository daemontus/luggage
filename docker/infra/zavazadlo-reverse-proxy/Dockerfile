FROM nginx:1.26.0

COPY nginx.conf /etc/nginx/nginx.conf
COPY snippets/cors.conf /etc/nginx/snippets/cors.conf
COPY snippets/proxy.conf /etc/nginx/snippets/proxy.conf
COPY snippets/authelia-location.conf /etc/nginx/snippets/authelia-location.conf
COPY snippets/authelia-authrequest.conf /etc/nginx/snippets/authelia-authrequest.conf

COPY sites/auth.conf /etc/nginx/sites/auth.conf
COPY sites/plex.conf /etc/nginx/sites/plex.conf
COPY sites/portal.conf /etc/nginx/sites/portal.conf
COPY sites/seafile.conf /etc/nginx/sites/seafile.conf
COPY sites/download.conf /etc/nginx/sites/download.conf
COPY sites/immich.conf /etc/nginx/sites/immich.conf
COPY sites/filebrowser.conf /etc/nginx/sites/filebrowser.conf
COPY sites/matrix.conf /etc/nginx/sites/matrix.conf

COPY sites/sw.mtlrank.conf /etc/nginx/sites/sw.mtlrank.conf
COPY sites/sw.celloracle.conf /etc/nginx/sites/sw.celloracle.conf
COPY sites/sw.stream.conf /etc/nginx/sites/sw.stream.conf

COPY sites/bbm.backend.conf /etc/nginx/sites/bbm.backend.conf
COPY sites/bbm.frontend.conf /etc/nginx/sites/bbm.frontend.conf
COPY sites/websockets.conf /etc/nginx/sites/websockets.conf

COPY sites/ms.sw.stream.conf /etc/nginx/sites/ms.sw.stream.conf
COPY sites/ms.sw.celloracle.conf /etc/nginx/sites/ms.sw.celloracle.conf
COPY sites/ms.sw.scenic.conf /etc/nginx/sites/ms.sw.scenic.conf
COPY sites/ms.sw.scboolseq.conf /etc/nginx/sites/ms.sw.scboolseq.conf
COPY sites/ms.sw.genie3.conf /etc/nginx/sites/ms.sw.genie3.conf
COPY sites/ms.sw.aeon.conf /etc/nginx/sites/ms.sw.aeon.conf
COPY sites/ms.gpu.conf /etc/nginx/sites/ms.gpu.conf

COPY sites/ws.daemontus.code.conf /etc/nginx/sites/ws.daemontus.code.conf
COPY sites/ws.daemontus.lab.conf /etc/nginx/sites/ws.daemontus.lab.conf
COPY sites/ws.florekova.code.conf /etc/nginx/sites/ws.florekova.code.conf
COPY sites/ws.florekova.lab.conf /etc/nginx/sites/ws.florekova.lab.conf
COPY sites/ws.kuzlik.code.conf /etc/nginx/sites/ws.kuzlik.code.conf
COPY sites/ws.kuzlik.lab.conf /etc/nginx/sites/ws.kuzlik.lab.conf
COPY sites/ws.hakos.code.conf /etc/nginx/sites/ws.hakos.code.conf