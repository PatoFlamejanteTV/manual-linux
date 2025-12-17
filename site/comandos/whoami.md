# whoami

O comando `whoami` (quem sou eu) exibe o nome do usuário que está logado atualmente no terminal.

É útil quando você está alternando entre usuários (como root) e quer confirmar qual usuário está ativo.

## Exemplos

```bash
$ whoami
usuario
```

Se você usar `sudo`, o comando pode retornar `root` se executado em um shell de root:

```bash
$ sudo whoami
root
```
