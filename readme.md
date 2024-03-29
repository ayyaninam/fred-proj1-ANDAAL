
# Andaal Readme

La culture pour le developpement.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Use `.env_prod` for production and `.env_dev` for local

#### If your website have ssl (https):

`PAYPAL_CALLBACK_HTTPS` = `True`\

`EXCHANGE_RATE_API_KEY` = `YOUR-API-KEY` for fetching XAF rate with respect to EURO. \

`SMS_AUTH_SCRETE_KEY` = `YOUR-API-KEY` for sending SMS \

`SMS_SENDER_PHONE_NUMBER` = `YOUR-Mobile-Phone-Number` for sending SMS \

`EMAIL_HOST` = `Your Email host: smtp.gmail.com ` if you are using Gmail \

`EMAIL_USE_TLS` = `True` all modern day email support EMAIL_USE_TLS \

`EMAIL_PORT` Your Email PORT

`EMAIL_HOST_USER` Your Email address

`EMAIL_HOST_PASSWORD` Your Email App Pass 

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
