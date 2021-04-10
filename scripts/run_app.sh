#!/usr/bin/env bash

# migrations
python app/manage.py makemigrations
python app/manage.py migrate

# Run Application
python app/manage.py runserver 0.0.0.0:8000