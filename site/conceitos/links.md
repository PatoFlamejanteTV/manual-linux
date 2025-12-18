# Links

Links são atalhos para arquivos. Existem dois tipos principais no Linux.

## Hard Links

Apontam diretamente para os dados no disco (inode). Se você apagar o arquivo
original, o hard link continua funcionando pois os dados ainda estão lá.

* **Não funcionam entre partições diferentes.**
* **Não podem ser feitos para diretórios (geralmente).**

## Soft (Symbolic) Links

São como atalhos do Windows. Apontam para o *caminho* do arquivo. Se apagar o
original, o link quebra.

* `ln -s alvo link`: Cria um link simbólico.
* **Podem apontar para qualquer lugar.**
