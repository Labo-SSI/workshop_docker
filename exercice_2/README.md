# Exercice 2 : Créez votre propre image Docker

Dans cet exercice, vous allez apprendre à créer une image Docker personnalisée en écrivant un `Dockerfile`.

## Objectifs

- Comprendre la structure d’un `Dockerfile`.
- Construire une image Docker.
- Exécuter un conteneur basé sur cette image.

---

## Étapes

### 1. Écrire un Dockerfile

1. Créez un fichier nommé `Dockerfile` dans ce répertoire.
2. Ajoutez le contenu suivant :

   ```Dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY app.py /app
   RUN pip install flask
   CMD ["python", "app.py"]
   ```

3. **Explications** :

- `FROM` : Utilise une image de base Python légère.
- `WORKDIR` : Définit le répertoire de travail.
- `COPY` : Copie le fichier `app.py` dans le conteneur.
- `RUN` : Installe Flask.
- `CMD` : Commande pour démarrer l’application.

---

### 2. Construire l’image Docker

1. Dans le terminal, positionnez-vous dans ce répertoire.
2. Exécutez la commande :
   `docker build -t my-flask-app .`
3. **Résultat attendu** :
   - Docker construit une image nommée `my-flask-app`.

---

### 3. Lancer un conteneur basé sur cette image

1. Exécutez la commande suivante :
   `docker run -d -p 5000:5000 my-flask-app`
2. Ouvrez votre navigateur et rendez-vous sur [http://localhost:5000](http://localhost:5000).

---

## Résumé des commandes utilisées

- `docker build` : Construire une image Docker.
- `docker run` : Lancer un conteneur basé sur une image.
