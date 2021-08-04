# Python sample application

[![MIT licensed](https://img.shields.io/badge/license-MIT-white.svg)](./LICENSE)

![Docker Pulls](https://img.shields.io/docker/pulls/flanciskinho/example-photoscore-python.svg)
![Docker Stars](https://img.shields.io/docker/stars/flanciskinho/example-photoscore-python.svg)

This repository is a proof of concept.

The idea is to develop a very simple python web application in which you can use photoilike services. The service that this application uses is PhotoScore (to increase the speed the requests are made in parallel).

## Screenshots

![Home page](example/home.png?raw=true "Home Page")
![Result page](example/result.png?raw=true "Result Page")

## Building

```
docker build -t flanciskinho/example-photoscore-python .
```

## Launch web app

```
docker run -d --rm -p 80:80 flanciskinho/example-photoscore-python
```
