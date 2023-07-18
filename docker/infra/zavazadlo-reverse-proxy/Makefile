all: build push

user := $(shell whoami)

build: 
	echo $(user)
	docker build -t "$(user)/zavazadlo-reverse-proxy" .

push:
	docker push "$(user)/zavazadlo-reverse-proxy"