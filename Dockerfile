FROM ubuntu:14.04
MAINTAINER Yamila yamila.ms@gmail.com
WORKDIR /

# Install dependencies
RUN apt-get update && apt-get install -y -qq curl python3-pip git libpq-dev
RUN pip3 install virtualenv

# Configure locales
RUN locale-gen "en_US.UTF-8"
RUN dpkg-reconfigure locales
ENV LC_ALL "en_US.UTF-8"

# Install requirements
RUN virtualenv -p python3 venv
COPY requirements.txt /python-es-web/
RUN /venv/bin/easy_install --upgrade requests
RUN /venv/bin/pip install -r /python-es-web/requirements.txt

# SETUP the application
COPY . /python-es-web

WORKDIR /python-es-web
