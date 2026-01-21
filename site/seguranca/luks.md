# Criptografia de Disco (LUKS)

O LUKS (Linux Unified Key Setup) é o padrão para criptografia de disco rigido no Linux. Ele protege os dados em repouso caso o dispositivo físico seja roubado.

## Como Funciona

O LUKS opera sobre uma partição, criando um volume lógico desbloqueado que pode ser formatado e montado.

## Criando um Volume Criptografado

1. **Setup inicial** (CUIDADO: Apaga dados):

```bash
sudo cryptsetup luksFormat /dev/sdb1
```

1. **Abrir o volume**:

```bash
sudo cryptsetup luksOpen /dev/sdb1 meu_volume_seguro
```

1. **Formatar**:

```bash
sudo mkfs.ext4 /dev/mapper/meu_volume_seguro
```

1. **Montar**:

```bash
sudo mount /dev/mapper/meu_volume_seguro /mnt/seguro
```

1. **Fechar**:

```bash
sudo umount /mnt/seguro
sudo cryptsetup luksClose meu_volume_seguro
```
