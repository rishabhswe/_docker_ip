# _docker_ip

- Build docker image
```
 sudo docker build -t flask-app .
```

- Run docker image as a container (using 1. -d aka detached mode aka temrinal won't be blocked 2. -p aka port forwarding)
```
sudo docker run -d -p 3000:3000 flask-app
```
