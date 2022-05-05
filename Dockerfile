FROM python:latest

COPY ./requirements.txt .
COPY ./protienwizard_installer/. ./protienwizard_installer/.

RUN apt-get update && apt-get upgrade -y
RUN pip install -r requirements.txt