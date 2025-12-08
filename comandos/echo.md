# `echo`

O comando `echo` é usado para exibir uma linha de texto ou uma string no terminal.

Sua função principal é imprimir seus argumentos na saída padrão. Ele é frequentemente usado em scripts para exibir mensagens ou para redirecionar texto para um arquivo.

### Exemplos

**Exibir uma mensagem:**
```bash
$ echo "Olá, mundo!"
Olá, mundo!
```

**Escrever em um arquivo:**
Você pode usar o operador de redirecionamento `>` para escrever a saída do `echo` em um arquivo. Se o arquivo não existir, ele será criado. Se já existir, seu conteúdo será sobrescrito.

```bash
$ echo "Este é um novo arquivo." > meu_arquivo.txt
$ cat meu_arquivo.txt
Este é um novo arquivo.
```

**Acrescentar a um arquivo:**
Para adicionar texto ao final de um arquivo existente sem apagar seu conteúdo, use o operador `>>`:

```bash
$ echo "Adicionando uma nova linha." >> meu_arquivo.txt
$ cat meu_arquivo.txt
Este é um novo arquivo.
Adicionando uma nova linha.
```
