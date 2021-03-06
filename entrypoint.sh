#!/bin/sh
flask db migrate
flask db upgrade
# gunicorn wsgi:app -w 1 -b 0.0.0.0:5000 --capture-output --log-level debug --reload
export FLASK_ENV=development
flask run --host=0.0.0.0