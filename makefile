test:
	make up
	docker-compose run web python manage.py test
up:
	docker-compose up -d
down:
	docker-compose down
bash:
	docker-compose run web bash
build:
	docker-compose build
static: FORCE
	docker-compose run web /bin/sh -c "python manage.py collectstatic --no-input"  
FORCE:
