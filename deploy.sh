
#!/bin/bash

source /peddy/venv/bin/activate
cd /peddy/NewJodido
git pull origin master
pip install -r requirements.txt



python manage.py makemigrations lugares
python manage.py migrate
python manage.py makemigrations usuarios
python manage.py migrate
python manage.py makemigrations landing
python manage.py migrate



sudo systemctl restart gunicorn
deactivate
cd









