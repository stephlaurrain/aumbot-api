PROJECT=commercenumerique

setenv:
	source env/bin/activate

makemigration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

startserver:
	python manage.py runserver

reinitdb:	
	python manage.py makemigrations
	python manage.py migrate

deldb:
	find . -path "./migrations/*.py" -not -name "__init__.py" -delete
	find . -path "./migrations/*.pyc"  -delete
	rm db.sqlite3

initdev:
	python manage.py init_local_dev


.FORCE:
