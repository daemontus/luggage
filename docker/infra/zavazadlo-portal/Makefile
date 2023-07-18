all: build push

user := $(shell whoami)

build: 
	docker build -t "$(user)/zavazadlo-portal" .

push:
	docker push "$(user)/zavazadlo-portal"