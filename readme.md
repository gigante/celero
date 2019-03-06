# Celero [![Build Status](https://travis-ci.com/gigante/celero.svg?token=TjraJrya6tP6gQkwQ3xk&branch=master)](https://travis-ci.com/gigante/celero) [![Maintainability](https://api.codeclimate.com/v1/badges/4934f9263ab5e221c4b3/maintainability)](https://codeclimate.com/repos/5c7fd947c1be5c29740034fd/maintainability)

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

## Api examples

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

```
$ make test
```