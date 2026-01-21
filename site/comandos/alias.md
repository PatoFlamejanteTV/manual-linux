# alias

Cria atalhos ou "apelidos" para comandos mais longos. Útil para personalizar seu ambiente e agilizar tarefas repetitivas.

```
╭─quack @ termux in ~
╰─❯ alias ll='ls -l'
╭─quack @ termux in ~
╰─❯ ll
total 40
-rw-r--r-- 1 quack quack 123 Jan 21 18:00 arquivo.txt
drwxr-xr-x 2 quack quack 4096 Jan 21 18:00 documentos
```

Para ver todos os aliases definidos:

```
╭─quack @ termux in ~
╰─❯ alias
alias ll='ls -l'
alias grep='grep --color=auto'
```
