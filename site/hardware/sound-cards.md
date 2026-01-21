# Placas de Som (Sound Cards)

Dispositivos de áudio podem ser integrados à placa-mãe, placas dedicadas (PCIe) ou interfaces externas USB (DACs).

## Listando Dispositivos de Áudio

Para ver os dispositivos detectados pelo ALSA (Advanced Linux Sound Architecture):

```bash
aplay -l
```

Para ver o hardware no barramento PCI:

```bash
lspci | grep -i audio
```

## Mixers e Servidores de Som

Acima do driver de hardware (ALSA), geralmente roda um servidor de som como PulseAudio ou PipeWire.

Para controlar volumes via terminal, o `alsamixer` é uma ferramenta visual baseada em texto muito útil:

```bash
alsamixer
```

Pressione `F6` para selecionar entre diferentes placas de som se você tiver mais de uma.
