# Logs

Gerenciar logs é essencial para entender o que acontece no sistema.

## Syslog

O protocolo padrão de log em sistemas Unix/Linux. Muitos programas enviam suas
mensagens para o _daemon_ de syslog (como `rsyslog` ou `syslog-ng`), que as
grava em arquivos como `/var/log/syslog` ou `/var/log/auth.log`.

## Systemd Journal

Distribuições com `systemd` usam o `journald` para coletar e armazenar logs. Ele
captura logs do kernel, mensagens de inicialização, saída padrão de serviços,
etc.

Para ler os logs:

```bash
# Ver todos os logs
journalctl

# Ver logs de um serviço específico
journalctl -u nginx

# Ver logs em tempo real (follow)
journalctl -f
```
