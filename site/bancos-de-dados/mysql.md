# MySQL

O **MySQL** é um dos sistemas de gerenciamento de banco de dados relacional mais
populares do mundo. Ele é amplamente utilizado em aplicações web, sendo a base
de dados padrão para softwares como WordPress, Drupal e Joomla.

É conhecido por ser rápido, confiável e fácil de usar.

## Instalação

No Debian, Ubuntu e derivados:

```bash
sudo apt update
sudo apt install mysql-server
```

No Fedora e derivados:

```bash
sudo dnf install mysql-server
```

## Configuração Inicial

Após a instalação, é recomendável rodar o script de segurança para definir a
senha de root e remover configurações inseguras:

```bash
sudo mysql_secure_installation
```

## Acessando o MySQL

Para acessar o console do MySQL:

```bash
sudo mysql -u root -p
```
