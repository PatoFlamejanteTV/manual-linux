# Ansible

Ansible é uma ferramenta de automação de TI "open source" que automatiza o
provisionamento, o gerenciamento de configurações e a implantação de
aplicativos.

## Instalação

Debian/Ubuntu:

```bash
sudo apt update
sudo apt install ansible
```

## Comandos Básicos

Verificar versão:

```bash
ansible --version
```

Pingar todos os hosts (definidos no inventário):

```bash
ansible all -m ping
```
