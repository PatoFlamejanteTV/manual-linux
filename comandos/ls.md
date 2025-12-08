# `ls`

O comando `ls` (abreviação de "list") é um dos comandos mais fundamentais em sistemas Linux. Ele é usado para listar os arquivos e diretórios contidos em um diretório específico.

### Uso Básico
Quando executado sem argumentos, `ls` lista o conteúdo do diretório atual:
```bash
$ ls
documentos.txt  imagens/  musicas/  videos/
```

### Opções Comuns
O `ls` possui várias opções (flags) que modificam seu comportamento:

* `-l`: Lista os arquivos em formato longo, exibindo permissões, proprietário, tamanho e data de modificação.
* `-a`: Mostra todos os arquivos, incluindo os ocultos (aqueles que começam com `.`).
* `-h`: Quando usado com `-l`, exibe os tamanhos dos arquivos em um formato legível por humanos (por exemplo, `1K`, `2M`, `3G`).
* `-t`: Ordena os arquivos por data de modificação, dos mais recentes para os mais antigos.

### Exemplos com Opções

**Listagem em formato longo:**
```bash
$ ls -l
total 12
-rw-r--r-- 1 usuario grupo 1024 Jan 1 12:00 documentos.txt
drwxr-xr-x 2 usuario grupo 4096 Jan 1 12:00 imagens/
drwxr-xr-x 2 usuario grupo 4096 Jan 1 12:00 musicas/
drwxr-xr-x 2 usuario grupo 4096 Jan 1 12:00 videos/
```

**Listar todos os arquivos, incluindo os ocultos:**
```bash
$ ls -a
.  ..  .config/  documentos.txt  imagens/  musicas/  videos/
```

**Combinando opções:**
É comum combinar várias opções. Por exemplo, `ls -lah` lista todos os arquivos em formato longo e com tamanhos legíveis.
```bash
$ ls -lah
total 20K
drwxr-xr-x 4 usuario grupo 4.0K Jan  1 12:05 .
drwxr-xr-x 3 usuario grupo 4.0K Jan  1 12:00 ..
drwxr-xr-x 2 usuario grupo 4.0K Jan  1 12:00 .config/
-rw-r--r-- 1 usuario grupo 1.0K Jan  1 12:00 documentos.txt
drwxr-xr-x 2 usuario grupo 4.0K Jan  1 12:00 imagens/
drwxr-xr-x 2 usuario grupo 4.0K Jan  1 12:00 musicas/
drwxr-xr-x 2 usuario grupo 4.0K Jan  1 12:00 videos/
```
