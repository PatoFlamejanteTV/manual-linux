# Portas e Barramentos (Ports & Buses)

Os barramentos são os "caminhos" por onde os dados trafegam entre componentes.

## PCI Express (PCIe)

O principal barramento de alta velocidade para GPUs, NVMe e placas de expansão.

```bash
lspci -vv
```

A opção `-vv` mostra detalhes como a largura da banda (x1, x4, x16) e a velocidade do link.

## USB (Universal Serial Bus)

Para listar a hierarquia e velocidade dos barramentos USB:

```bash
lsusb -t
```

Isso é útil para depurar se um dispositivo USB 3.0 está conectado incorretamente em uma porta 2.0 ou se há gargalos em hubs.

## Thunderbolt / USB4

Dispositivos Thunderbolt podem ser gerenciados e autorizados no Linux via `boltctl` (parte do daemon boltd).

```bash
boltctl list
```
