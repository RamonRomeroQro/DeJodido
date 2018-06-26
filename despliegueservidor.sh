
#!/bin/bash
cd /home/jodido/
source venv/bin/activate
cd NewJodido/
pip install -r requirements.txt
git pull origin master
python manage.py makemigrations landing
python manage.py migrate
python manage.py makemigrations lugares
python manage.py migrate
python manage.py makemigrations usuarios
python manage.py migrate
sudo systemctl restart gunicorn
deactivate
cd ~
