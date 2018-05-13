
echo "Drop DATABASE jodido;CREATE DATABASE jodido  ;" > new.sql


psql<new.sql

rm -rf ./new.sql

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
echo ''
echo 'Borrado de creación de migraciones'
echo ''

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



