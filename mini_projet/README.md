# Challenge Docker - Mini-infrastructure PHP/MySQL

## Objectifs

Dans ce challenge, vous allez créer une mini-infrastructure avec Docker et Docker Compose, comprenant une application PHP interagissant avec une base de données MySQL. Vous devrez configurer un serveur web PHP et une base de données MySQL à l'aide de conteneurs Docker.

### Étapes du challenge

1. **Docker Compose** : Créez un fichier `docker-compose.yml` pour orchestrer deux services : un service web PHP et un service MySQL.
2. **Dockerfile** : Créez un fichier `Dockerfile` pour construire l'image PHP, contenant une application qui se connecte à la base de données MySQL.
3. **Base de données** : Utilisez MySQL comme base de données et initialisez-la avec une table `users`.
4. **Connexion PHP-MySQL** : L'application PHP doit pouvoir récupérer les utilisateurs depuis la base de données MySQL et les afficher dans une page HTML.

### Structure du projet

L'arborescence du projet est la suivante :

```text
.
├── db # Contient le fichier d'initialisation de la base de données
├── docker-compose.yml # Fichier pour orchestrer les services
└── web # Contient l'application PHP
    ├── Dockerfile # Fichier pour construire l'image PHP
    └── src
       ├── config.php # Configuration de la base de données
       └── index.php # Application PHP qui affiche les utilisateurs
```

### Commandes utiles

1. **Construire et démarrer les services** :
   Exécutez la commande suivante pour démarrer tous les services définis dans `docker-compose.yml` :

   `docker-compose up --build`

2. **Accéder à l'application** :
   L'application PHP sera accessible à l'adresse suivante :
   [http://localhost:8080](http://localhost:8080)

   Vous devriez voir une page avec les utilisateurs récupérés de la base de données MySQL.

3. **Arrêter et nettoyer les services** :
   Une fois l'exercice terminé, vous pouvez arrêter et supprimer les conteneurs et réseaux créés avec la commande :

   `docker-compose down`

### Résultats attendus

L'application PHP doit afficher une liste d'utilisateurs provenant de la base de données MySQL. Si l'application fonctionne correctement, vous devriez voir une page affichant les informations suivantes :

- ID, nom et email de chaque utilisateur.
  
Bonne chance !
