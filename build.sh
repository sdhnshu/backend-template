#!/bin/sh
if test -z "$1"
then
    echo "No env given"
    exit
else
    echo "Building for env: $1"
fi
# $(aws ecr get-login --no-include-email --region ap-south-1)
docker build -t backend-$1 --build-arg BUILD_ENV=$1 .
# docker tag backend-$1:latest 000000000000.dkr.ecr.ap-south-1.amazonaws.com/backend-$1:latest
# docker push 000000000000.dkr.ecr.ap-south-1.amazonaws.com/backend-$1:latest