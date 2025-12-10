# gzip

O comando `gzip` (abreviação de **G**NU **zip**) é uma das ferramentas de compressão mais tradicionais em sistemas Linux. Ele serve para compactar um único arquivo, reduzindo seu tamanho no disco.

Por padrão, quando você usa o `gzip`, ele:
1.  Cria uma versão compactada do arquivo com a extensão `.gz`.
2.  **Remove** o arquivo original.

É ideal para economizar espaço ao armazenar arquivos de texto grandes, como logs.

## Exemplo de uso

Vamos criar um arquivo de texto, ver seu tamanho, compactá-lo e depois ver o resultado.

```bash
# 1. Crie um arquivo de texto
$ echo "Este é um exemplo de texto que será compactado pelo gzip." > texto.log

# 2. Veja o tamanho original
$ ls -l texto.log
-rw-rw-r-- 1 user user 55 Dec 10 15:30 texto.log

# 3. Compacte o arquivo
$ gzip texto.log

# 4. Verifique o resultado
$ ls -l
-rw-rw-r-- 1 user user 45 Dec 10 15:30 texto.log.gz
```

**Analisando o resultado:**

*   O arquivo original `texto.log` foi removido.
*   Um novo arquivo, `texto.log.gz`, foi criado em seu lugar.
*   Note que o tamanho do arquivo compactado (45 bytes) é menor que o original (55 bytes). A economia pode ser muito maior em arquivos maiores.

Para descompactar um arquivo `.gz`, você pode usar o comando `gunzip`.
