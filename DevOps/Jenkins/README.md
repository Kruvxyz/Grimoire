
# Installation
## Build the Jenkins BlueOcean Docker Image (or pull and use the one I built)
```
docker build -t myjenkins-blueocean:2.414.2 .

#IF you are having problems building the image yourself, you can pull from my registry (It is version 2.332.3-1 though, the original from the video)

docker pull devopsjourney1/jenkins-blueocean:2.332.3-1 && docker tag devopsjourney1/jenkins-blueocean:2.332.3-1 myjenkins-blueocean:2.332.3-1
```

## Create the network 'jenkins'
```
docker network create jenkins
```

## Run the Container
### MacOS / Linux
```
docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.414.2
```

### Windows
```
docker run --name jenkins-blueocean --restart=on-failure --detach `
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
  --volume jenkins-data:/var/jenkins_home `
  --volume jenkins-docker-certs:/certs/client:ro `
  --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.414.2
```


## Get the Password
```
docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```

## Connect to the Jenkins
```
https://localhost:8080/
```

## Installation Reference:
https://www.jenkins.io/doc/book/installing/docker/


## alpine/socat container to forward traffic from Jenkins to Docker Desktop on Host Machine

https://stackoverflow.com/questions/47709208/how-to-find-docker-host-uri-to-be-used-in-jenkins-docker-plugin
```
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
docker inspect <container_id> | grep IPAddress
```

# Nodes
```
pipeline {
    agent {
        label 'NODE_NAME'
    }
    ...
}
```

## Jenkins add known host
```
docker exec -it <jenkins-container-id> bash
```

BASH
```
ssh-keyscan -H <ec2-public-ip-or-hostname> >> /var/jenkins_home/.ssh/known_hosts
chmod 700 /var/jenkins_home/.ssh
chmod 644 /var/jenkins_home/.ssh/known_hosts
```

## EC2
https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/#creating-a-key-pair

### Install Java on EC2 instance
AMAZON LINUX
```
sudo rpm --import https://yum.corretto.aws/corretto.key
sudo curl -L -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo
sudo yum install -y java-11-amazon-corretto-devel
java -version
```

### Install EC2 amazon plugin on jenkins

### Define node
Manage Jenins --> Nodes --> + New Node --> NODE_NAME (makr Permanent Agent) --> Remote root directory: EC2 instance IP 
--> Credintials --> Add --> Jenkins --> SSH username and private key --> username: ec2-user (aws linux) / password: from .pem file.
### EC2 Credentials


# GITHUB
Go to github.com --> Profile --> settings --> developers settings --> Personal access tokens --> Tokens (classic) 
--> Generate new token --> New personal access token (classic) --> Select scope, mark repo boxes --> Generate token 
--> copy token

## jenkins credential
Username : github username
password: token

## jenkins pipeline
```
pipeline {
    agent {
        label 'p8d.kruv.xyz'
    }
    environment {
        GITHUB_REPO = GITHUB_REPO
        GIT_CREDENTIALS_ID = 'Kruvxyz' // Your Jenkins credential ID for PAT
    }
    ...
}
```