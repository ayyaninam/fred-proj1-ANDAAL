
# Andaal Readme

La culture pour le developpement.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Use `.env_prod` for production and `.env_dev` for local

#### If your website have ssl (https):

`PAYPAL_CALLBACK_HTTPS` = `True`\

`EXCHANGE_RATE_API_KEY` = `YOUR-API-KEY` for fetching XAF rate with respect to EURO. \

`REFRESH_XAF_RATE_AFTER_SEC` = `Time Gap` in seconds for fetching the XAF rate with respect to EURO. \

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



# Migrate from SQLITE to PSQL

Breif description on how to migrate the data from sqlite to PSQL

## Prefer for only Production

Step 1: Install the PSQL \
Step 2: Install the requirements.txt

```bash
pip install -r requirements.txt
```
Step 3: Dump all the Data \
Or you can grab the data.json file from the proj directory. \
I already created that.\
Please Run this command in project directory to create data.json file.

```bash
python3 manage.py dumpdata --all > data.json
```

Step 4: Create DB Schema.

```bash
python3 manage.py sqlflush > schema.sql
```

Step 5: Launch the PSQL

Step 6: Create the DB (with your prefer pass and name) \

Step 7: Run this command to load the Schema in your database.

```bash
\i PATH_TO_schema.sql
```

Step 8: Go to the ``.env_prod`` or ```.env_dev``` and change the DB extensions accordingly. 

```bash
pip install -r requirements.txt
```


## Note:
```bash
\i PATH_TO_schema.sql
```
If this command make some problem.\
Then Go to the project ```.env``` and change the DB extension to connect to PSQL.\
After that, run:
```bash
python3 manage.py migrate
```
Then Repeat the Step 7 and Step 8.

```bash
python3 manage.py loaddata data.json
```

# Static Files (if you aren't use NGINX in Production)

```bash
python3 manage.py collectstatic
```

This will push all your Static files in new Folder.\
Then ```whitenoise``` will take care of all the Static Files.\
Delete or Comment this line:
```bash 
whitenoise.runserver_nostatic
```
and this line:
```bash
whitenoise.middleware.WhiteNoiseMiddleware
```
Currently at: line no: 30 and 102 in settings.py\
If you want NGINX to take care of Static files.