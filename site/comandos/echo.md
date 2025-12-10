# echo
Literalmente um "repeteco", um comando pra mostrar o que você acabou de passar pra ele, parece inútil, mas você pode usar para escrever a saída dele (literalmente o que você quiser) em um arquivo (também praticamente qualquer arquivo).

```
╭─quack @ termux in ~
╰─❯ echo Olá!
Olá!
╭─quack @ termux in ~
╰─❯ echo oi! > arquivo.txt
╭─quack @ termux in ~
╰─❯ cat arquivo.txt
─────┬─────────────────────────────────────────────────
     │ File: arquivo.txt
─────┼─────────────────────────────────────────────────
   1 │ oi!
─────┴─────────────────────────────────────────────────
╭─quack @ termux in ~
╰─❯
```