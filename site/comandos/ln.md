# ln

Cria links entre arquivos. Por padrão cria links "hard", mas com a opção `-s` cria links simbólicos (symlinks), que são como atalhos.

```
╭─quack @ termux in ~
╰─❯ ln -s arquivo_original.txt meu_link
╭─quack @ termux in ~
╰─❯ ls -l meu_link
lrwxrwxrwx 1 quack quack 20 Jan 21 18:05 meu_link -> arquivo_original.txt
```
