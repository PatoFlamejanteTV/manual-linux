# journalctl

O **journalctl** é usado para consultar e exibir logs do systemd.

## Ver todos os logs

```bash
journalctl
```

## Ver logs do boot atual

```bash
journalctl -b
```

## Acompanhar logs em tempo real (follow)

```bash
journalctl -f
```

## Logs de um serviço específico

journalctl -u nginx
```

## Filtros Avançados

### Logs do Kernel (`-k`)
Ver mensagens de hardware, boot e drivers (similar ao `dmesg`).

```bash
journalctl -k
```

### Por Período (`--since`)

```bash
journalctl --since "1 hour ago"
journalctl --since "2023-01-01 12:00:00"
```

### Por Prioridade (`-p`)
Ver apenas erros (3: err, 4: warning).

```bash
journalctl -p err
```

## Manutenção

Limpar logs antigos para liberar espaço (manter apenas 100MB):

```bash
journalctl --vacuum-size=100M
```

