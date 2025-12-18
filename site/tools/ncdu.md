# ncdu

**ncdu** (NCurses Disk Usage) é uma ferramenta de análise de uso de disco com
uma interface ncurses. É famoso por ser rápido, simples de usar e funcionar em
qualquer ambiente POSIX com ncurses instalado.

É uma excelente alternativa ao comando `du` para visualizar o que está ocupando
espaço no seu disco.

## Uso

Para analisar o diretório atual:

```bash
$ ncdu
```

Para analisar um diretório específico (ex: raiz):

```bash
$ ncdu /
```

## Navegação

* Use as setas **Cima/Baixo** para selecionar arquivos ou diretórios.
* Use **Enter** ou seta **Direita** para entrar em um diretório.
* Use seta **Esquerda** para voltar ao diretório pai.
* Pressione **d** para deletar o arquivo/diretório selecionado (cuidado!).
* Pressione **q** para sair.
