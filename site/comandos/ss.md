# ss

O **ss** é um utilitário para investigar sockets. Ele permite ver informações sobre conexões de rede e é mais rápido que o `netstat`.

## Listar conexões TCP

```bash
ss -t
```

## Listar conexões escutando (listening)

```bash
ss -lt
```

## Mostrar processos usando sockets

```bash
sudo ss -ltp
```
