A simple python flask webservice to encrypt/decrypt pdf files
git repo: https://github.com/trevynmace/flask_web_pdf_encryption
docker image: https://hub.docker.com/r/trevynmace/flask_web/
docker pull trevynmace/flask_web 



FROM python:3.7-alpine (smaller filesize than python:3.7 or ubuntu [obviously])

docker build -t flask_web:latest .
docker run -p 5000:5000 flask_web
docker container ls
docker stop <containerId here>

docker ps

docker save -o <output path> flask_web

docker commit <containerId> flask_web
docker tag flask_web <repo url>
docker push <repo url>

docker cloud upload:
docker login
docker tag <image> $DOCKER_ID_USER/flask_web
docker push $DOCKER_ID_USER/flask_web



gcp:
gcloud components install kubectl
gcloud auth configure-docker
gcloud container clusters create flask-web --num-nodes=3
#3 hours later...
gcloud compute instances list
