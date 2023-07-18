all: build push

user := $(shell whoami)

build: 
	docker build -t "$(user)/dnsmasq" .

push:
	docker push "$(user)/dnsmasq"