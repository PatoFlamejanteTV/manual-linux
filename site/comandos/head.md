# head

O comando `head` (do inglês, "cabeça") serve para exibir as **primeiras partes** de um arquivo de texto, sem precisar abri-lo por completo.

Ele é o comando irmão do `tail`, que faz a mesma coisa, mas para o final do arquivo.

Por padrão, o `head` mostra as primeiras 10 linhas. É muito útil para dar uma espiada rápida no começo de um arquivo e entender do que se trata, como checar o cabeçalho de um arquivo CSV ou as primeiras linhas de um código-fonte.

## Exemplo Básico

Ao usar o `head` sem nenhuma opção, ele exibirá as 10 primeiras linhas do arquivo especificado.

```bash
$ head /etc/services
# Network services, Internet style
#
# Note that it is presently the policy of IANA to assign a single well-known
# port number for both TCP and UDP; hence, most entries here have two entries
# even if the protocol doesn't support UDP operations.
# Updated from https://www.iana.org/assignments/service-names-port-numbers
#
# See also:
# https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
tcpmux          1/tcp                           # TCP Port Service Multiplexer
```

## Especificando o número de linhas com `-n`

Assim como no `tail`, você pode usar a opção `-n` para definir exatamente quantas linhas quer ver.

```bash
# Para ver as 3 primeiras linhas do arquivo
$ head -n 3 /etc/services
# Network services, Internet style
#
# Note that it is presently the policy of IANA to assign a single well-known

# Uma sintaxe alternativa e mais curta para o mesmo comando
$ head -3 /etc/services
# Network services, Internet style
#
# Note that it is presently the policy of IANA to assign a single well-known
```
O `head` é uma ferramenta simples, mas que economiza muito tempo no dia a dia para inspecionar arquivos rapidamente.

## Exemplo com arquivo local

```bash
$ head -n 3 exemplo.txt
Linha 1
Linha 2
Linha 3
```
