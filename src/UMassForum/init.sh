#! /bin/bash

# A script that automates the reconstruction of the entire database.
rm -f db.sqlite3
<<<<<<< HEAD
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
python3 manage.py migrate
python3 manage.py shell < init.py

=======
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py migrate
python manage.py shell < init.py
>>>>>>> f6465e6102a2f11cdc833ec2ee44ccb53dee0397
