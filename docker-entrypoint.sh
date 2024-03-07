#!/usr/bin/sh

flask db upgrade
exec gunicorn --bin 0.0.0.0:80 "app:create_app()"