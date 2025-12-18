# Nginx

O **Nginx** (fala-se "Engine X") é o queridinho da performance. Ele é leve,
rápido e aguenta o tranco de muito tráfego sem suar a camisa.

Além de servir sites, ele é muito usado como **Proxy Reverso** (recebe os
pedidos e passa pra outro servidor, tipo um Node.js rodando atrás).

## Instalação

Também é super simples de instalar.

No Debian/Ubuntu:

```bash
sudo apt update
sudo apt install nginx
```

No Fedora:

```bash
sudo dnf install nginx
```

## Configuração

Tudo fica em `/etc/nginx/`.

- **`/etc/nginx/nginx.conf`**: Configuração global.
- **`/etc/nginx/sites-available/`**: Configurações de sites específicos (no
  estilo Debian).
- **`/usr/share/nginx/html/`** ou **`/var/www/html/`**: Onde geralmente fica
  a página padrão.

Depois de instalar, acessa `localhost` no navegador. Se ver a mensagem
"Welcome to nginx!", tá tudo em casa.
