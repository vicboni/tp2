# Answers

Nom:    BONIFACIO
Prénom: VICTOR
NB:     2

## 1.3
command: docker run -it --rm --name my-running-app my-app-python

## 1.4
answer: Les ports ne sont pas ouverts
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp my-app-python

## 1.5
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp -e ENVIRONMENT=python:3-alpine my-app-python

## 1.6
answer:
command: docker login (login dans docker hub)
         docker images (pour trouver l'id de mon image)
         docker tag 90fa3f50cef8 vicboni123/tp2 (tag mon appli docker vers son id docker hub)
         docker push vicboni123/tp2 (push mon appli vers docker hub)
25df2af11ea8
## 1.7
answer:
command: docker rmi -f XXXXXXX (id de l'image)
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp -e ENVIRONMENT=python:3-alpine vicboni123/tp2
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp -e ENVIRONMENT=python:3-alpine -d vicboni123/tp2
6b1c576fe718d692a8197a90713e24a8eab94e12f76ff57637fd902279c44275

## 1.8
answer:
command: docker ps (nom de mon container: my-running-app, id: 6b1c576fe718)
command: docker rename 6b1c576fe718 new-name restart new-name

## 1.9
answer: docker exec -it 6b1c576fe718 cat /etc/*release
answer: NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.8.1
PRETTY_NAME="Alpine Linux v3.8"
HOME_URL="http://alpinelinux.org"
BUG_REPORT_URL="http://bugs.alpinelinux.org"


docker build -t my-app-front ./
docker run -it --rm --name my-running-app -p 8181:8181/tcp -e APP_PORT=8181 -e WS_BACK_URL=172.17.0.1 -e ENVIRONMENT=python:3-alpine -d vicboni123/tp2.front

## 1.11
command:

## 2.1
command:

## 2.6
command:
command:
