# mpv

O mpv é um reprodutor de mídia gratuito, de código aberto e multiplataforma.
Ele suporta uma grande variedade de formatos de arquivo de vídeo, áudio e
legendas. É conhecido por seu design minimalista e alta configurabilidade.

## Instalação

```bash
# Debian/Ubuntu
sudo apt install mpv

# Arch Linux
sudo pacman -S mpv
```

## Exemplos de Uso

### Reproduzir um arquivo

```bash
mpv video.mkv
```

### Reproduzir uma URL

O mpv pode reproduzir links do YouTube e outros sites (usando o `yt-dlp` em
segundo plano):

```bash
mpv "URL_DO_VIDEO"
```

### Atalhos de teclado úteis

- `Espaço`: Pausar/Reproduzir.
- `f`: Alternar tela cheia.
- `9` / `0`: Diminuir/Aumentar volume.
- `m`: Mutar áudio.
- `Setas`: Avançar/Retroceder.
- `q`: Sair.
