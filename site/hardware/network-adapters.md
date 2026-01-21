# Adaptadores de Rede (Network Adapters)

Adaptadores de rede permitem que o computador se comunique com outras máquinas. Isso inclui placas Ethernet (com fio) e placas Wi-Fi (sem fio).

## Listando Dispositivos

Para ver o hardware físico de rede (controladores PCI/USB):

```bash
lspci | grep -i network
lspci | grep -i ethernet
```

Para adaptadores USB:

```bash
lsusb
```

## Informações e Configuração

Para ver as interfaces de rede lógicas criadas pelo kernel:

```bash
ip link show
```

Para detalhes técnicos avançados (velocidade suportada, modo duplex, wake-on-lan) de uma interface cabeada:

```bash
sudo ethtool eth0
```

*(Substitua `eth0` pelo nome da sua interface)*

## Wi-Fi

Para interfaces wireless, o comando `iw` é frequentemente usado:

```bash
iw dev
```
