#!/bin/bash

export UID_FOR_DOCKER=$(id -u)
export GID_FOR_DOCKER=$(id -g)
export USERNAME_FOR_DOCKER=$(whoami)

docker compose up -d
