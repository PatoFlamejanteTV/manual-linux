# mkdir

O comando `mkdir` (abreviação de **m**a**k**e **dir**ectory) é usado para criar um ou mais diretórios (pastas).

É um dos comandos mais básicos e essenciais para organizar seus arquivos no sistema.

## Exemplo Simples

Para criar um único diretório, basta fornecer o nome dele como argumento.

```bash
# Cria uma pasta chamada "Musicas"
$ mkdir Musicas

# Verifica se a pasta foi criada
$ ls
Musicas/  Documentos/  Videos/
```

## Criando vários diretórios de uma vez

Você pode criar múltiplos diretórios ao mesmo tempo, separando os nomes com espaços.

```bash
$ mkdir Imagens Ferramentas Jogos

$ ls
Musicas/  Documentos/  Videos/  Imagens/  Ferramentas/  Jogos/
```

## Criando diretórios aninhados com `-p`

Às vezes, você quer criar uma estrutura de pastas, como `Aulas/Programacao/Projeto1`. Se você tentar `mkdir Aulas/Programacao/Projeto1` e a pasta `Aulas` ou `Programacao` não existirem, o comando dará um erro.

A opção `-p` (**p**arents) resolve isso. Ela instrui o `mkdir` a criar todos os diretórios "pais" necessários no caminho.

```bash
# Este comando cria "Aulas", depois "Programacao" dentro dela, e finalmente "Projeto1"
$ mkdir -p Aulas/Programacao/Projeto1

# Verificando a estrutura criada
$ ls -R Aulas/
Aulas/:
Programacao/

Aulas/Programacao:
Projeto1/
```
A opção `-p` é uma mão na roda para evitar a criação manual de cada nível de diretório.

## Teste em Terminal Real

```bash
$ mkdir test_dir_xyz
mkdir: foi criado o diretório 'test_dir_xyz'

$ ls -ld test_dir_xyz
drwxrwxr-x 2 quack quack 4096 jan 11 15:23 test_dir_xyz
```
