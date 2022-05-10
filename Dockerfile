FROM python:latest

COPY ./requirements.txt .

RUN apt-get update && apt-get upgrade -y
RUN pip install -r requirements.txt