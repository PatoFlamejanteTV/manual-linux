# which

Localiza o caminho executável de um comando.

```
╭─quack @ termux in ~
╰─❯ which python3
/usr/bin/python3
```

Se o comando não existir ou não estiver no PATH, não retorna nada.

```
╭─quack @ termux in ~
╰─❯ which comando_inexistente
╭─quack @ termux in ~
╰─❯
```
