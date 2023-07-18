all: build push

user := $(shell whoami)

build: 
	docker build -t "$(user)/zavazadlo-reverse-proxy" .

push:
	docker push "$(user)/zavazadlo-reverse-proxy"