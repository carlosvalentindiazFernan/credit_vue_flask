#  Credit Api



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes


### Installing



```shell

$pip install -r requirements.txt

```

And run

```shell

$ vagrant up

```


```shell

$ docker run --name data-credit -e POSTGRES_PASSWORD=mysecretpassword -e \ POSTGRES_USER=psqlm -e POSTGRES_DB=creditDB -d postgres

```


## Built With

* [Flask](http://flask.pocoo.org/)
* [Vagrant](https://www.vagrantup.com/)

