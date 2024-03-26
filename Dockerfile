FROM python:3.11-bullseye

WORKDIR /app

COPY requirements.txt .

RUN apt update && apt-get install -y build-essential && apt-get install -y python3-psycopg2 && \
    apt install -y python3-pip && apt install -y postgresql postgresql-contrib && apt install -y python3-dev libpq-dev \
    && apt install -y git

RUN pip3 install -r requirements.txt

COPY . .



