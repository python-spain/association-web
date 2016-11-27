#!/bin/bash
echo "... Updating python-es-web: Fetch code from github"
git fetch origin
git reset --hard origin/master
echo "... Updating python-es-web: Build the docker image"
docker build -t python-es-web:1.0 -f Dockerfile .
echo "... Updating python-es-web: Restart the service"
$DOCKER_COMPOSE -f docker-compose.yml stop python-es-web
$DOCKER_COMPOSE -f docker-compose.yml rm -v -f python-es-web
$DOCKER_COMPOSE -f docker-compose.yml up -d --no-deps python-es-web

