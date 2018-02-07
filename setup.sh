#!/bin/sh
. ./env_var.sh

if [ "heroku" = $1 ]; then
  gunicorn -b 0.0.0.0:$PORT index:app --log-file=-
else
  python3 index.py
fi
