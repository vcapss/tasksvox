
test: ## Test the project
	python manage.py test

migrate:
	python manage.py migrate

migration:
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser

run: migration migrate ## Sync the database, run collectstatic and start the server
	python manage.py runserver

install:
	pip install -r requirements.txt

worker:
	celery -A understand.tasks worker --loglevel=DEBUG

consumer:
	understand/./manage.py celery beat
