# du

O comando `du` (abreviação de **d**isk **u**sage) serve para verificar o espaço em disco **usado** por arquivos e diretórios.

Enquanto o `df` mostra o espaço total e livre das partições, o `du` é mais específico, permitindo saber o tamanho de uma pasta ou arquivo em particular.

## Exemplo com `-h` e `-s`

As opções mais comuns para o `du` são:
*   `-h` (**h**uman-readable): Mostra os tamanhos em formato legível (KB, MB, GB).
*   `-s` (**s**ummarize): Exibe apenas o total para cada argumento, em vez de listar o tamanho de todos os subdiretórios.

Juntando as duas, o comando `du -sh` é perfeito para saber o tamanho total de uma pasta.

```bash
$ du -sh Documentos/ Videos/ Imagens/
3.5G    Documentos/
12G     Videos/
1.2G    Imagens/
```

**Entendendo a saída:**

O comando acima mostra o tamanho total de cada um dos diretórios especificados. A primeira coluna é o espaço usado e a segunda é o nome do diretório.

Se você executar `du -h` sem um caminho específico, ele mostrará o tamanho de todos os subdiretórios a partir de onde você está.
