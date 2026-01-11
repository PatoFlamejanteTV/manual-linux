# tar

O comando `tar` (abreviação de **t**ape **ar**chive) é o canivete suíço para lidar com arquivos compactados no Linux. Originalmente, ele foi criado para agrupar arquivos e gravá-los em fitas magnéticas (daí o nome), mas hoje sua principal função é agrupar múltiplos arquivos e diretórios em um único arquivo `.tar`.

É importante entender que o `tar` por si só **não comprime** arquivos, ele apenas os **agrupa**. Para comprimir, ele é combinado com outros algoritmos como `gzip` ou `bzip2`.

## As operações mais comuns

As opções do `tar` podem parecer confusas, mas a maioria dos usos se resume a algumas combinações principais. O segredo é lembrar das letras-chave:
*   `-c`: **C**riar um arquivo.
*   `-x`: **E**xtrair arquivos.
*   `-v`: Modo **v**erbose (mostra os arquivos sendo processados).
*   `-f`: Permite especificar o nome do arquivo (**f**ile) a ser criado ou extraído.

### Criando um arquivo `.tar`

Para agrupar uma pasta e todo o seu conteúdo em um arquivo:

```bash
# Cria um arquivo chamado "meu_projeto.tar" contendo tudo da pasta "meu_projeto/"
$ tar -cvf meu_projeto.tar meu_projeto/
meu_projeto/
meu_projeto/index.html
meu_projeto/style.css
meu_projeto/script.js
```

### Extraindo um arquivo `.tar`

Para extrair o conteúdo de um arquivo `.tar` na pasta atual:
```bash
$ tar -xvf meu_projeto.tar
meu_projeto/
meu_projeto/index.html
meu_projeto/style.css
meu_projeto/script.js
```

## Juntando com compressão (gzip)

O uso mais comum do `tar` é em conjunto com o `gzip` para criar arquivos `.tar.gz` ou `.tgz`, que são agrupados **e** comprimidos. Para isso, basta adicionar a letra `-z`.

### Criando um arquivo `.tar.gz`

```bash
# Adiciona o 'z' para usar gzip
$ tar -czvf meu_projeto.tar.gz meu_projeto/
```
O resultado é um arquivo `meu_projeto.tar.gz` que é menor do que o `meu_projeto.tar` simples.

### Extraindo um arquivo `.tar.gz`

O `tar` é inteligente. Para extrair um `.tar.gz`, você pode usar a mesma opção `-z` ou simplesmente omiti-la, pois ele detecta o formato automaticamente na maioria das vezes.

```bash
# O 'z' diz para descompactar com gzip antes de extrair
$ tar -xzvf meu_projeto.tar.gz

# Na maioria dos sistemas modernos, isso também funciona
$ tar -xvf meu_projeto.tar.gz
```
Dominar `tar -czvf` e `tar -xvf` resolve 99% das suas necessidades com arquivos compactados no Linux.

## Outras Operações Úteis

### Listar conteúdo sem extrair

Para ver o que tem dentro do arquivo sem descompactar tudo:

```bash
# -t: list
tar -tvf arquivo.tar.gz
```

### Extrair um único arquivo

Se você quer apenas um arquivo específico de dentro do pacote:

```bash
tar -xvf arquivo.tar.gz pasta/arquivo_especifico.txt
```

### Outros Formatos de Compressão

O `tar` suporta outros algoritmos que podem comprimir mais (mas demoram mais):

*   **Bzip2** (`.tar.bz2`): Use a flag `-j`.
    ```bash
    tar -cjvf arquivo.tar.bz2 pasta/
    ```

*   **Xz** (`.tar.xz`): Use a flag `-J` (maiúsculo). Geralmente a melhor compressão.
    ```bash
    tar -cJvf arquivo.tar.xz pasta/
    ```

## FAQ

**Q: Erro "Exiting with failure status due to previous errors"**
R: Geralmente acontece quando você tenta criar um tar de arquivos que não tem permissão de leitura, ou se os arquivos mudaram enquanto o tar estava rodando.

