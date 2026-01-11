# cat
Miau! Um comando simples para exibir o conteúdo de um arquivo, dependendo de alguma extensão ou personalização do terminal, ele pode aparecer com uns "firuleibes", mas, por exemplo, no GRUB Shell, o resultado de um cat é só os conteúdos sendo exibidos diretamente no terminal.

```
╭─quack @ termux in ~
╰─❯ ls                                                 .rw------- 185k u0_a502 20 Nov 20:24  dark_waves.png.1
drwx------    - u0_a502 20 Nov 20:25  Desktop/        drwx------    - u0_a502 20 Nov 20:07 󰉍 Downloads/
.rw-------  35k u0_a502 20 Nov 20:17  install.sh
drwx------    - u0_a502 20 Nov 20:05  storage/
.rw------- 285k u0_a502 20 Nov 20:36  termux_setup.log╭─quack @ termux in ~
╰─❯ echo teste > exemplo.txt
╭─quack @ termux in ~
╰─❯ cat exemplo.txt
─────┬─────────────────────────────────────────────────
     │ File: exemplo.txt
─────┼─────────────────────────────────────────────────   1 │ teste
─────┴─────────────────────────────────────────────────
╭─quack @ termux in ~
╰─❯
```

No exemplo acima, eu usei o `ls` para listar os arquivos na pasta atual, e usei o `echo` para escrever `teste` no arquivo `exemplo.txt`. Após isso, eu li os conteúdos dele usando o `cat`.

## Exemplo Simples

```bash
$ cat exemplo.txt
Linha 1
Linha 2
Linha 3
Esta é uma linha importante
Outra linha
Linha final
ERROR: Algo deu errado
WARN: Aviso
INFO: Tudo certo
```