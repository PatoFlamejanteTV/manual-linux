# sed

O **sed** (stream editor) é usado para filtrar e transformar texto.

## Substituição Simples

Substituir a primeira ocorrência de "velho" por "novo":

```bash
echo "velho mundo" | sed 's/velho/novo/'
```

## Substituição Global

Substituir todas as ocorrências na linha:

```bash
sed 's/erro/acerto/g' arquivo.txt
```

## Deletar linhas

Deletar a segunda linha:

```bash
sed '2d' arquivo.txt
```
