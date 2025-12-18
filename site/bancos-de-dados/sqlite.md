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

No Arch Linux:

```bash
sudo pacman -S sqlite
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

### Comandos do Shell SQLite

Os comandos internos do SQLite (que não são SQL) começam com um ponto.

Ver ajuda:

```text
.help
```

Listar tabelas:

```text
.tables
```

Sair do prompt:

```text
.quit
```

### SQL

Você pode executar comandos SQL normais dentro do prompt (lembre-se do ponto e
vírgula `;` no final):

```sql
CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT);
INSERT INTO usuarios (nome) VALUES ('Alice');
SELECT * FROM usuarios;
```
