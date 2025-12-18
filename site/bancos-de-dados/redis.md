# Redis

O **Redis** é um armazenamento de estrutura de dados em memória, usado como
banco de dados, cache e *message broker*. Ele suporta estruturas de dados como
strings, hashes, listas, conjuntos e muito mais.

É extremamente rápido e é frequentemente usado para melhorar a performance de
aplicações web.

## Instalação

No Debian/Ubuntu:

```bash
sudo apt update
sudo apt install redis-server
```

No Fedora:

```bash
sudo dnf install redis
```

## Configuração

O arquivo de configuração geralmente fica em `/etc/redis/redis.conf`.
Para permitir que o Redis seja usado como um serviço de *systemd*, pode ser
necessário alterar a diretiva `supervised` para `systemd` no arquivo de
configuração.

## Uso Básico

Para acessar a interface de linha de comando do Redis:

```bash
redis-cli
```

Teste se está funcionando com um ping:

```bash
127.0.0.1:6379> ping
PONG
```
