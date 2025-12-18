# SQLite

O **SQLite** é uma biblioteca em linguagem C que implementa um banco de dados
SQL embutido. Diferente de outros sistemas de banco de dados, o SQLite não tem
um processo de servidor separado.

O banco de dados inteiro é armazenado em um único arquivo no disco, o que o
torna extremamente portátil e fácil de usar para aplicações menores,
desenvolvimento e testes.

## Instalação

Geralmente já vem instalado na maioria das distros. Caso contrário:

No Debian/Ubuntu:

```bash
sudo apt install sqlite3
```

No Fedora:

```bash
sudo dnf install sqlite
```

## Uso Básico

Para criar ou abrir um banco de dados:

```bash
sqlite3 meu_banco.db
```

Isso abrirá o prompt do SQLite onde você pode executar comandos SQL.
