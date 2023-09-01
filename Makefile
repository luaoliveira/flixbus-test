#!/bin/bash

all: build run

build:
	docker build -t fibonacci:latest .

run:
	docker run -d -p 5000:5000 --name fibonacci_api fibonacci:latest

stop:
	docker stop fibonacci_api
	docker rm fibonacci_api
