# ToDo List Application

## Quick Start
Prepare Python env and fetch dependencies

```shell script
python -m venv env
env\scripts\activate
pip install -r todo/requirements.txt
```

Make/run migration and start server
```shell script
cd todo
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Init data
```shell script
python3 manage.py loaddata initial_role_data.json
```