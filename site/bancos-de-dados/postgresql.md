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

No Fedora:

```bash
sudo dnf install postgresql-server postgresql-contrib
```

## Inicialização (Fedora/CentOS)

Em sistemas baseados em RHEL/Fedora, você precisa inicializar o banco de dados
antes de iniciar o serviço:

```bash
sudo postgresql-setup --initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

## Acessando o PostgreSQL

O Postgres cria um usuário de sistema chamado `postgres`. Para acessar o
console:

```bash
sudo -u postgres psql
```
