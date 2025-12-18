# Devices (Dispositivos)

No Linux, "tudo é um arquivo". Isso inclui o hardware, como discos rígidos,
mouses e terminais. Esses arquivos especiais residem no diretório `/dev`.

## Tipos de Dispositivos

Existem dois tipos principais de arquivos de dispositivo:

1.  **Character Devices (c)**: Transferem dados caractere por caractere (stream).
    Exemplos: Teclados, mouses, terminais seriais.
2.  **Block Devices (b)**: Transferem dados em blocos de tamanho fixo. Permitem
    acesso aleatório. Exemplos: Discos rígidos, SSDs, pen drives.

## Major e Minor Numbers

Em vez de tamanho, dispositivos têm números identificadores:

*   **Major Number**: Identifica o driver associado ao dispositivo.
*   **Minor Number**: Identifica o dispositivo específico controlado por aquele
    driver.

Você pode vê-los com `ls -l` em `/dev`:

```bash
$ ls -l /dev/sda
brw-rw---- 1 root disk 8, 0 Jan 1 10:00 /dev/sda
```

Aqui, `b` indica Block Device, `8` é o Major e `0` é o Minor.
