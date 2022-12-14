# tl-test-task

**Table of contents:**
- [Installation](#install)
- [Migrations](#migrations)
- [Loaddata](#loaddata)
- [Run](#run)


First of all, clone this repository in the folder and open it in cmd

```
git clone https://github.com/khasanovmma/tl-test-task.git
```

## Install

Use the package manager pip to install foobar

```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```


Copy .env.local and paste in the root project directory and configure it

```
.env
```

.env configuration

```
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
NAME=
```

## Migrations
```
python manage.py migrate
```

## Create Super User
```
python manage.py createsuperuser
```

## Loaddata
```
python manage.py loaddata fixtures/structure_app.jon
```


## Run

Default Run the web service
```
python manage.py runserver
```

Run with a specific host and port
```
python manage.py runserver 0.0.0.0:8080
```