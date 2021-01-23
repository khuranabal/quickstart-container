## Prerequisite

* docker


## Build image

`docker build -t wapi -f sample-http-api/Dockerfile .`

## Initialize container to start the api

`docker run --rm -it -p 5000:5000 wapi`

## Access localhost url to trigger the api

`http://localhost:5000`
