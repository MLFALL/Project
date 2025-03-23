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

## Partie C : Automatisation du Push de l’Image vers DockerHub (2pts)

# Prérequis
1. Un compte GitHub pour héberger votre projet.
2. Un compte DockerHub pour stocker l'image Docker.

# Instructions

1. Créez un token avec les permissions nécessaires pour pousser des images.

      ==> Au niveau du DockerHub,  "Account Settings" > "Security" > "Personal Access Token", pour générer a new token


2. Ajoutez deux secrets :DOCKER_HUB_USERNAME et DOCKER_HUB_TOKEN

      ==> Création d'un dépot GitHub, ensuite au niveau de notre repository on y va sur "settings" et puis sur secrets et variables/Actions  pour coller et enregistrer les codes des variables créer dans  le DockerHub

3. Création au niveau de la racine du projet un répertoire .github/workflows/docker-build-push.yml et on ajoute le contenu du workflows

   #             le Contenu se resume ainsi
    ==> Déclencheur : Le pipeline est déclenché à chaque push sur la branche main.

    ==> Checkout du code : Récupère le code du dépôt GitHub.

    ==> Connexion à DockerHub : Utilise les secrets GitHub pour se connecter à DockerHub.

    ==> Construction de l'image Docker : Construit l'image à partir du Dockerfile.

    ==> Tagging de l'image : Tagge l'image avec latest et v1.0 (ou une autre convention de versionnement).

    ==> Push de l'image : Pousse l'image vers DockerHub.

    #               Pour tester, on fait:
       ==> git init
       ==> git add .
       ==> git commit -m "Ajout du pipeline CI/CD"
       ==> git remote add origin https://github.com/MLFALL/Project.git
       ==> git push origin main

    #               Vérifier l'exécution du pipeline :

    ==> Allez dans l'onglet "Actions" de votre dépôt GitHub.

    ==> Vous devriez voir le workflow en cours d'exécution.

    ==> Vérifier l'image sur DockerHub :

    ==> Une fois le workflow terminé, allez sur DockerHub et vérifiez que l'image a bien été poussée..