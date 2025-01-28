# Workshop : Introduction à Docker et Docker Compose  

Bienvenue dans ce workshop dédié à Docker et Docker Compose. Ce guide est conçu pour les débutants souhaitant découvrir les bases de Docker, apprendre à manipuler des conteneurs et créer des environnements simples grâce à Docker Compose.  

## Objectifs du Workshop  

- Comprendre les concepts fondamentaux de Docker.  
- Manipuler des conteneurs et créer des images.  
- Utiliser Docker Compose pour orchestrer plusieurs conteneurs.  
- Réaliser une mini-infrastructure en autonomie.  

---

## Plan du Workshop  

1. **Introduction à Docker (10 min)**  
   - Présentation de Docker : histoire, utilité, concepts clés.  
   - Diaporama disponible [ici](https://docs.google.com/presentation/d/14sULM5ChtUo4arMNiQsu1hWhqySLdItSMiULQFIxFMA/edit?usp=sharing).  

2. **Premiers pas avec Docker (20 min)**  
   - Lancer un conteneur depuis Docker Hub.  
   - Explorer les commandes de base (`docker run`, `docker ps`, etc.).  

3. **Créer votre propre image Docker (20 min)**  
   - Rédiger un `Dockerfile`.  
   - Construire et tester une image Docker personnalisée.  

4. **Découverte de Docker Compose (10 min)**  
   - Écrire un fichier `docker-compose.yml`.  
   - Orchestrer deux conteneurs qui interagissent.  

5. **Challenge final : Construire une mini-infrastructure (40 min)**  
   - Mettre en pratique les acquis pour créer une infrastructure simple.  

---

## Structure des dossiers  

Chaque exercice est placé dans un dossier nommé `exercice_XX`.  

- **Contenu des dossiers** :  
  Chaque dossier contient :  
  - Un fichier `README.md` détaillant l'exercice à réaliser.  
  - Tous les fichiers nécessaires pour compléter l'exercice (ex. : `Dockerfile`, `docker-compose.yml`, scripts, etc.).  

- **Exemples** :  

```plaintext
exercice_01/
├── README.md  # Instructions pour lancer le hello-world
├── Dockerfile
└── ...

exercice_02/
├── README.md  # Instructions pour lancer une application Flask
├── app.py
├── Dockerfile
└── ...
```

## Pré-requis

### Outils nécessaires

Docker installé sur votre machine (instructions d’installation).

Docker Compose (inclus avec Docker Desktop).

## Ressources utiles

[Documentation officielle de Docker](https://docs.docker.com/)

[Docker Hub](https://hub.docker.com/)

[Guide sur Docker Compose](https://docs.docker.com/compose/gettingstarted/)

## Licence

Ce workshop est publié sous licence MIT. Vous êtes libres de l’utiliser et de le modifier.

Bon courage et amusez-vous bien avec Docker ! 🚀
