# Answers

Nom:    BONIFACIO
Prénom: VICTOR
NB:     2

## 1.3
command:
        docker build -t my-app-python ./
        docker run -it --rm --name my-running-app my-app-python

## 1.4
answer: Les ports ne sont pas ouverts
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp my-app-python

## 1.5
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp -e ENVIRONMENT=python:3-alpine my-app-python

## 1.6
answer: Le nom de l'image ne correspond pas au repo du docker. Il faut faire un docker tag pour les faire correspondre
command: docker login (login dans docker hub)
         docker images (pour trouver l'id de mon image)
         docker tag 90fa3f50cef8 vicboni123/tp2 (tag mon appli docker vers son id docker hub)
         docker push vicboni123/tp2 (push mon appli vers docker hub)

## 1.7
answer: L'image n'est pas en local, on doit donc la récupérer via un pull
command: docker rmi -f 25df2af11ea8 (id de l'image)
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp -e ENVIRONMENT=python:3-alpine vicboni123/tp2
command: docker run -it --rm --name my-running-app -p 8080:8080/tcp -e ENVIRONMENT=python:3-alpine -d vicboni123/tp2

## 1.8
answer: nom de mon container: my-running-app, id: 6b1c576fe718
command: docker ps
command: docker rename 6b1c576fe718 new-name restart new-name

## 1.9
answer: docker exec -it 6b1c576fe718 cat /etc/*release
answer: NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.8.1
PRETTY_NAME="Alpine Linux v3.8"
HOME_URL="http://alpinelinux.org"
BUG_REPORT_URL="http://bugs.alpinelinux.org"

## 1.11
command: docker run -it --rm -p 8081:8081 -e APP_PORT=8081 -e WS_BACK_URL=172.20.10.3 vicboni123/tp2.front

answer: You called at : 2018-11-12 21:05:34.422443 (dynamic) On environment : python:3-alpine (from env variable) With path : test1 (from URL path) With front : f44t234f4545 (from real hostname of front service) With back : 324gfg664523 (from real hostname of back service)

command: docker exec -it 65437t9rr544 bash

## 2.1
command: docker-compose up

## 2.6
command: docker-compose up -d
command: docker-compose logs

## 2.9
command: docker-compose up -d --scale service-back=2
