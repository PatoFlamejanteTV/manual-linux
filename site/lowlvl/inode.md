# Inode (Index Node)

No sistema de arquivos Linux, um **inode** é uma estrutura de dados que armazena
informações sobre um arquivo ou diretório, exceto seu nome e seus dados reais.

## O que contém um Inode?

Cada arquivo tem um inode único no sistema de arquivos. O inode contém:

*   **Permissões**: Quem pode ler, escrever ou executar.
*   **Proprietário e Grupo**: Quem é dono do arquivo.
*   **Tamanho**: O tamanho do arquivo em bytes.
*   **Timestamps**: Quando foi criado, modificado ou acessado.
*   **Ponteiros**: Apontam para os blocos no disco onde os dados estão
    realmente gravados.

## Comandos

Você pode ver o número do inode de um arquivo com a opção `-i` do `ls`:

```bash
$ ls -i arquivo.txt
123456 arquivo.txt
```

Para ver o uso de inodes no disco (eles são finitos!):

```bash
$ df -i
```
