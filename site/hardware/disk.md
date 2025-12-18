# Armazenamento (Disco/SSD)

O armazenamento é onde seus arquivos, sistema operacional e programas vivem
permanentemente (até você apagá-los, claro). Diferente da RAM, ele não esquece
as coisas quando você desliga o PC.

## Dispositivos

No Linux, seus discos são representados como arquivos na pasta `/dev`.

- **SATA (HDD/SSD):** Geralmente aparecem como `/dev/sda`, `/dev/sdb`, etc.
- **NVMe (SSDs rápidos):** Aparecem como `/dev/nvme0n1`, etc.

## Partições

Um disco pode ser dividido em pedaços menores chamados partições. Elas ganham
números no final do nome do disco.
Por exemplo, `sda1` é a primeira partição do disco `sda`.

## Comandos Úteis

Para ver os discos e partições conectados:

```bash
$ lsblk
```

Para ver o espaço livre e ocupado:

```bash
$ df -h
```

Para ver o que está ocupando espaço em uma pasta:

```bash
$ du -sh pasta/
```
