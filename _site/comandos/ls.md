# ls
Um dos comandos mais básicos, simples, e utilizados do Linux, usado para mostrar arquivos na pasta ("diretório") atual.

```
╭─quack @ termux in ~
╰─❯ ls                                                 .rw------- 185k u0_a502 20 Nov 20:24  dark_waves.png.1
drwx------    - u0_a502 20 Nov 20:25  Desktop/        drwx------    - u0_a502 20 Nov 20:07 󰉍 Downloads/
.rw-------    6 u0_a502  7 Dec 21:01  exemplo.txt
.rw-------  35k u0_a502 20 Nov 20:17  install.sh
drwx------    - u0_a502 20 Nov 20:05  storage/        .rw------- 285k u0_a502 20 Nov 20:36  termux_setup.log
╭─quack @ termux in ~
╰─❯
```

Também já alguns argumentos que você possa usar junto com o `ls`. (_por mais que eu não use nenhum deles..._)

```
╭─quack @ termux in ~
╰─❯ ls -f
.rw------- 185k u0_a502 20 Nov 20:24  dark_waves.png.1
.rw-------    6 u0_a502  7 Dec 21:01  exemplo.txt
.rw-------  35k u0_a502 20 Nov 20:17  install.sh
.rw------- 285k u0_a502 20 Nov 20:36  termux_setup.log
╭─quack @ termux in ~
╰─❯ ls -d
drwx------ - u0_a502  7 Dec 21:01  ./
╭─quack @ termux in ~
╰─❯
```