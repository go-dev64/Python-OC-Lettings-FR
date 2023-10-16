# pull the official base image
FROM python:3.10.7-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# copy project
COPY . /app

# Exposez le port sur lequel Django écoute
EXPOSE 8000

# start django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
