# Docker environment for SocialPageParser

## Project description

This is just a backend and frontend for small project, which parser specified facebook pages for events and posts.
Main purpose is to have dashboard which gonna show you latest events of your favorite pages, also as filtering certain posts, let's say articles and videos or musical posts like soundcloud widgets for example.


## Terminology

* Virtualbox - hypervisor for running host OS to host docker containers
* Docker-machine - allows to organize host os to run docker containers
* Docker-compose - allows to orchestrate docker containers

## Prepare

* Get virtualbox
* Get docker-machine
* Get docker-compose

Or try [docker-toolbox](https://www.docker.com/toolbox) should work for mac and windows.

### Clone project

Clone project to this repo root

```
git clone git@github.com:holms/SocialPageParser.git zohoint
```

### Setup docker

Create virtual machine to host docker containers:

```
docker-machine create -d virtualbox dev
```

To use a docker-compose you need to pass environment

```
eval "$(docker-machine env dev)"
```

### Building containers

```
docker-compose build
```

### Launching containers

```
docker-compose up
```

Launch containers in daemon mode

```
docker-compose up -d
```

## How to launch bash in container

First of all get ID of container

```
docker ps
```

Then launch bash

```
docker exect -it <ID> /bin/bash
```
