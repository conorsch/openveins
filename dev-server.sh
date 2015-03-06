#!/bin/bash
./manage.py migrate
./manage.py collectstatic --noinput
./manage.py clearsessions 
./manage.py runserver [::]:8001 -v 3
