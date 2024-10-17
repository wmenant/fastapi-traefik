# Dockerizing FastAPI with Postgres, Uvicorn, and Traefik

### Development

Build the images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Test it out:

1. [http://fastapi.localhost:8008/](http://fastapi.localhost:8008/)
1. [http://fastapi.localhost:8081/](http://fastapi.localhost:8081/)

### Production

Update the domain in *docker-compose.prod.yml*, and add your email to *traefik.prod.toml*.

Build the images and run the containers:

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
```
# Deployment with helm
 => Build end push image in exempleImage folder

 => creates the dns records for the different namespaces example: 
  - prod-traefik.exemple-datascientest.cloudns.eu
  - dev-traefik.exemple-datascientest.cloudns.eu

 => change host value in values.yaml lines: 10 (do not remove pull it)(without dev,prod ) example: "-traefik.exemple-datascientest.cloudns.eu"

 => change host value in values.yaml lines: 83 (without dev,prod ) example: "traefik.example-datascientest.cloudns.eu"

 => change image value in values.yaml lines: 15 wiht your repository 

 => enter in file: k3s-dev and run :
 ```sh
 $ kubectl create namespace <your Namespace>
 ```
 ```sh
 - helm install <your ChartName> . --values=values.yaml -n <your Namespace>
 ```
 => to test follow the instructions in terminal or: 

 Service web: http://<your DNS> example: https://dev-traefik.example-datascientest.cloudns.eu
 
 Traefik Dashboard: http://<your DNS>:nodeport  example https://dev-traefik.example-datascientest.cloudns.eu:31740
 


   