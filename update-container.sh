#!/bin/bash

# Get variables from .env file
export $(cat .env | xargs)

# Authenticate with Docker Hub
docker login -u "$DOCKERHUB_USERNAME" -p "$DOCKERHUB_PASSWORD"

docker-compose down
docker-compose pull
docker-compose up -d