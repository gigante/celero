.PHONY: install db test static back run

export HOST=localhost
export BACK_PORT=8000
export DB_NAME=celero

install:
	@pipenv install --skip-lock --dev

db:
	@echo "== DROP DATABASE =="
	@dropdb --if-exists $(DB_NAME)
	@echo '> OK'
	@echo "== CREATE DATABASE =="
	@createdb $(DB_NAME)
	@echo '> OK'
	@echo "== APPLY MIGRATIONS =="
	@python ./manage.py migrate
	@echo '> OK'

test:
	@python manage.py test

static:
	@echo '== CLEANING UP STATIC =='
	@rm -rf backend/static
	@echo '> OK'
	@python ./manage.py collectstatic

run:
	@python manage.py runserver_plus $(HOST):$(BACK_PORT)
