.PHONY: venv deps-dev deps-prod db migration static back front run

export HOST=localhost
export FRONT_PORT=5000
export BACK_PORT=8000
export DB_NAME=django_start

venv:
	@pipenv shell

deps-dev:
	@npm --prefix ./frontend install
	@pipenv install --dev

deps-prod:
	@npm --prefix ./frontend install --production
	@pipenv install

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

migration:
	@echo '== CLEANING UP MIGRATIONS =='
	@find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@find . -path "*/migrations/*.pyc"  -delete
	@echo '> OK'
	@echo '== MAKE MIGRATIONS =='
	@python ./manage.py makemigrations
	@echo '> OK'

static:
	@echo '== CLEANING UP STATIC =='
	@rm -rf backend/static
	@echo '> OK'
	@npm --prefix ./frontend run build
	@python ./manage.py collectstatic

back:
	@python ./manage.py runserver_plus $(HOST):$(BACK_PORT)

front:
	HOST=$(HOST) PORT=$(FRONT_PORT) npm --prefix ./frontend run dev

run:
	HOST=$(HOST) PORT=$(FRONT_PORT) npm --prefix ./frontend run dev & python manage.py runserver_plus $(HOST):$(BACK_PORT)
