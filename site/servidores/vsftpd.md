# VSFTPD (Very Secure FTP Daemon)

VSFTPD é um servidor FTP seguro e rápido.

## Instalação

```bash
sudo apt install vsftpd
```

## Configuração

Arquivo: `/etc/vsftpd.conf`.

Habilitar upload:

```text
write_enable=YES
```

Habilitar usuários locais:

```text
local_enable=YES
```

## Reiniciar

```bash
sudo systemctl restart vsftpd
```
