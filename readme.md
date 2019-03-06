# Celero [![Build Status](https://travis-ci.org/gigante/celero.svg?branch=master)](https://travis-ci.org/gigante/celero) [![Maintainability](https://api.codeclimate.com/v1/badges/c83accfacb782b3726bf/maintainability)](https://codeclimate.com/github/gigante/celero/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/c83accfacb782b3726bf/test_coverage)](https://codeclimate.com/github/gigante/celero/test_coverage) [![Requirements Status](https://requires.io/github/gigante/celero/requirements.svg?branch=master)](https://requires.io/github/gigante/celero/requirements/?branch=master)

Components:
- Django
- Django Rest Framework
- Swagger

## Documentation & live testing

[https://celero.herokuapp.com/](https://celero.herokuapp.com/)

## How to install

1. Clone this repo
2. Install [pipenv](https://github.com/pypa/pipenv)
3. Install deps
4. Activate venv

```
$ git clone https://github.com/gigante/celero
$ pip install --user pipenv
$ make install
$ pipenv shell
```

## Configure and run

1. Copy env example
2. Edit env config
3. Migrate database
4. Create first user
4. Run Celero

```
$ cp .env.example .env
$ $EDITOR .env
$ make db
$ python manage.py createsuperuser
$ make run
```

## Api usage examples

Install [HTTPie](https://httpie.org)

**get token**

```
http post https://celero.herokuapp.com/api/token/get/ username=USER password=PASSWORD
```

**list accounts**

```
$ http get https://celero.herokuapp.com/api/accounts/ Authorization:'JWT TOKEN'
```

**ordering by name (ASC, DESC)**

```
$ http get https://celero.herokuapp.com/api/accounts/?ordering=name
$ http get https://celero.herokuapp.com/api/accounts/?ordering=-name
```

**ordering by value (ASC, DESC)**

```
$ http get https://celero.herokuapp.com/api/accounts/?ordering=currency
$ http get https://celero.herokuapp.com/api/accounts/?ordering=-currency
```

**get one account**

```
$ http get https://celero.herokuapp.com/api/accounts/UUID Authorization:'JWT TOKEN'
```

**create account**

```
$ http post https://celero.herokuapp.com/api/accounts/ Authorization:'JWT TOKEN' name=Fornecedor currency=500, flow=EXP
```

**update account**

```
http put https://celero.herokuapp.com/api/accounts/UUID/ Authorization:'JWT TOKEN' name=FornecedorX currency=501 flow=EXP
```

**update (partial) account**

```
http patch https://celero.herokuapp.com/api/accounts/UUID/ Authorization:'JWT TOKEN' name=Fornecedor
```

## How to test

Test and code coverage

```
$ make test
```
