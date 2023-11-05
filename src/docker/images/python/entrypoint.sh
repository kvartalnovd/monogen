#!/usr/bin/env bash

PYTHONPATH="$( dirname "$(pwd)")";
export PYTHONPATH;

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )";

# Changes the folder to: repository: /src/server | Docker: /usr/src/app/server
cd "$(dirname "$(dirname "$(dirname "${SCRIPT_DIR}")")")"/server || exit;

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
#gunicorn config.wsgi:application --bind 0.0.0.0:8000
daphne -b 0.0.0.0 -p 8000 config.asgi:application
