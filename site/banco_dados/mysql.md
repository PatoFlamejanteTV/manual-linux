# MySQL

O MySQL (e seu fork open source MariaDB) é um dos sistemas de gerenciamento de
banco de dados relacionais (RDBMS) mais populares do mundo. Ele utiliza a
linguagem SQL (Structured Query Language) para manipular e recuperar dados.

## Instalação

No Debian/Ubuntu e derivados:

```bash
sudo apt update
sudo apt install mariadb-server
# ou mysql-server, dependendo da distro
```

No Arch Linux:

```bash
sudo pacman -S mariadb
```

No Fedora:

```bash
sudo dnf install mariadb-server
```

## Configuração Inicial

Após a instalação, é recomendável rodar o script de segurança para definir a
senha de root e remover configurações inseguras padrão:

```bash
sudo mysql_secure_installation
```

## Comandos Básicos

Acessar o shell do banco de dados:

```bash
sudo mariadb -u root -p
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
