# chmod

O comando `chmod` (abreviação de **ch**ange **mod**e) é usado para alterar as permissões de acesso a arquivos e diretórios no Linux.

Ele define quem pode **ler**, **escrever** ou **executar** um arquivo. Esse conceito de permissões é um dos pilares da segurança em sistemas baseados em Unix.

## O caso de uso mais comum: Tornar um script executável

Um dos usos mais frequentes do `chmod` é dar permissão de execução a um script que você acabou de criar ou baixar.

```bash
# 1. Crie um script de exemplo
$ echo '#!/bin/bash' > meu_script.sh
$ echo 'echo "Olá, mundo!"' >> meu_script.sh

# 2. Veja as permissões atuais. Note que não há "x" (execução)
$ ls -l meu_script.sh
-rw-rw-r-- 1 jules jules 35 Dec 10 18:00 meu_script.sh

# 3. Tente executá-lo (vai dar erro)
$ ./meu_script.sh
bash: ./meu_script.sh: Permission denied

# 4. Adicione a permissão de execução para o usuário dono do arquivo ("u+x")
$ chmod u+x meu_script.sh

# 5. Verifique as novas permissões (agora tem "x")
$ ls -l meu_script.sh
-rwx-rw-r-- 1 jules jules 35 Dec 10 18:00 meu_script.sh

# 6. Execute o script com sucesso
$ ./meu_script.sh
Olá, mundo!
```

## Entendendo as permissões

Existem duas formas principais de usar o `chmod`:

### 1. Modo Simbólico (letras)

É a forma mais intuitiva, como no exemplo acima (`u+x`):
*   **Para quem?** `u` (usuário dono), `g` (grupo), `o` (outros), `a` (todos).
*   **O que fazer?** `+` (adicionar), `-` (remover), `=` (definir exatamente).
*   **Qual permissão?** `r` (leitura), `w` (escrita), `x` (execução).

**Exemplos:**
*   `chmod g-w arquivo.txt`: Remove a permissão de escrita para o grupo.
*   `chmod a+r arquivo.txt`: Adiciona permissão de leitura para todos.
*   `chmod u=rwx,go=r script.sh`: Define permissões exatas: dono pode ler, escrever e executar; grupo e outros podem apenas ler.

### 2. Modo Octal (números)

É a forma mais rápida, mas menos intuitiva. Cada permissão tem um valor numérico:
*   `r` (leitura) = 4
*   `w` (escrita) = 2
*   `x` (execução) = 1

Você soma os valores para cada categoria (dono, grupo, outros).
*   **7**: `4+2+1` (ler, escrever, executar)
*   **6**: `4+2` (ler, escrever)
*   **5**: `4+1` (ler, executar)
*   **4**: `4` (apenas ler)

O famoso `chmod 755 script.sh` significa:
*   **7** para o dono (`rwx`)
*   **5** para o grupo (`r-x`)
*   **5** para outros (`r-x`)

Ambas as formas funcionam, use a que você se sentir mais confortável!
