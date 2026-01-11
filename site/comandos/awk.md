# awk

O **awk** é uma linguagem de programação voltada para processamento de padrões e varredura de arquivos.

## Imprimir coluna específica

Imprimir apenas a primeira coluna de um arquivo (separado por espaços):

```bash
awk '{print $1}' arquivo.txt
```

## Usar outro delimitador

Imprimir a segunda coluna de um arquivo CSV (separado por vírgula):

```bash
awk -F, '{print $2}' dados.csv
```

## Filtrar linhas

Imprimir linhas onde a terceira coluna é maior que 10:

```bash
awk '$3 > 10' numeros.txt
```
