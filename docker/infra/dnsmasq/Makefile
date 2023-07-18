all: build push

user := $(shell whoami)

build: 
	echo $(user)
	docker build -t "$(user)/dnsmasq" .

push:
	docker push "$(user)/dnsmasq"