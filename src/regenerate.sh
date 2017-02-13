#!/bin/sh

rm -f db.sqlite3
python manage.py syncdb --noinput --migrate
python manage.py loaddata initial_user
