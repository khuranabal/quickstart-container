## Build image

`docker build -t wapi -f Dockerfile .`

## Initialize container to start the api

`docker run --rm -it -p 5000:5000 wapi`
