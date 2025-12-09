# mv

O comando `mv` (abreviação de **m**o**v**e) tem duas funções principais e muito importantes: **renomear** e **mover** arquivos e diretórios.

A ação que ele executa (renomear ou mover) depende do segundo argumento que você passa para ele. A sintaxe básica é a mesma do `cp`: `mv origem destino`.

## 1. Renomeando arquivos e diretórios

Se o `destino` for um **novo nome** no mesmo diretório, o `mv` simplesmente renomeia a `origem`.

```bash
# Cria um arquivo com um nome temporário
$ touch relatorio_temp.txt

# Renomeia o arquivo
$ mv relatorio_temp.txt relatorio_final.txt

# Verifica o resultado (o nome antigo sumiu)
$ ls
relatorio_final.txt
```
O mesmo vale para diretórios. Ao contrário de `cp` e `rm`, você não precisa de nenhuma opção `-r` para renomear ou mover um diretório.

```bash
$ mv pasta_antiga/ pasta_nova/
```

## 2. Movendo arquivos e diretórios

Se o `destino` for um **diretório existente**, o `mv` move a `origem` para dentro desse diretório.

```bash
# Cria uma pasta para arquivar relatórios
$ mkdir Arquivados/

# Move o relatório final para dentro da pasta
$ mv relatorio_final.txt Arquivados/

# Verifica o resultado
$ ls
Arquivados/
$ ls Arquivados/
relatorio_final.txt
```

Você também pode mover múltiplos arquivos de uma vez para um diretório.
```bash
$ mv foto.jpg video.mp4 musica.mp3 Midia/
```

## 3. Movendo e renomeando ao mesmo tempo

Você pode combinar as duas operações. Se o `destino` for um diretório **e** um novo nome de arquivo, o `mv` moverá e renomeará em um único passo.

```bash
# Move o arquivo para a pasta "Arquivados" e o renomeia para "relatorio_2023.txt"
$ mv relatorio_final.txt Arquivados/relatorio_2023.txt
```

O comando `mv` é eficiente porque, na maioria das vezes (dentro do mesmo sistema de arquivos), ele não precisa copiar os dados do arquivo; ele apenas atualiza os "ponteiros" que indicam onde o arquivo está e qual é o seu nome.
