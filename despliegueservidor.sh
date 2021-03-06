
#!/bin/bash
source venv/bin/activate
git pull origin master
pip install -r requirements.txt
python manage.py makemigrations landing
python manage.py migrate
python manage.py makemigrations lugares
python manage.py migrate
python manage.py makemigrations usuarios
python manage.py migrate
python manage.py makemigrations sm
python manage.py migrate
sudo systemctl restart gunicorn
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart deajodidocelery
sudo supervisorctl status deajodidocelery
deactivate
cd ~
