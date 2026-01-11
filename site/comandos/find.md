# find

O comando `find` é uma ferramenta de busca extremamente poderosa e flexível. Ele permite procurar por arquivos e diretórios em uma hierarquia de pastas com base em diferentes critérios, como nome, tipo, tamanho, data de modificação e muito mais.

A sintaxe básica é: `find [onde_procurar] [critério] [o_que_procurar]`

*   **onde_procurar**: O diretório inicial da busca. Usar `.` significa "a partir do diretório atual".
*   **critério**: O tipo de busca que você quer fazer (ex: `-name` para nome, `-type` para tipo).
*   **o_que_procurar**: O termo da sua busca.

## Procurando por nome (`-name`)

Este é o uso mais comum. Ele busca por arquivos e diretórios com um nome exato.

```bash
# Procurar por um arquivo chamado "logo.png" a partir do diretório atual
$ find . -name "logo.png"
./assets/images/logo.png
```

Você pode usar curingas (`*`) para buscar por padrões. Lembre-se de colocar o padrão entre aspas para que o shell não o interprete.

```bash
# Encontrar todos os arquivos que terminam com ".md"
$ find . -name "*.md"
./README.md
./conceitos/shell.md
./comandos/find.md
```

## Procurando por tipo (`-type`)

Você também pode filtrar a busca pelo tipo do item. Os mais comuns são:
*   `f`: para arquivos (**f**ile)
*   `d`: para diretórios (**d**irectory)

```bash
# Encontrar todos os diretórios chamados "node_modules"
$ find . -type d -name "node_modules"
./projeto1/node_modules
./projeto2/node_modules
```

```bash
# Encontrar todos os arquivos de configuração do "Vim" (que terminam com .vimrc)
$ find /home -type f -name "*.vimrc"
/home/jules/.vimrc
/home/jules/backups/.vimrc
```

O `find` pode parecer complexo no início, mas é uma das ferramentas mais úteis para se dominar no terminal.

## Teste em Terminal Real

Buscando todos os arquivos Python (`*.py`) no diretório atual:

```bash
$ find . -name "*.py"
./update_readmes.py
```

Buscando por um diretório chamado "site":

```bash
$ find . -type d -name "site"
./site
./.git/modules/site
```

## Buscas Avançadas

### Por Data de Modificação (`-mtime`)

Encontrar arquivos modificados nos últimos dias.

```bash
# Modificados nos últimos 7 dias
find . -mtime -7

# Modificados há mais de 30 dias
find . -mtime +30
```

### Por Tamanho (`-size`)

```bash
# Arquivos maiores que 100MB
find . -size +100M
```

## Executando Comandos (`-exec`)

O poder real do `find` é fazer algo com o que ele encontra. Use `{}` como placeholder para o arquivo encontrado.

```bash
# Mudar permissão de todos os arquivos .sh para executável
find . -name "*.sh" -exec chmod +x {} \;
```

Note o `\;` no final, é obrigatório para terminar o comando.

### Deletar (`-delete`)

Cuidado! Apaga sem perguntar.

```bash
# Apagar todos os arquivos .tmp
find . -name "*.tmp" -delete
```

