FROM python:latest

COPY ./requirements.txt .

RUN apt-get update && apt-get upgrade -y
RUN tar xjf protienwizard_installer/pwiz-bin-linux-x86_64-gcc7-release-3_0_22124_688773f.tar.bz2
RUN pip install -r requirements.txt