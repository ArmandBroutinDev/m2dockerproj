# application projet
projet en docker contenant:
v du frontend
v du backend
une base de donnée
v un dockerfile
un docker compose
v un readme
un schéma
une documentation autogérée
# concept
on a en sortie des pages web avec le front ce dernier fonctionne en flask
le backend utilise fastapi et dans le futur du sqlalchemy pour acceder a une base (probablement en mysql)
l'image sera stockée sur docker-hub
Une quatrième route sera ajoutée et servira d'interface front et back
il y a un docker compose non configuré

# comment build
#todo
# comment run
#todo

# commandes utilisées pour les tests (temporaire)
docker build -t test:01 .
docker run --name test -p 3306:3306 -d test:01

docker stop test
docker rm test
docker rmi test:01

docker build -t back:01 .
docker run --name back -p 3305:3305 -d back:01

docker stop back
docker rm back
docker rmi back:01

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
