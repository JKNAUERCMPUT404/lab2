#!/bin/sh
IMAGE="lab2"

docker rmi -f $IMAGE
docker build -t $IMAGE .
docker run $IMAGE:latest
