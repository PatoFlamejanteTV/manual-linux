# Puppet

Puppet é uma ferramenta de gerenciamento de configuração que permite definir o
estado da sua infraestrutura de TI e, em seguida, impor automaticamente esse
estado.

## Instalação

Debian/Ubuntu (Agent):

```bash
sudo apt install puppet
```

## Comandos Básicos

Verificar versão:

```bash
puppet --version
```

Aplicar um manifesto:

```bash
sudo puppet apply manifesto.pp
```
