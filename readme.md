# application projet
projet en docker contenant:
du frontend
du backend
une base de donnée
un dockerfile
un docker compose
un readme
un schéma
une documentation autogérée
la sortie c'est des pages web.
# comment build
#todo
# comment run
#todo


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

