A simple python flask webservice to encrypt/decrypt pdf files
git repo: https://github.com/trevynmace/flask_web_pdf_encryption
docker image: https://hub.docker.com/r/trevynmace/flask_web/
docker pull trevynmace/flask_web

GCP service endpoint: http://35.227.178.5:5000
OR
http://trevynmace.com:5000



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



upload to gcr:
docker tag trevynmace/flask_web gcr.io/<projectId>/flask_web:latest
docker push gcr.io/<projectId goes here>/flask_web:latest



gcp:
gcloud components install kubectl
gcloud auth configure-docker
gcloud container clusters create flask-web --num-nodes=3
#3 hours later...
gcloud compute instances list

kubectl run <kubernetes cluster name> --image=trevynmace/flask_web:latest --port 5000
OR
kubectl run <kubernetes cluster name> --image=gcr.io/<projectId>/flask_web:latest --port 5000

kubectl get pods
kubectl expose deployment <kubernetes cluster name> --type=LoadBalancer --port 5000 --target-port 5000

#then to get the external ip of the service
kubectl get service

#to update the service running on the cluster
docker build, docker tag,
kubtctl set image deployment/flask-web flask-web=<image location>:<tag>







