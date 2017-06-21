#!/bin/bash

CONTAINER_NAME=btcrs/tiny-django

docker run --rm -p 8000:8000 --name ${CONTAINER_NAME} -v `pwd`/app:/code -w /code python app.py runserver
