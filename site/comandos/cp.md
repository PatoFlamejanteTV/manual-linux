# cp

O comando `cp` (abreviação de **c**o**p**y) é usado para copiar arquivos e diretórios. É uma das operações mais fundamentais e utilizadas no dia a dia no terminal.

A sintaxe básica é: `cp [opções] origem destino`

*   **origem**: O arquivo ou diretório que você quer copiar.
*   **destino**: Para onde você quer copiar o arquivo/diretório.

## 1. Copiando um arquivo (e renomeando)

O uso mais simples é criar uma cópia exata de um arquivo no mesmo diretório, mas com um nome diferente.

```bash
# Cria um arquivo original
$ echo "Conteúdo original" > relatorio.txt

# Copia relatorio.txt para relatorio_backup.txt
$ cp relatorio.txt relatorio_backup.txt

# Verifica se os dois arquivos existem
$ ls
relatorio.txt  relatorio_backup.txt

# Confirma que o conteúdo foi copiado
$ cat relatorio_backup.txt
Conteúdo original
```

## 2. Copiando um arquivo para outro diretório

Se o `destino` for um diretório, o `cp` copiará o arquivo de `origem` para dentro desse diretório, mantendo o mesmo nome.

```bash
# Cria um diretório para backups
$ mkdir backups/

# Copia o arquivo para a pasta backups
$ cp relatorio.txt backups/

# Verifica o conteúdo da pasta
$ ls backups/
relatorio.txt
```

## 3. Copiando múltiplos arquivos

Você pode listar vários arquivos como `origem` e, desde que o `destino` final seja um diretório, todos eles serão copiados para lá.

```bash
$ cp relatorio.txt foto.jpg script.sh documentos/
```

## 4. Copiando diretórios com `-r`

Assim como no `rm`, se você tentar copiar um diretório sem nenhuma opção, o `cp` dará um erro. Para copiar um diretório e todo o seu conteúdo (incluindo subdiretórios e arquivos), você precisa usar a opção `-r` (**r**ecursive).

```bash
# Copia a pasta "projeto_final" e tudo dentro dela para uma nova pasta "projeto_final_backup"
$ cp -r projeto_final projeto_final_backup
```
Esta é a forma correta de fazer backup de uma pasta inteira.

## Teste em Terminal Real

```bash
$ cp test_dir_xyz/file1.txt test_dir_xyz/file2.txt
'test_dir_xyz/file1.txt' -> 'test_dir_xyz/file2.txt'

$ ls -l test_dir_xyz/
total 0
-rw-rw-r-- 1 quack quack 0 jan 11 15:23 file1.txt
-rw-rw-r-- 1 quack quack 0 jan 11 15:23 file2.txt
```
