#!/usr/bin/env bash

docker stop -f $(docker ps | grep lamp)