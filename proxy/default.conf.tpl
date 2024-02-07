server {
    listen ${LISTEN_PORT};

    location /static/ {
        alias /vol/web/;
    }

    location /media/ {
        alias /vol/web/;
   }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    20M;
    }
}