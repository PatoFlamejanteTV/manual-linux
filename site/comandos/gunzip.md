# gunzip

O comando `gunzip` (abreviação de **G**NU **unzip**) é o parceiro do `gzip`: ele serve para **descompactar** arquivos que foram compactados no formato `.gz`.

Assim como o `gzip`, o `gunzip` também remove o arquivo original por padrão. Ou seja, ao descompactar `arquivo.txt.gz`, ele irá criar o `arquivo.txt` e apagar o `.gz`.

## Exemplo de uso

Vamos usar o arquivo que foi compactado no exemplo do `gzip`.

```bash
# 1. Veja o arquivo compactado
$ ls -l
-rw-rw-r-- 1 user user 45 Dec 10 15:30 texto.log.gz

# 2. Descompacte o arquivo
$ gunzip texto.log.gz

# 3. Verifique o resultado
$ ls -l
-rw-rw-r-- 1 user user 55 Dec 10 15:30 texto.log
```

**Analisando o resultado:**

*   O arquivo `texto.log.gz` foi removido.
*   O arquivo original, `texto.log`, foi restaurado com seu conteúdo e tamanho originais.

Você pode confirmar que o conteúdo foi restaurado usando o comando `cat`:
```bash
$ cat texto.log
Este é um exemplo de texto que será compactado pelo gzip.
```

É simples assim! `gzip` para compactar, `gunzip` para descompactar.
