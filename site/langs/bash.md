# Bash

Bash (Bourne Again SHell) é o shell padrão na maioria das distribuições Linux. Além de ser o interpretador de comandos onde você digita `ls` e `cd`, o Bash é também uma linguagem de script poderosa.

Scripts em Bash (geralmente com extensão `.sh`) são usados para automatizar tarefas, configurar sistemas e criar ferramentas simples.

## Exemplo de Script

Um script simples `ola.sh`:

```bash
#!/bin/bash
# Isso é um comentário

echo "Qual é o seu nome?"
read nome
echo "Olá, $nome! Bem-vindo ao Linux."
```

Para executar, você precisa dar permissão de execução:

```bash
$ chmod +x ola.sh
$ ./ola.sh
```
