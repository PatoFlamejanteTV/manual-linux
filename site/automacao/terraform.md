# Terraform

Terraform é uma ferramenta de infraestrutura como código (IaC) de código aberto
que permite criar, alterar e melhorar a infraestrutura de maneira segura e
previsível.

## Instalação

Geralmente requer adicionar o repositório da HashiCorp.

```bash
wget -O- https://apt.releases.hashicorp.com/gpg | \
sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update && sudo apt install terraform
```

## Comandos Básicos

Inicializar um diretório de trabalho:

```bash
terraform init
```

Planejar a execução:

```bash
terraform plan
```

Aplicar as mudanças:

```bash
terraform apply
```
