# pwd

O comando `pwd` (print working directory) é um dos mais simples e úteis do Linux. Ele simplesmente mostra o diretório (pasta) em que você está no momento. É muito útil quando você está navegando por várias pastas e não tem certeza de onde está.

## Exemplos

```bash
$ pwd
/home/quack
```

## Argumentos Suportados

O `pwd` não tem muitos argumentos, mas alguns podem ser úteis:

*   `-L` ou `--logical`: Mostra o caminho lógico, que pode ser um link simbólico.
*   `-P` ou `--physical`: Mostra o caminho físico, resolvendo todos os links simbólicos.

## Fontes

*   [Documentação do GNU Coreutils](https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html)
*   [Manual do `pwd`](https://man7.org/linux/man-pages/man1/pwd.1.html)

## BusyBox/Toybox

O comando `pwd` está disponível tanto no BusyBox quanto no Toybox, sendo um comando essencial em ambos.
