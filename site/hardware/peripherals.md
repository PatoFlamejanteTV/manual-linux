# Periféricos (Peripherals)

Periféricos incluem dispositivos de entrada e saída como teclados, mouses, webcams e mesas digitalizadoras. No Linux, o suporte a esses dispositivos está geralmente incluído no kernel.

## Identificação USB

A maioria dos periféricos modernos usa USB. Use `lsusb` para listá-los:

```bash
lsusb
```

A saída mostra o ID do Fabricante (Vendor ID) e o ID do Produto (Product ID), úteis para solucionar problemas de driver.

## Dispositivos de Entrada (Input)

O sistema gerencia entradas através do subsistema `evdev`. Você pode listar dispositivos de entrada com:

```bash
cat /proc/bus/input/devices
```

Ou usando ferramentas como `libinput` para testar eventos de mouse e teclado:

```bash
sudo libinput list-devices
```

## Webcams e Mídia

Para listar câmeras conectadas, verifique os dispositivos de vídeo:

```bash
v4l2-ctl --list-devices
```

*(Requer o pacote `v4l-utils`)*
