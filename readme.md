
# application projet

projet en docker contenant:  
- du frontend
- du backend
- une base de donnée
- un dockerfile
- un docker compose
- un readme
- un schéma
- une documentation autogérée

# concept

Mon objectif est de produire une version augmentée du site portfolio avec des données stockées dans une base de données pour montrer mes compétences.

on a en sortie des pages web avec le front ce dernier fonctionne en flask.

le backend utilise fastapi et dans le futur du sqlalchemy pour acceder a une base (probablement en mysql)

l'image sera stockée sur docker-hub

Une quatrième route sera ajoutée et servira d'interface front et back

il y a un docker compose non configuré

# comment build

#todo

# comment run

#todo

# forme du projet


    _____________________________________________________
    |                     projet                        |
    |___________________________________________________|
    |-docker-compose.yml                                |
    |-readme.md                                         |
    |+front                                             |
    |+back                                              |
    |_________________________________|_________________|
    |              front              |       back      |
    |_________________________________|_________________|
    |-Dockerfile                      |-Dockerfile      |
    |-requirements.txt                |-requirements.txt|
    |-app.py                          |-main.py         |
    |+templates                       |-database.db     |
    |+static/styles                   |_________________|
    |_________________|_______________|
    |    templates    | static/styles |
    |_________________|_______________|
    |-welcome.html    |-style.css     |
    |-about.html      |_______________|
    |-contact.html    |
    |-database.html   |
    |_________________|


# schema

![Untitled Diagram drawio](https://user-images.githubusercontent.com/71330618/132662822-e2f2e217-eff7-4743-82e3-369d5531765a.png)


# commandes utilisées pour les tests (temporaire)


    docker build -t front:01 .
    docker run --name front -p 3306:3306 -d front:01

    docker stop front
    docker rm front
    docker rmi front:01

    docker build -t back:01 .
    docker run --name back -p 3305:3305 -d back:01

    docker stop back
    docker rm back
    docker rmi back:01
