# Interfaces de Armazenamento

Além dos discos em si (HDs e SSDs), é importante entender as interfaces que os conectam ao sistema.

## SATA (Serial ATA)

Tradicionalmente usado para HDs e SSDs de 2.5". No Linux, dispositivos SATA geralmente aparecem como `/dev/sdX`.

```bash
lsscsi
```

## NVMe (Non-Volatile Memory Express)

Interface moderna que conecta SSDs diretamente ao barramento PCIe, oferecendo latência muito menor. Dispositivos aparecem como `/dev/nvme0n1`.

Para ver detalhes específicos de drives NVMe:

```bash
# Requer pacote nvme-cli
$ sudo nvme list
$ sudo nvme smart-log /dev/nvme0
```

## USB (Armazenamento Externo)

Pen drives e HDs externos. O comando `lsusb -t` pode mostrar a árvore de dispositivos e a velocidade negociada (480M, 5000M, etc.), indicando se está operando em USB 2.0 ou 3.0+.
