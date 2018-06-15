python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py makemigrations busqueda
python3 manage.py migrate
python3 manage.py shell < djangocities.py

python3 manage.py createbase --lat 20.5924074 --lng -100.3788854 --keyword "kaah" --city "Santiago de Querétaro" --state "Querétaro" --country "México"
