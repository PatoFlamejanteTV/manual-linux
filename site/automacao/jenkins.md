# Jenkins

Jenkins é um servidor de automação open source.

## Instalação (Ubuntu/Debian)

Requer Java.

```bash
sudo apt install openjdk-11-jdk
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins
```

## Acesso inicial

Acesse `http://localhost:8080`.
A senha inicial está em:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
