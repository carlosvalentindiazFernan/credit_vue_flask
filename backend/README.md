#  Credit Api



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes


## Installing

### (Working pip and virtualenv )

Define  Env

```shell

$ export FLASK_ENV=development
$ export DATABASE_URL=sqlite:///example.sqlite
$ export FLASK_APP=manage
$ export SECRET=l^s5%rqakgof#b7(ba-p)-sb5@whu-v7++l(3*9qjt$d#*w1)k

```


```shell

$ pip install -r requirements.txt

```

```shell

(virtualenv)$ python manage.py runserver

```

### Create User for login


```shell

(virtualenv)$ python manage.py createsuperuser

```

### (Working pip and pipenv )


```shell

$ pipenv run python manage.py runserver

```

### Create User for login


```shell

$ pipenv run python manage.py createsuperuser

```

## Run with postgres

This project run sqlite but you can work with psql only run container psql and change env (DATABASE_URL)

```shell

$ docker run --name data-credit -e POSTGRES_PASSWORD=mysecretpassword -e  POSTGRES_DB=creditDB -d -p 5432:5432 postgres

```


## Built With

* [Flask](http://flask.pocoo.org/)
* [Vagrant](https://www.vagrantup.com/)

