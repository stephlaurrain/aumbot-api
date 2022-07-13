all: build

PROJECT=commercenumerique
CONTAINER_NAME=djangorest_devenv_ctn
IMAGE_NAME=djangorest_devenv_img
DOCKER_USER=docker
REMOTE_ROOT=-w '/root'

start:
	service docker start

listctn: 
	docker container ls --all

listimg:
	docker image ls

rembash:
	docker exec -ti $(CONTAINER_NAME) bash

getip:
	docker inspect $(CONTAINER_NAME) | grep "IPAddress"

restartapache:
	docker exec  $(REMOTE_ROOT) $(CONTAINER_NAME) service apache2 restart

startapache:
	docker exec   $(REMOTE_ROOT) $(CONTAINER_NAME) service apache2 start

startmysql:
	docker exec  $(REMOTE_ROOT) $(CONTAINER_NAME) /etc/init.d/mysql start
 


stopall:
	docker stop $$(docker ps -q -a)

##cleaning
dri:
	docker rmi $$(docker images -q)

drmf: 
	docker rm -f $$(docker ps -q -a)

#clnall: stopall drmf dri prune

clnright:
	docker exec  $(REMOTE_ROOT) $(CONTAINER_NAME) bash -c '/root/install/clnright.sh'

prune:
	docker image prune -a

erase: stopall
	docker container rm $(CONTAINER_NAME) && docker image rm $$(docker images '*$(CONTAINER_NAME)*')
#
# launch
build:
	docker-compose build

up:
	docker-compose up
upd: 
	docker-compose up -d

setpsswd:
	docker exec  $(REMOTE_ROOT)  $(CONTAINER_NAME) passwd docker

buildraw:
	docker build -t $(CONTAINER_NAME) ./docker/build

browser: 
	python3 browser.py

setenv:
	source env/bin/activate

migrate:
	python manage.py migrate

startserver:
	python manage.py runserver



.FORCE:
