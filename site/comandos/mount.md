# mount

O **mount** manualmente anexa um sistema de arquivos à estrutura de diretórios do Linux.

## Montar um dispositivo

Montar a partição `/dev/sdb1` em `/mnt/dados`:

```bash
sudo mount /dev/sdb1 /mnt/dados
```

## Montar ISO

```bash
sudo mount -o loop imagem.iso /mnt/iso
```
