# FFmpeg

O FFmpeg é uma estrutura multimídia completa e multiplataforma capaz de
decodificar, codificar, transcodificar, multiplexar, demultiplexar, transmitir,
filtrar e reproduzir praticamente qualquer coisa que humanos e máquinas criaram.

É a "ferramenta suíça" para manipulação de áudio e vídeo no terminal.

## Instalação

```bash
# Debian/Ubuntu
sudo apt install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

## Exemplos de Uso

### Converter vídeo

Converter um arquivo MP4 para MKV:

```bash
ffmpeg -i entrada.mp4 saida.mkv
```

### Extrair áudio de um vídeo

Extrair o áudio e salvar como MP3:

```bash
ffmpeg -i video.mp4 -vn -c:a libmp3lame audio.mp3
```

- `-vn`: Desabilita o vídeo.
- `-c:a libmp3lame`: Define o codec de áudio para MP3.

### Cortar um vídeo

Cortar do segundo 10 até o segundo 20:

```bash
ffmpeg -i entrada.mp4 -ss 00:00:10 -to 00:00:20 -c copy corte.mp4
```

- `-ss`: Tempo de início.
- `-to`: Tempo final.
- `-c copy`: Copia os fluxos sem recodificar (muito rápido).

### Redimensionar vídeo

Redimensionar para largura de 1280px (mantendo proporção):

```bash
ffmpeg -i entrada.mp4 -vf scale=1280:-1 saida.mp4
```
