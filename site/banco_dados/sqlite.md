# SQLite

O SQLite é uma biblioteca em linguagem C que implementa um banco de dados SQL
embutido. Ao contrário da maioria dos outros bancos de dados SQL, o SQLite não
tem um processo de servidor separado. Ele lê e escreve diretamente em arquivos
de disco comuns.

## Instalação

Geralmente já vem instalado em muitas distros Linux. Caso não esteja:

No Debian/Ubuntu:

```bash
sudo apt install sqlite3
```

No Arch Linux:

```bash
sudo pacman -S sqlite
```

## Uso Básico

Para criar ou abrir um banco de dados, basta passar o nome do arquivo para o
comando `sqlite3`:

```bash
sqlite3 dados.db
```

Isso abrirá o prompt interativo do SQLite.

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
