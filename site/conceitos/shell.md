# Shell

O **Shell** é um programa que atua como uma interface entre o usuário e o [Kernel](kernel.md) do sistema operacional. Ele "envolve" (daí o nome *shell*, ou concha) o núcleo, interpretando os comandos que você digita e traduzindo-os para instruções que o sistema possa executar.

## CLI vs GUI

* **GUI (Graphical User Interface):** É a interface gráfica com janelas, ícones e mouse que usamos no dia a dia.
* **CLI (Command Line Interface):** É a interface de linha de comando, onde usamos o Shell. Embora pareça intimidante, a CLI é muitas vezes mais rápida e poderosa para tarefas complexas ou repetitivas.

## Como funciona?

Quando você abre um terminal, você está vendo um **Prompt** do shell, geralmente algo assim:

```bash
usuario@computador:~$
```

* `usuario`: Quem está logado.
* `computador`: Nome da máquina (hostname).
* `~`: O diretório atual (o til representa a pasta `/home/usuario`).
* `$`: Indica que você é um usuário comum (se fosse `#`, seria o superusuário root).

Quando você digita um comando e aperta Enter, o Shell procura esse programa no sistema e o executa.

## Shells Populares

Existem vários "sabores" de shell, cada um com recursos diferentes:

1. **Bash (Bourne Again Shell):** O padrão na grande maioria das distribuições Linux. É robusto e onipresente. Se você aprender Shell Script, provavelmente aprenderá no dialeto do [Bash](../langs/bash.md).
2. **Zsh (Z Shell):** Muito popular entre desenvolvedores e agora o padrão no macOS. É altamente customizável e possui sistemas de plugins famosos como o "Oh My Zsh".
3. **Fish (Friendly Interactive Shell):** Focado em ser amigável. Possui auto-sugestões coloridas e correções automáticas "fora da caixa", sem precisar configurar nada.
4. **Dash:** Um shell minimalista usado pelo Debian/Ubuntu para scripts de sistema (devido à sua velocidade), mas raramente usado interativamente por humanos.

## Scripting

Além de uso interativo, o Shell é uma linguagem de programação. Você pode salvar uma sequência de comandos em um arquivo de texto para automatizar tarefas. Isso é chamado de **Shell Script**.
