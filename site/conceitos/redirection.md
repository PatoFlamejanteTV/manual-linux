# Redirecionamento e Pipes

No Linux, tudo gira em torno de fluxos de dados. Entender como controlar para
onde esses dados vão é um superpoder.

## Fluxos Padrão

Todo programa tem três canais de comunicação abertos por padrão:

* **Stdin (0):** Entrada padrão (geralmente o teclado).
* **Stdout (1):** Saída padrão (geralmente a tela).
* **Stderr (2):** Erro padrão (também a tela, mas separado do stdout).

## Operadores

* `>`: Redireciona a saída (stdout) para um arquivo (sobrescreve).
* `>>`: Redireciona a saída para um arquivo (anexa no final).
* `<`: Redireciona a entrada (lê de um arquivo).
* `|` (Pipe): Joga a saída de um comando na entrada do próximo.

Exemplo: `ls -l | grep "txt" > lista.txt`
