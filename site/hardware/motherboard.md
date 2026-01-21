# Placa-mãe (Motherboard)

A placa-mãe é o componente principal que conecta todas as partes do computador. No Linux, você pode obter informações detalhadas sobre a placa-mãe, como fabricante, modelo e versão da BIOS, usando ferramentas de linha de comando.

## Identificação via DMI

O comando `dmidecode` é a ferramenta padrão para extrair informações da tabela DMI (Desktop Management Interface).

```bash
# Necessita de permissões de root/sudo
$ sudo dmidecode -t baseboard
```

## Arquivos do Sistema

Também é possível ler informações diretamente do sistema de arquivos virtual `/sys`:

```bash
cat /sys/class/dmi/id/board_vendor
cat /sys/class/dmi/id/board_name
cat /sys/class/dmi/id/board_version
```

Essas informações são úteis para identificar drivers corretos e verificar compatibilidade de atualizações de firmware.
