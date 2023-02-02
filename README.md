# LAB - Class 32/33
## Project: drf-api-permissions-postgres
Author: Monica Ramirez

## Links and Resources

[Django](https://docs.djangoproject.com/en/4.1/)

[Django REST](https://django-rest-framework.org)

[Whitenoise](http://whitenoise.evans.io/en/latest/)

🦄[Gunicorn](https://gunicorn.org/)

🐳[Docker](https://www.docker.com/)

## Description 
This projects was created using Django and Django REST Framework. It is a practice in the creating of an api through DRF and implementing permissions. The Database has mock entries for art, artwork names, and descriptions. This project can also run in a Docker container which runs litesql3, can be modified to run postgress in settings.py and by modifying docker-compose yml. The docker version is running gunicorn and uses whitenoise as middleware. 


## 💻 Setup
In virtual enviroment run `python manage.py runserver` to start app. Once running, database can be accessed through this ip address http://127.0.0.1:8000/api/v1/art/. This file can use either postgres or litesql3 in a docker container. 

 
## Tests
Test for CRUD functionaly of models was implemented. Testing of user model was also created. 


