# jobs

Lista os processos que estão rodando em segundo plano ou suspensos no shell atual.

```
╭─quack @ termux in ~
╰─❯ sleep 100 &
[1] 12345
╭─quack @ termux in ~
╰─❯ sleep 200 &
[2] 12346
╭─quack @ termux in ~
╰─❯ jobs
[1]-  Executando             sleep 100 &
[2]+  Executando             sleep 200 &
```
