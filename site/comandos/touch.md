# touch

O comando `touch` é usado principalmente para criar arquivos vazios. Se o arquivo já existir, ele atualiza a data de modificação ("timestamp") do arquivo para o momento atual, sem alterar seu conteúdo.

## Exemplos

Para criar um arquivo novo:

```bash
$ touch arquivo.txt
```

Você pode criar vários arquivos de uma vez:

```bash
$ touch arquivo1.txt arquivo2.txt arquivo3.txt
```

Se `arquivo.txt` já existir, o comando abaixo apenas atualizará a data de acesso e modificação dele:

```bash
$ touch arquivo.txt
```

## Teste em Terminal Real

```bash
$ touch test_dir_xyz/file1.txt
$ ls -l test_dir_xyz/file1.txt
-rw-rw-r-- 1 quack quack 0 jan 11 15:23 test_dir_xyz/file1.txt
```
