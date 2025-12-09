# less

O comando `less` é um visualizador de arquivos de texto muito poderoso e flexível. O nome é uma brincadeira com um comando mais antigo chamado `more` (em inglês, "less" é menos e "more" é mais), com a ideia de que "menos te dá mais".

Ao contrário do `cat`, que joga todo o conteúdo do arquivo na tela de uma vez, o `less` abre o arquivo em um ambiente interativo, permitindo que você navegue pelo texto para cima e para baixo.

Isso o torna ideal para ler arquivos longos, como logs ou códigos-fonte.

## Exemplo de uso

Para abrir um arquivo com o `less`, basta digitar:

```bash
$ less /var/log/syslog
```

Isso abrirá o arquivo de log do sistema em tela cheia.

### Comandos de Navegação

Uma vez dentro do `less`, você não digita no terminal, mas usa teclas para navegar:

*   **Setas (↑ e ↓)** ou **Page Up/Page Down**: Para rolar o texto.
*   **/texto**: Para buscar por "texto" dentro do arquivo. Pressione `n` para ir para a próxima ocorrência e `N` para a anterior.
*   **g**: Para ir para o início do arquivo.
*   **G**: Para ir para o final do arquivo.
*   **h**: Para exibir uma tela de ajuda com todos os comandos.
*   **q**: Para **q**uitar (sair) do `less` e voltar ao terminal.

O `less` é uma daquelas ferramentas que, depois que você se acostuma, não consegue mais viver sem!
