# chown

O comando `chown` (abreviação de **ch**ange **own**er) é usado para mudar o **dono** e/ou o **grupo** de um arquivo ou diretório.

No Linux, todo arquivo pertence a um usuário e a um grupo. Essas propriedades são fundamentais para o sistema de permissões, pois definem quem pode ler, escrever ou executar o arquivo (junto com o `chmod`). O `chown` é o comando que permite ao superusuário (`root`) ou ao dono do arquivo transferir essa propriedade.

A sintaxe básica é: `chown [novo_dono]:[novo_grupo] [arquivo_ou_diretorio]`

**Nota:** Na maioria das vezes, você precisará usar `sudo` para executar o `chown`, a menos que você já seja o `root`.

## Exemplos de Uso

Vamos imaginar que temos um arquivo `relatorio.txt` que pertence ao usuário `ana` e ao grupo `vendas`.

```bash
$ ls -l relatorio.txt
-rw-r--r-- 1 ana vendas 1024 Dec 10 20:00 relatorio.txt
```

### 1. Mudando apenas o dono

Para transferir o arquivo para o usuário `pedro`:

```bash
$ sudo chown pedro relatorio.txt

$ ls -l relatorio.txt
-rw-r--r-- 1 pedro vendas 1024 Dec 10 20:00 relatorio.txt
```

### 2. Mudando o dono e o grupo de uma vez

Para transferir o arquivo para o usuário `pedro` e também para o grupo `marketing`:

```bash
$ sudo chown pedro:marketing relatorio.txt

$ ls -l relatorio.txt
-rw-r--r-- 1 pedro marketing 1024 Dec 10 20:00 relatorio.txt
```

### 3. Mudando apenas o grupo

Se você omitir o nome do novo dono e colocar dois pontos (`:`) antes do nome do grupo, você muda apenas o grupo.

```bash
$ sudo chown :engenharia relatorio.txt

$ ls -l relatorio.txt
-rw-r--r-- 1 pedro engenharia 1024 Dec 10 20:00 relatorio.txt
```

### 4. Mudando a propriedade de um diretório recursivamente (`-R`)

Assim como no `chmod` ou `rm`, a opção `-R` (**R**ecursive) aplica a mudança de propriedade a um diretório e a **todos** os arquivos e subdiretórios dentro dele.

```bash
# Muda o dono de toda a pasta "projetos/" e seu conteúdo para o usuário "julia"
$ sudo chown -R julia projetos/
```
Esta opção é extremamente útil para transferir a posse de um projeto inteiro de um usuário para outro.
