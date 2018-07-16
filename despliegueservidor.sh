
#!/bin/bash
cd /home/jodido/
source venv/bin/activate
cd NewJodido/
git pull origin develop
pip install -r requirements.txt
python manage.py makemigrations landing
python manage.py migrate
python manage.py makemigrations lugares
python manage.py migrate
python manage.py makemigrations usuarios
python manage.py migrate
python manage.py makemigrations eastereggs
python manage.py migrate
sudo systemctl restart gunicorn
deactivate
cd ~
