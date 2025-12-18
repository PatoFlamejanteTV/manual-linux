# Docker

Docker é uma plataforma aberta para desenvolvimento, envio e execução de
aplicativos. O Docker permite separar seus aplicativos de sua infraestrutura
para que você possa entregar software rapidamente.

Com o Docker, você pode gerenciar sua infraestrutura da mesma forma que gerencia
seus aplicativos.

## Comandos Básicos

Verificar a versão do Docker:

```bash
$ docker --version
```

Rodar um container "Hello World":

```bash
$ docker run hello-world
```

Listar containers em execução:

```bash
$ docker ps
```

Listar todos os containers (incluindo os parados):

```bash
$ docker ps -a
```

Listar imagens locais:

```bash
$ docker images
```

Baixar uma imagem do Docker Hub:

```bash
$ docker pull ubuntu
```
