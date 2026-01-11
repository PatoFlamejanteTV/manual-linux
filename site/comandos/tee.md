# tee

O **tee** lê da entrada padrão e escreve na saída padrão e em arquivos simultaneamente.

## Salvar log e ver na tela

```bash
./script.sh | tee saida.log
```

## Append (Adicionar ao final)

Use `-a` para não sobrescrever o arquivo:

```bash
echo "nova linha" | tee -a saida.log
```
