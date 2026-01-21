# nice

Executa um programa com uma prioridade de agendamento modificada. Valores maiores significam menor prioridade (mais "gentil" com outros processos).

```
╭─quack @ termux in ~
╰─❯ nice -n 10 tar -czf backup.tar.gz documentos/
```

Para verificar a prioridade (NI):

```
╭─quack @ termux in ~
╰─❯ ps -o pid,ni,comm
  PID  NI COMMAND
12347  10 tar
12348   0 ps
```
