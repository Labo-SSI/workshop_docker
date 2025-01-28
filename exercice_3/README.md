# Exercice 3 : Découverte de Docker Compose

Dans cet exercice, vous allez apprendre à orchestrer deux conteneurs grâce à Docker Compose.

## Objectifs

- Créer un fichier `docker-compose.yml`.
- Lancer plusieurs conteneurs qui interagissent.

---

## Étapes

### 1. Structure du projet

Ce répertoire contient :

- `app/` : Répertoire de l’application Flask.
- `db/` : Répertoire contenant un fichier de configuration pour la base de données.

### 2. Écrire un fichier `docker-compose.yml`

1. Créez un fichier `docker-compose.yml` avec le contenu suivant :

   ```yml
   version: "3.9"
   services:
     web:
       build: ./app
       ports:
         - "5000:5000"
       depends_on:
         - db
     db:
       image: postgres:13
       environment:
         POSTGRES_USER: user
         POSTGRES_PASSWORD: password
         POSTGRES_DB: mydb
   ```

2. **Explications** :
   - `web` : Service pour l’application Flask.
   - `db` : Service pour une base de données PostgreSQL.
   - `depends_on` : Assure que le service `web` attend que la base de données soit prête.

---

### 3. Lancer les conteneurs

1. Exécutez la commande suivante :
   `docker-compose up`
2. Une fois les services démarrés :
   - L'application Flask est accessible sur [http://localhost:5000](http://localhost:5000).

3. Pour arrêter les services :
   `docker-compose down`

---

## Résumé des commandes utilisées

- `docker-compose up` : Lancer les services définis dans le fichier `docker-compose.yml`.
- `docker-compose down` : Arrêter et supprimer les conteneurs et réseaux créés.
