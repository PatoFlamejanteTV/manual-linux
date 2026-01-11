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

```bash
journalctl -u nginx
```
