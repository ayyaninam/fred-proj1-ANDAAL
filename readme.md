
## Run Locally

Clone the project

```bash
  git clone https://github.com/ayyaninam/fred-proj1-ANDAAL
```

Go to the project directory

```bash
  cd fred-proj1-ANDAAL
```

New Virtual Environment

```bash
  python3 -m venv env
```

Active Virtual Environment 


Mac/Linux:

```bash
  source env/bin/activate
```

Windows:

```bash
  env\Scripts\bin\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Make Migrations

```bash
  python3 manage.py makemigrations
```

Migrate

```bash
  python3 manage.py migrate
```


Base Make Migrations

```bash
  python3 manage.py makemigrations base
```

Base Migrate

```bash
  python3 manage.py migrate base
```

Run Redis Services

```bash
  redis-server
```

Run Celery Services

```bash
  celery -A proj1 worker -l info
```