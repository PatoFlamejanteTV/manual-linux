# ImageMagick

ImageMagick é um conjunto de software gratuito e de código aberto para exibir,
converter e editar arquivos de imagem raster e vetorial. Ele pode ler e gravar
imagens em mais de 200 formatos.

A ferramenta principal é o comando `convert` (ou `magick` em versões mais
recentes).

## Instalação

```bash
# Debian/Ubuntu
sudo apt install imagemagick

# Arch Linux
sudo pacman -S imagemagick
```

## Exemplos de Uso

### Converter formato

Converter uma imagem PNG para JPG:

```bash
convert imagem.png imagem.jpg
```

### Redimensionar imagem

Redimensionar para 50% do tamanho original:

```bash
convert entrada.jpg -resize 50% saida.jpg
```

Redimensionar para uma largura fixa de 800px:

```bash
convert entrada.jpg -resize 800 saida.jpg
```

### Criar um GIF animado

Criar um GIF a partir de várias imagens JPG:

```bash
convert -delay 20 -loop 0 *.jpg animacao.gif
```

- `-delay 20`: Tempo entre quadros (20/100 segundos).
- `-loop 0`: Repetir infinitamente.

### Adicionar texto na imagem

```bash
convert entrada.jpg -gravity center -pointsize 30 \
  -draw "text 0,0 'Ola Mundo'" saida.jpg
```
