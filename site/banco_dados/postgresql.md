# PostgreSQL

PostgreSQL (frequentemente chamado apenas de Postgres) é um sistema de
gerenciamento de banco de dados relacional e objeto-relacional avançado e de
código aberto. É conhecido por sua confiabilidade, integridade de dados e
robustez.

## Instalação

No Debian/Ubuntu e derivados:

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

No Arch Linux:

```bash
sudo pacman -S postgresql
```

No Fedora:

```bash
sudo dnf install postgresql-server postgresql-contrib
```

## Inicialização

Algumas distros exigem inicializar o cluster de banco de dados antes de iniciar
o serviço:

```bash
# Arch Linux e Fedora
sudo postgresql-setup --initdb
# Ou
sudo -u postgres initdb -D /var/lib/postgres/data
```

## Comandos Básicos

O PostgreSQL cria um usuário de sistema chamado `postgres` por padrão.

Acessar o shell do Postgres (`psql`):

```bash
sudo -u postgres psql
```

### Dentro do shell psql

Listar bancos de dados:

```sql
\l
```

Conectar a um banco de dados:

```sql
\c nome_do_banco
```

Listar tabelas:

```sql
\dt
```

Criar um banco de dados:

```sql
CREATE DATABASE meu_app;
```

Criar um usuário:

```sql
CREATE USER meu_usuario WITH PASSWORD 'minha_senha';
```

Sair do shell:

```sql
\q
```
