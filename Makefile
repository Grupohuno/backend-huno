
up:
	docker-compose up --build

build:
	docker-compose build

down:
	docker-compose down

migrate!:
	docker-compose run api python manage.py migrate

makemigrations!:
	docker-compose run api python manage.py makemigrations

superup:
	docker-compose run api python manage.py makemigrations
	docker-compose run api python manage.py migrate
	docker-compose up --build -d

black:
	docker-compose run api black ./*.py ./api/*.py ./store/*.py ./store/tests/*.py

# flake8:
# 	docker-compose run app flake8 *.py

pylint:
	docker-compose run api pylint  ./*.py ./api/*.py ./store/*.py ./store/tests/*.py

test:
	docker-compose run api pytest

supertest:
	sudo docker-compose run api python manage.py makemigrations
	sudo docker-compose run api python manage.py migrate
	sudo docker-compose run api pytest

seeds!:
	docker-compose run api python manage.py loaddata store/seeds/*.json