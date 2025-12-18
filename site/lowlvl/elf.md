# ELF (Executable and Linkable Format)

O formato padrão de arquivos executáveis no Linux é o ELF. Quando você roda um
comando como `ls` ou `bash`, você está executando um arquivo ELF.

## Estrutura

Um arquivo ELF é dividido em partes principais:

*   **ELF Header**: O cabeçalho, que diz "Eu sou um ELF" (começa com o "número
    mágico" `7f 45 4c 46` ou `.ELF`). Ele diz se é 32 ou 64 bits, e a
    arquitetura (x86, ARM, etc).
*   **Program Header Table**: Diz ao sistema como criar o processo na memória.
*   **Section Header Table**: Descreve as seções do arquivo para o linker.

## Ferramentas

Você pode inspecionar arquivos ELF com o comando `readelf`.

```bash
$ readelf -h /bin/ls
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  ...
```
