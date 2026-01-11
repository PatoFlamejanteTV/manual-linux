# uniq

O **uniq** reporta ou omite linhas repetidas. Geralmente usado após o `sort`.

## Remover duplicatas adjacentes

```bash
sort arquivo.txt | uniq
```

## Contar ocorrências

Conta quantas vezes cada linha aparece:

```bash
sort arquivo.txt | uniq -c
```

## Mostrar apenas linhas duplicadas

```bash
sort arquivo.txt | uniq -d
```
