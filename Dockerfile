
FROM python:3.10.7-alpine 

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt /app
RUN pip install -r requirements.txt

# copy project
COPY . /app


ARG SENTRY_DNS
ENV SENTRY_DNS=$SENTRY_DNS
ARG SECRET_KEY_DJANGO
ENV SECRET_KEY_DJANGO=$SECRET_KEY_DJANGO



RUN python manage.py collectstatic --noinput

# Exposez le port sur lequel Django écoute
EXPOSE 8000

# purposes the "base" image is used here.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

