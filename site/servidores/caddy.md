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

    file_server
}
```

## Comandos de Serviço

Depois de alterar o Caddyfile, recarregue sem derrubar o servidor:

```bash
sudo systemctl reload caddy
```

Parar o servidor:
```bash
sudo systemctl stop caddy
```

## Logs

Para ver o que está acontecendo (erros, acessos):

```bash
journalctl -u caddy -f
```

## Proxy Reverso (Exemplo)

Caddy é excelente para colocar HTTPS na frente de aplicações Node/Python/Go rodando em portas locais (ex: 3000).

```text
meudominio.com {
    reverse_proxy 127.0.0.1:3000
}
```
O certificado HTTPS será gerado e renovado automaticamente!

