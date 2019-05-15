#!/usr/bin/env bash

#export for MacOS
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin


# Ejecutar por primera vez para desarrollo local o restart de base de datos
# Creacion y ejecucion de ambiente virtual

echo "Creacion de ambiente virtual python ((venv))"

python3 -m venv venv
source venv/bin/activate


# Instalacion de requerimientos

echo "Instalacion de dependencias"

pip install --upgrade pip
pip install -r requirements.txtsource venv/bin/activate






# Creacion de base de datos en local

echo "Drop DATABASE deajodido;DROP RolE postgres; CREATE DATABASE deajodido;create user postgres with encrypted password 'postgres';grant all privileges on database deajodido to postgres;" > new.sql
psql < new.sql
rm -rf ./new.sql


# borrando migraciones previas , ejecutar unicamente tras primiera ejecucion a

# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete
# echo ''
# echo 'Borrado de creación de migraciones'
# echo ''

# creando migraciones

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py makemigrations landing
python3 manage.py migrate
python3 manage.py makemigrations lugares
python3 manage.py migrate
python3 manage.py makemigrations usuarios
python3 manage.py migrate
python3 manage.py makemigrations eastereggs
python3 manage.py migrate
python3 manage.py makemigrations sm
python3 manage.py migrate

python3 manage.py makemigrations


echo ''
echo 'Ejecutando de migraciones '
echo ''





python3 manage.py migrate


echo ''
echo '>>>>>>Creacion de superusuario U:jodido  P:jodido '
echo ''
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('jodido', 'jodido@example.com', '0123456abc')"



echo ''
echo 'Corriendo servidor ...'
echo ''

python3 manage.py runserver



#python3 manage.py createbase --lat 20.5924074 --lng -100.3788854 --keyword "Bar Los Amigos" --city "Santiago de Querétaro" --state "Querétaro" --country "México"
