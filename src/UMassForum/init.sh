#! /bin/bash

# A script that automates the reconstruction of the entire database.
rm -rf db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py migrate
python3 manage.py shell < init.py
