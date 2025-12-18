# yt-dlp

O yt-dlp é um gerenciador de download de vídeo de linha de comando para YouTube
e outros sites de vídeo. É um fork do famoso `youtube-dl` com recursos
adicionais e correções mais frequentes.

## Instalação

```bash
# Baixando o binário diretamente (recomendado)
sudo curl -L \
  https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp \
  -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

## Exemplos de Uso

### Baixar um vídeo

Simplesmente passe a URL:

```bash
yt-dlp "URL_DO_VIDEO"
```

### Baixar apenas o áudio

Extrair o áudio em formato MP3:

```bash
yt-dlp -x --audio-format mp3 "URL_DO_VIDEO"
```

### Baixar playlist completa

```bash
yt-dlp -i --yes-playlist "URL_DA_PLAYLIST"
```

### Listar formatos disponíveis

Ver quais resoluções e codecs estão disponíveis para um vídeo:

```bash
yt-dlp -F "URL_DO_VIDEO"
```
