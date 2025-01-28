# Exercice 1 : Premiers pas avec Docker

Dans cet exercice, vous allez apprendre à utiliser des commandes Docker de base pour lancer et interagir avec des conteneurs.

## Objectifs

- Lancer un conteneur "Hello World".
- Démarrer un conteneur Ubuntu en mode interactif.
- Lancer une application Flask en utilisant Docker.

---

## Étapes

### 1. Lancer un conteneur "Hello World"

1. Exécutez la commande suivante :
   `docker run hello-world`
2. Observez le message affiché dans votre terminal.

---

### 2. Démarrer un conteneur Ubuntu

1. Lancez un conteneur Ubuntu en mode interactif :
   `docker run -it ubuntu`
2. Une fois dans le conteneur :
   - Mettez à jour les paquets :
     `apt-get update`
   - Testez quelques commandes Linux simples :
     `echo "Hello from Docker!"`
     `ls`
     `pwd`
3. Quittez le conteneur avec la commande :
   `exit`

---

### 3. Lancer une application Flask

1. Lancez une application Flask en utilisant une image existante :
   `docker run -d -p 5000:5000 tiangolo/hello-world`
2. Ouvrez votre navigateur et rendez-vous sur [http://localhost:5000](http://localhost:5000).
3. Pour arrêter le conteneur :
   - Trouvez son ID avec :
     `docker ps`
   - Arrêtez-le :
     `docker stop <container_id>`

---

## Résumé des commandes utilisées

- `docker run` : Lancer un conteneur.
- `docker ps` : Lister les conteneurs en cours d'exécution.
- `docker stop` : Arrêter un conteneur.
