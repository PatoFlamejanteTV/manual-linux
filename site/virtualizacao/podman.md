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

## Gerenciamento de Imagens

```bash
podman pull docker.io/library/alpine
podman images
podman rmi alpine
```

## Pods
Diferente do Docker, o Podman entende o conceito de "Pods" (grupos de containers que compartilham rede), similar ao Kubernetes.

```bash
podman pod create --name meu-pod -p 8080:80
podman run -dt --pod meu-pod nginx
```

## Integração com Systemd
Podman pode gerar arquivos `.service` para seus containers rodarem automaticamente no boot.

```bash
podman generate systemd --name meu-container --files --new
```
Basta mover o arquivo gerado para `~/.config/systemd/user/` e habilitar.

