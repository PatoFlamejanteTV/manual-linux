# grep

O `grep` ( **g**lobal **r**egular **e**xpression **p**rint) é uma das ferramentas de linha de comando mais poderosas e mais utilizadas no mundo Linux. Sua principal função é **buscar por texto dentro de arquivos**.

Ele lê o conteúdo de um ou mais arquivos, linha por linha, e exibe apenas as linhas que contêm o padrão de texto que você especificou.

A sintaxe básica é: `grep [opções] "padrão_de_texto" [arquivo(s)]`

## Exemplo Básico

Vamos supor que temos um arquivo `compras.txt` com o seguinte conteúdo:
```
Leite
Ovos
Café
Pão
Manteiga
```

Para encontrar a linha que contém "Café", faríamos:
```bash
$ grep "Café" compras.txt
Café
```

## Buscando sem diferenciar maiúsculas e minúsculas (`-i`)

Por padrão, o `grep` diferencia "Café" de "café". Se você quiser que a busca ignore essa diferença, use a opção `-i` (**i**nsensitive).

```bash
# O arquivo agora contém "café" em minúsculas
$ echo "café" > compras.txt

# A busca normal não encontra nada
$ grep "Café" compras.txt

# Com -i, a busca funciona
$ grep -i "Café" compras.txt
café
```

## Buscando em múltiplos arquivos e recursivamente (`-r`)

Se você precisa encontrar um texto em um projeto com muitas pastas e arquivos, a opção `-r` (**r**ecursive) é sua melhor amiga. Ela faz o `grep` procurar no diretório especificado e em todos os subdiretórios.

```bash
# Procurar pela palavra "import" em todos os arquivos dentro da pasta "src/"
$ grep -r "import" src/
src/index.js:import React from 'react';
src/components/Button.js:import styles from './styles.css';
src/utils/api.js:import { API_URL } from '../constants';
```
A opção `-r` geralmente é combinada com `-i` (`grep -ri ...`) para buscas mais abrangentes. Dominar o `grep` é um superpoder para qualquer pessoa que usa o terminal.
