.PHONY: build run bash stop clean logs build-no-cache

# Variables
IMAGE_NAME = ibanfirst-api
CONTAINER_NAME = ibanfirst-api
PORT = 5000

# Commandes Docker
build:
	docker build -t $(IMAGE_NAME) .

build-no-cache:
	docker build --no-cache -t $(IMAGE_NAME) .

run:
	docker run -d \
		--name $(CONTAINER_NAME) \
		-p $(PORT):$(PORT) \
		--env-file .env.production \
		$(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

bash:
	docker exec -it $(CONTAINER_NAME) bash

clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

logs:
	docker logs -f $(CONTAINER_NAME)
