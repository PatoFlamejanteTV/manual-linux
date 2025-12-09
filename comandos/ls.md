# `ls`

Um dos comandos mais básicos, simples e utilizados do Linux, usado para mostrar arquivos na pasta ("diretório") atual.

```bash
$ ls
Documentos/  Imagens/  Musicas/  README.md
```

Também há alguns argumentos que você pode usar junto com o `ls` (_por mais que eu não use quase nenhum deles..._). Os mais famosos são:

*   `-l`: Mostra uma lista mais detalhada, com permissões, tamanho, data, etc.
*   `-a`: Mostra **todos** os arquivos, incluindo os ocultos (que começam com `.`).
*   `-h`: Quando usado com `-l`, mostra os tamanhos de um jeito mais "humano" de ler (ex: `1K`, `23M`, `2G`).

Você pode até combinar tudo pra ter uma visão completa:

```bash
$ ls -lah
drwxr-xr-x 1 user user 4.0K Jan  1 12:00 .
drwxr-xr-x 1 user user 4.0K Jan  1 12:00 ..
-rw-r--r-- 1 user user  12K Jan  1 12:00 .config
drwxr-xr-x 1 user user 4.0K Jan  1 12:00 Documentos/
drwxr-xr-x 1 user user 4.0K Jan  1 12:00 Imagens/
drwxr-xr-x 1 user user 4.0K Jan  1 12:00 Musicas/
-rw-r--r-- 1 user user  512 Jan  1 12:00 README.md
```
