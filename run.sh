#!/bin/bash

CONTAINER_NAME=tiny-django

docker run --rm -p 8000:8000 --name ${CONTAINER_NAME} -v `pwd`/app:/code -w /code btcrs/tinydjango python app.py test
