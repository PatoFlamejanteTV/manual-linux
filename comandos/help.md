# `help`

É praticamente uma lista de comandos dentro do terminal. Ele exibe os comandos internos do seu shell (como o Bash), juntamente com os `-argumentos` e `--flags` que você pode usar.

É extremamente útil caso você esteja em uma distro mais "hacker" (Arch, Gentoo, LFS, etc.), ou quando você faz algo errado no sistema e seu computador inicia no GRUB bash (um dos meus traumas, particularmente).

### Como usar

Se você digitar `help` sozinho, ele vai cuspir uma lista gigante. É mais útil pedir ajuda para um comando específico:

```bash
$ help cd
cd: cd [-L|[-P [-e]]] [-@] [dir]
    Change the shell working directory.

    # ... (e continua com mais detalhes)
```

Assim, ele te dá a "colinha" do que o comando `cd` faz e de como usá-lo.
