# Utiliser une image de base Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier server.py dans le conteneur
COPY app/server.py .

# Exposer le port 8000
EXPOSE 8000

# Commande pour exécuter le serveur
CMD ["python", "server.py"]