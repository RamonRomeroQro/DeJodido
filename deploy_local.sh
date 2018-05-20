python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py makemigrations busqueda
python3 manage.py migrate
python3 manage.py shell < djangocities.py

