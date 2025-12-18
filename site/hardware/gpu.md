# GPU (Placa de Vídeo)

A GPU (Unidade de Processamento Gráfico) é responsável por renderizar imagens,
vídeos e jogos. No Linux, o suporte a drivers pode variar entre fabricantes
(NVIDIA, AMD, Intel).

## Identificando sua GPU

Para saber qual placa de vídeo você tem, use o comando `lspci` procurando por
"VGA" ou "3D":

```bash
$ lspci | grep -i vga
```

## Drivers

- **Intel/AMD:** Geralmente possuem drivers de código aberto que já vêm no
  Kernel Linux (Mesa). Funcionam "out of the box".
- **NVIDIA:** Possui drivers proprietários que geralmente oferecem melhor
  desempenho para jogos, mas drivers de código aberto (Nouveau) também existem
  (embora mais lentos).

## Monitoramento

Para ver o uso da GPU (se for NVIDIA e tiver drivers proprietários):

```bash
$ nvidia-smi
```

Para AMD/Intel, ferramentas como `radeontop` ou `intel_gpu_top` podem ser
usadas.
