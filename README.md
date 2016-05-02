# Django Ecommerce API services

**Warning** App is very early stage, not ready for use.

Minimal ecommerce django app. It aims to expose API services using [django rest framework](www.django-rest-framework.org/), This api services can be consumed by  any modern frontend javascript framwork like reactjs,angularjs,emberjs etc  to build complete ecommerce application

As we are using [HStoreField](https://docs.djangoproject.com/en/1.9/ref/contrib/postgres/fields/#hstorefield), this app will work only on postgresql.

## Installation
* git clone https://github.com/ayarshabeer/drf_shop.git drf_shop
* cd drf_shop
* Configure in environment variable DRF_SHOP_DATABASE_URL in the format postgresql://[user[:password]@][netloc][:port][/dbname]
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

## Todo
* API Documentaion
* Unit tests
* Granular persmissions and filters
* Checkout & Payment
