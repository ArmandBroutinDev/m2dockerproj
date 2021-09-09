# application projet
projet en docker contenant:</br>
v du frontend</br>
v du backend</br>
une base de donnée</br>
v un dockerfile</br>
un docker compose</br>
v un readme</br>
un schéma</br>
une documentation autogérée</br>
# concept
Mon objectif est de produire une version augmentée du site portfolio avec des données stockées dans une base de données pour montrer mes compétences.</br>
on a en sortie des pages web avec le front ce dernier fonctionne en flask</br>
le backend utilise fastapi et dans le futur du sqlalchemy pour acceder a une base (probablement en mysql)</br>
l'image sera stockée sur docker-hub</br>
Une quatrième route sera ajoutée et servira d'interface front et back</br>
il y a un docker compose non configuré</br>

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
docker build -t test:01 .</br>
docker run --name test -p 3306:3306 -d test:01</br>
</br>
docker stop test</br>
docker rm test</br>
docker rmi test:01</br>
</br>
docker build -t back:01 .</br>
docker run --name back -p 3305:3305 -d back:01</br>
</br>
docker stop back</br>
docker rm back</br>
docker rmi back:01</br>
