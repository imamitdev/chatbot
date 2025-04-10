#!/bin/bash

# On git push, this script will run automatically on server

set -e  # exit if anything fails

echo "Installing requirements"
pip3.11 install --upgrade pip --user
pip3.11 install -r requirements/requirements.txt --user

echo "Collecting Static files"
python3.11 manage.py collectstatic --noinput --settings=chatbot.settings.production

echo "Running migrations"
python3.11 manage.py migrate --settings=chatbot.settings.production

echo "Restarting uwsgi"
touch chatbot/wsgi.py

echo "Updating crons"
crontab < deploy/crons.crontab

echo "Successfully Deployed. Woohoo!"
