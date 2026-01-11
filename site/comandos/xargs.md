# xargs

O **xargs** constrói e executa comandos a partir da entrada padrão.

## Deletar arquivos encontrados

```bash
find . -name "*.tmp" | xargs rm
```

## Executar para cada item

Use `-I` para especificar onde o argumento vai:

```bash
cat lista_urls.txt | xargs -I {} wget {}
```
