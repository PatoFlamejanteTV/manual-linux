# Caddy

Caddy é um servidor web moderno, conhecido por obter certificados SSL/TLS automaticamente via Let's Encrypt.

## Instalação (Debian/Ubuntu)

```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

## Rodar um site estático

Na pasta do site:

```bash
caddy file-server --listen :8080
```

## Caddyfile

O arquivo de configuração padrão fica em `/etc/caddy/Caddyfile`.

```text
meusite.com {
    reverse_proxy localhost:3000
    file_server
}
```
