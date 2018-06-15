
#!/bin/bash
cd /home/libelula/
source my_env/bin/activate
cd Libelulas/
pip install -r requirements.txt
git pull origin master
python manage.py makemigrations jugadora
python manage.py migrate
python manage.py makemigrations equipo
python manage.py migrate
python manage.py makemigrations torneo
python manage.py migrate
python manage.py makemigrations coaches
python manage.py migrate
sudo systemctl restart gunicorn
deactivate
cd ~
