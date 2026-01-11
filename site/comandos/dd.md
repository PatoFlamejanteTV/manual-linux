# dd

O **dd** é usado para converter e copiar arquivos, sendo muito utilizado para criar pendrives bootáveis ou backups de disco.

## Criar pendrive bootável

Cuidado! Isso apaga o destino.

```bash
sudo dd if=linux.iso of=/dev/sdX bs=4M status=progress
```

## Backup de MBR

```bash
sudo dd if=/dev/sda of=mbr_backup.img bs=512 count=1
```
