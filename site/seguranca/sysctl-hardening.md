# Hardening via Sysctl

O comando `sysctl` permite modificar parâmetros do kernel em tempo de execução. Muitas configurações de rede podem ser ajustadas para aumentar a segurança.

## Arquivo de Configuração

Edite `/etc/sysctl.conf` ou crie um arquivo em `/etc/sysctl.d/`.

## Parâmetros Recomendados

### Desabilitar Roteamento de Pacotes (se não for roteador)

```ini
net.ipv4.ip_forward = 0
```

### Bloquear ICMP Redirects (Mitiga Man-in-the-Middle)

```ini
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
```

### Ignorar Ping de Broadcast

```ini
net.ipv4.icmp_echo_ignore_broadcasts = 1
```

### Proteção contra SYN Flood

```ini
net.ipv4.tcp_syncookies = 1
```

Para aplicar as mudanças:

```bash
sudo sysctl -p
```
