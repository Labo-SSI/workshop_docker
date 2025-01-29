# Utiliser l'image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY . /app

RUN apt update -y && apt install -y gcc libpq-dev

# Installer les dépendances Python nécessaires
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application Flask sera accessible
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]
