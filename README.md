
# _De A Jodido:_<br>_an idea by BlackEMail_


### General Structure

* ./api/: Django Rest API FRAMEWORK
* ./deajodido/: Settings, urls, keys and deployment
* ./landing/: General Landing Search
* ./lugares/: Models and views for places
* ./sm/: Super Management and administrative module
* ./static/: FrontEnd Framework dependencies
* ./static/: FrontEnd Framework dependencies
* ./usuarios/: User Models

### Setup Up

1. Create virtual enviroment

    ``` bash

    python3 -m venv venv

    ```
2. Initialize  virtual enviroment

    ``` bash
    source venv/bin/activate
 
    ```
3. Upgrade Package Manager (PIP) 

    ``` bash
    pip3 install --upgrade pip
 
    ```
4. Install dependencies

    ``` bash
    pip3 install -r requirements.txt
 
    ```
5. Setup Postgresql

    ```` bash
   




    # remove old database files (If there was any)# install the binary

    brew install postgresql

    brew services start postgresql
    initdb /usr/local/var/postgres
    /usr/local/opt/postgres/bin/createuser -s postgres
    brew services start postgresql
    psql -d postgres -U postgres -c "drop database deajodido;"
    psql -d postgres -U postgres -c "create database deajodido;"
    



    ```

6. Migrate and run

    ``` bash
   find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
    
    python3 manage.py makemigrations 
    python3 manage.py migrate 
    python3 manage.py makemigrations landing
    python3 manage.py migrate
    python3 manage.py makemigrations lugares
    python3 manage.py migrate
    python3 manage.py makemigrations usuarios
    python3 manage.py migrate
    python3 manage.py makemigrations sm
    python3 manage.py migrate
    ```

7. SU Creation

    ``` bash

    python3 manage.py createsuperuser

    ```
   
8. Install redis
      
    ``` bash
    
        sudo apt install  redis
    ```
    


11. Import or create .env or enviromental variables

    ``` bash
    

    python3 manage.py runserver

    ```
    
## ENV VALS
``` bash 
sudo nano /etc/supervisor/conf.d/deajodido_celery.conf 
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status deajodidocelery
```
## Idea

_**De A Jodido** es un portal en el cual uno busca diferentes opciones de salidas (viajes, tours, vida noctura, etc.) con base a tu presupuesto y preferencias (+ API's). De igual manera, se podrán armar grupos en la mismo portal para expandir la experiencia social y conocer los gustos y recomendaciones del mismo. <br><br>**De A Jodido** ,  a diferencia de las actuales plataformas de viajes o salidas, está hecha por, cómo nos gusta decir, hecha por la raza, para la raza. Esto significa que todas nuestras recomendaciones son hechas por usuarios que ya han tenido estas experiencias y de igual manera son calificadas por otros usuarios._

## Misión

* Nuestra aplicación Permite redescubrir tu ciudad de manera que ajuste a tu presupuesto, mostrándote alternativas a los “lugares de siempre”

## Visión

* Que la aplicación sea el máximo referente cuando alguien diga “¿qué se arma?”


### Colaboradores:

* Alejandro López, @AleLopezPerez
* Ramón Romero, @RamonRomeroQro

# Thanks for the support to all those who supported the development of the idea.

----
