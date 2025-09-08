- create venv

- py -3.13 -m venv venv
- . venv/Script/activate

- cd config
- pip install -r requirements.txt

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

- Api Document
- Path
  Swagger Document
  {BASE_DIR}/api/schema/swagger-ui/


# Server Setting
# create .dockerignore
- touch .dockerignore

# in nginx

include mime.type;
default_type_application/octet-streem;

# use for static admin file render
