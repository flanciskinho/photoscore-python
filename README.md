# Python sample application

This repository is a proof of concept.

The idea is to develop a very simple python web application in which you can use photoilike services. The service that this application uses is PhotoScore (to increase the speed the requests are made in parallel).

## Building

```
docker build -t photoscore .
```

## Launch web app

```
docker run -d --rm -p 80:80 photoscore
```
