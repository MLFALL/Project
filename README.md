## Partie A : Création d'un Serveur HTTP Minimaliste avec Docker : (9pts) 

# Serveur HTTP Minimaliste avec Docker

Ce projet met en place un serveur HTTP minimaliste en utilisant Python et Docker. Il est conçu pour aider à comprendre les bases de Docker et la création d'un serveur HTTP simple sans framework.

## Structure du projet

basic-docker-project/
├── app/
│ ├── server.py
├── Dockerfile
├── docker-compose.yml
└── README.md


- `app/server.py` : Contient le code du serveur HTTP.
- `Dockerfile` : Fichier de configuration pour construire l'image Docker.
- `docker-compose.yml` : Fichier pour orchestrer le déploiement avec Docker Compose.
- `README.md` : Documentation du projet.

## Prérequis
- Docker installé
- Docker Compose installé

## Instructions


### 1. Sans Docker Compose
1. Construire l'image Docker :
    docker build -t simple-http-server .
2. Exécuter le conteneur :
    docker run -p 8000:8000 simple-http-server
3. Allez vers le navigateur
    http://localhost:8000
### 2. Avec Docker Compose
1. Exécuter le conteneur :
    docker-compose up
2. Allez vers le navigateur
    http://localhost:8000

///////////////////////////////////////////////////////////////////////////////


## Partie B : Pousser l’image de l’application vers DockerHub : (9pts)
1. Construire l'image Docker
    docker build -t simple-http-server .
2. Se connecter à DockerHub
    docker login
3. Tagger l'image
    docker tag simple-http-server lamina26/simple-http-server:latest
4. Pousser l'image sur DockerHub
    docker push lamina26/simple-http-server:latest
5. Télécharger l'image depuis DockerHub
    docker pull lamina26/simple-http-server:latest

    #                        *****Utiles*****
    #            #  Arrêter le conteneur (sans Docker Compose) :
                            docker stop "container_id"
    #             #  Supprimer un conteneur :
                            docker rm "container_id"
    #             #  Arrêter et supprimer les conteneurs (avec Docker Compose) :
                            docker-compose down