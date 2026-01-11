# MySQL

O **MySQL** é um dos sistemas de gerenciamento de banco de dados relacional mais
populares do mundo. Ele é amplamente utilizado em aplicações web, sendo a base
de dados padrão para softwares como WordPress, Drupal e Joomla.

É conhecido por ser rápido, confiável e fácil de usar. Frequentemente, em
distribuições Linux, o MariaDB é usado como um substituto direto e de código
aberto para o MySQL.

## Instalação

No Debian, Ubuntu e derivados:

```bash
sudo apt update
sudo apt install mysql-server
# ou default-mysql-server
```

No Arch Linux:

```bash
sudo pacman -S mariadb
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

## Comandos Básicos

Acessar o shell do banco de dados:

```bash
sudo mysql -u root -p
```

### Dentro do shell SQL

Listar bancos de dados:

```sql
SHOW DATABASES;
```

Criar um banco de dados:

```sql
CREATE DATABASE meu_banco;
```

Criar um usuário:

```sql
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'senha_forte';
```

Conceder permissões:

```sql
GRANT ALL PRIVILEGES ON meu_banco.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
```

Sair do shell:

```sql
EXIT;
```

## Backup e Restauração

### Fazer Backup (Dump)

Para fazer backup de um banco específico para um arquivo SQL:

```bash
mysqldump -u root -p meu_banco > backup_meu_banco.sql
```

Para todos os bancos:

```bash
mysqldump -u root -p --all-databases > backup_completo.sql
```

### Restaurar Backup

```bash
mysql -u root -p meu_banco < backup_meu_banco.sql
```

