# traffic_director_system

## Setup (To run locally)
- Clone this git repository and cd into it:
    - git clone https://github.com/SerGandrex/traffic_director_system.git
    - cd traffic_director_system/

- Create virtualenv:
  - virtualenv --python=python3.6 venv
  
- activate virtualenv:
  - source venv/bin/activate
  
- Install requirements:
  - pip install -r requirements.txt

- Database migrations:
  
  - change database parameters in traffic_director_system/settings.py DATABASE section
  - set 'HOST': 'localhost',
  - create a database in psql:
  - CREATE DATABASE traffic_director_system_db;
  - python manage.py makemigrations
  - python manage.py migrate

- Run application:
  - python manage.py runserver
  
## Setup (To run dockerized solution)
  - change database parameters in traffic_director_system/settings.py DATABASE section
  - set 'HOST': 'db',
  - docker build -t traffic-web:0.1 .
  - docker-compose up -d
  - open http://0.0.0.0:8020/