# tr

Traduz ou deleta caracteres da entrada padrão. Muito útil em pipes.

```
╭─quack @ termux in ~
╰─❯ echo "ola mundo" | tr 'a-z' 'A-Z'
OLA MUNDO
```

Deletando caracteres específicos:

```
╭─quack @ termux in ~
╰─❯ echo "o.l.a" | tr -d '.'
ola
```
