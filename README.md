# AUMBot-API: API for the Python AUM Bot

The AumBot-API project is a REST API application to be executed with the Python / Selenium project "AumBot" 


## Dev environment

### Virtual environment pipenv

Define virtual environment 

**(YOU MUST BE IN src directory)**

```
python3 -m venv env
```

Use the environment

```
source env/bin/activate
```

### Set environnement into vs code 

```
mkdir .vscode && touch .vscode/settings.json
```

```
{
    "python.defaultInterpreterPath": "./src/env/bin/python",    
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "editor.rulers": [
        79
    ]
}
```

### Install dependencies

```
pip install -r requirements.txt
```

### Prepare migration from models

```
python manage.py makemigrations
```

### Do migrations

```
python manage.py migrate
```

### Init local dev

```
python manage.py init_local_dev
```

### Run server

```
python manage.py runserver
```

## Utils 

### delete migrations

```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

```

```
python manage.py migrate --fake aum zero
```

### List migrations

```
python manage.py showmigrations
```


### Urls

**[admin]http://localhost:8000/admin/login/?next=/admin/**

**[visit]http://localhost:8000/api/visit/**

**[visit by aum_id]http://localhost:8000/api/visit/?aum_id=123541**

## Change server port


### Change host and port :
```
python manage.py runserver 127.0.0.1:7000
```

### Simple port :
```
python manage.py runserver 7000
```

### Running on docker :
```
python manage.py runserver 0:7000
```