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

No Arch Linux:

```bash
sudo pacman -S redis
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

Iniciar o serviço (se não iniciado automaticamente):

```bash
sudo systemctl start redis
```

Para acessar a interface de linha de comando do Redis:

```bash
redis-cli
```

### Comandos no CLI

Testar conexão (deve responder PONG):

```text
PING
```

Definir um valor para uma chave:

```text
SET minha_chave "Olá Mundo"
```

Obter o valor de uma chave:

```text
GET minha_chave
```

Expirar uma chave após 10 segundos:

```text
EXPIRE minha_chave 10
```

Deletar uma chave:

```text
DEL minha_chave
```
