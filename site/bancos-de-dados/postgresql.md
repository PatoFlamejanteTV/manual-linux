# PostgreSQL

O **PostgreSQL** (ou Postgres) é um sistema de gerenciamento de banco de dados
objeto-relacional poderoso e de código aberto. Ele é conhecido por sua
confiabilidade, robustez e performance.

Muitas empresas e projetos utilizam o PostgreSQL por sua conformidade com os
padrões SQL e recursos avançados.

## Instalação

No Debian, Ubuntu e derivados:

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
o serviço.

Em sistemas baseados em RHEL/Fedora:

```bash
sudo postgresql-setup --initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

No Arch Linux:

```bash
sudo -u postgres initdb -D /var/lib/postgres/data
```

## Comandos Básicos

O Postgres cria um usuário de sistema chamado `postgres` por padrão.

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
