# Base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /forecastment_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc  \
    && pip install psycopg2 \
    && pip3 install -r requirements.txt

COPY . .
CMD flask db init ; \
flask db stamp head && \
flask db migrate && \
flask db upgrade && \
gunicorn --workers 4 --timeout 120 -b 0.0.0.0:5000 --reload forecastment:app

