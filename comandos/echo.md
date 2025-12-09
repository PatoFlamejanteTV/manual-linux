# `echo`

Literalmente um "repeteco", um comando pra mostrar o que você acabou de passar pra ele. Parece inútil, mas é super útil para escrever coisas em arquivos.

```bash
# Ele repete o que você escreve
$ echo "Olá, mundo!"
Olá, mundo!

# E você pode mandar essa repetição para um arquivo
$ echo "Isso vai para dentro do arquivo." > meu_arquivo.txt

# Se usar 'cat' para ver o arquivo...
$ cat meu_arquivo.txt
Isso vai para dentro do arquivo.
```

**Dica:**

*   `>`: Cria um novo arquivo ou apaga o que já existe para escrever o novo conteúdo.
*   `>>`: Adiciona o conteúdo no final do arquivo, sem apagar nada.
