# About
This is a multi-app executor that it used when we have some different task in a our applications and want to run them at the same time. It uses SQLAlchemy for ORM and Alembic for database migrations.

# Installation

#### Ubuntu Requirements:
Install some packages:
> $ sudo apt-get install libpq-dev python-dev


#### Python >= 3.8:
For install python >= 3.8:
> $ sudo add-apt-repository ppa:deadsnakes/ppa

> $ sudo apt-get update

> $ sudo apt-get install python3.8 python3.8-distutils

> $ python3.8 -m pip install --upgrade pip setuptools wheel

> $ sudo apt install python3.8-venv python3.8-dev


#### Postgresql:
Install Postgresql Database >= 10:
> $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

> $ echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list

> $ sudo apt-get install postgresql-10


#### Create database:
> $ sudo su postgres

> $ psql

> $ create database NAME;

> $ create user USER with encrypted password 'PASS';

> $ grant all privileges on database NAME to USER;


#### Clone sources

> $ cd /opt

> $ git clone https://github.com/majid/multi-runner-server

> sudo chown -R $user:$user server


#### Create python virtual environment:
> $ cd server/src

> $ python3.8 -m venv .env

> $ source .env/bin/activate

> $ pip install -r ../requirements.txt


#### Change setting of sqlalchemy:
Change applications and database settings

Eexample apps are: 
- example_messages_app: It has only a table
- example_users_app: It has only a table
- example_UDP_app: It has a socket handler app and a table
> $ nano src/setting/settings.py


#### Configs and database migrations
Before run the server check configs and database migrations

> $ nano setting/setting.py

> $ python manage.py --reconfigure

> $ python manage.py --makemigration "MESSAGE"

> $ python manage.py --migrate


#### References:
1. SQLAlchemy ORM Tutorial for Python Developers [link](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/#SQLAlchemy-in-Practice "Link")
2. Schema migrations with Alembic, Python and PostgreSQL [link](https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql "Link")
