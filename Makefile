DOCKER_IMAGE_NAME := anki_swiss_knife
DOCKER_TEST_IMAGE_NAME := ${DOCKER_IMAGE_NAME}_test

build_image:
	docker build -t ${DOCKER_IMAGE_NAME} .

build_test_image: build_image
	docker build -t ${DOCKER_TEST_IMAGE_NAME} -f Dockerfile.test .

clear_dangling_resources:
	docker system prune -f
	docker image prune -f

install:
	poetry install

test:
	poetry run py.test --cov=anki_swiss_knife --cov-report term --cov-report xml --testdox tests/

test_container: build_test_image
	docker run -ti -v tests/:/code/tests/ ${DOCKER_TEST_IMAGE_NAME}