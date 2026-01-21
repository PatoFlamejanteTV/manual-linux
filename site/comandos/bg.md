# bg

Coloca um processo que estava suspenso para rodar em segundo plano (background).

```
╭─quack @ termux in ~
╰─❯ sleep 100
^Z
[1]+  Parado                 sleep 100
╭─quack @ termux in ~
╰─❯ bg
[1]+ sleep 100 &
```
