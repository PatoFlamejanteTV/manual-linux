# rm

O comando `rm` (abreviação de **r**e**m**ove) é usado para apagar arquivos e diretórios.

**MUITO CUIDADO:** Este é um dos comandos mais "perigosos" do Linux, porque os arquivos apagados com `rm` **não vão para a lixeira**. Uma vez removidos, recuperá-los é extremamente difícil ou impossível. Use com atenção!

## Apagando um ou mais arquivos

Para apagar um único arquivo, basta passar o nome dele como argumento.

```bash
# Cria um arquivo de teste
$ touch arquivo_temporario.txt

# Apaga o arquivo
$ rm arquivo_temporario.txt

# Verifica se ele sumiu
$ ls arquivo_temporario.txt
ls: cannot access 'arquivo_temporario.txt': No such file or directory
```

Você também pode apagar múltiplos arquivos de uma vez, listando-os um após o outro.
```bash
$ rm arquivo1.txt foto.jpg documento.pdf
```

## Apagando diretórios com `-r`

Se você tentar usar `rm` em um diretório, receberá um erro. Para apagar um diretório e **todo** o seu conteúdo (incluindo subdiretórios), você precisa usar a opção `-r` (**r**ecursive).

```bash
# Cria uma pasta e alguns arquivos dentro
$ mkdir minha_pasta
$ touch minha_pasta/arquivo1.txt minha_pasta/arquivo2.txt

# Tenta apagar a pasta (dá erro)
$ rm minha_pasta
rm: cannot remove 'minha_pasta': Is a directory

# Apaga a pasta e todo o seu conteúdo recursivamente
$ rm -r minha_pasta

# Verifica se a pasta foi removida
$ ls -d minha_pasta
ls: cannot access 'minha_pasta': No such file or directory
```

### Forçando a remoção com `-f`

Às vezes, alguns arquivos podem pedir confirmação antes de serem apagados (por exemplo, se estiverem protegidos contra escrita). A opção `-f` (**f**orce) ignora esses avisos e força a remoção sem perguntar nada.

A combinação `rm -rf` é extremamente poderosa e perigosa. O comando `rm -rf /` (com privilégios de administrador) pode apagar o seu sistema operacional inteiro. **Sempre verifique duas vezes o que você está digitando!**

## Teste em Terminal Real

Apagando um arquivo:
```bash
$ rm test_dir_xyz/file1.txt
$ ls -l test_dir_xyz/
total 0
-rw-rw-r-- 1 quack quack 0 jan 11 15:23 moved_file.txt
```

Apagando o diretório inteiro:
```bash
$ rm -r test_dir_xyz
$ ls -ld test_dir_xyz
ls: não foi possível acessar 'test_dir_xyz': Arquivo ou diretório inexistente
```
