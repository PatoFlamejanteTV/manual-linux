# Fail2Ban

Fail2Ban examina arquivos de log e bane IPs que mostram sinais maliciosos, como muitas falhas de senha.

## Instalação

```bash
sudo apt install fail2ban
```

## Configuração

O arquivo principal é `/etc/fail2ban/jail.conf`, mas deve-se criar uma cópia local `/etc/fail2ban/jail.local` para edições.

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

## Habilitar proteção SSH

No arquivo `jail.local`:

```ini
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
```

## Reiniciar serviço

```bash
sudo systemctl restart fail2ban
```
