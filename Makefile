
up:
	docker-compose up --build

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

# black:
# 	docker-compose run app black *.py

# flake8:
# 	docker-compose run app flake8 *.py

# pylint:
# 	docker-compose run app pylint *.py

# test:
# 	docker-compose run app pytest

# seeds!:
# 	# docker-compose run app python manage.py loaddata seeds.json seeds_binary.json