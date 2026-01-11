# Podman

Podman é uma engine de containers sem daemon, compatível com Docker.

## Instalação

```bash
sudo apt install podman
```

## Diferenças do Docker

- Não precisa de root (Rootless).
- Não tem daemon rodando em background.
- Comandos são quase idênticos (`alias docker=podman`).

## Rodar um container

```bash
podman run -it alpine sh
```
