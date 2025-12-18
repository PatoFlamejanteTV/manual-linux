# Senhas e Segurança

As senhas são a primeira linha de defesa no Linux. O sistema utiliza
criptografia forte para armazenar senhas, garantindo que elas não sejam salvas
em texto plano.

## Armazenamento de Senhas

No Linux, as informações dos usuários ficam em `/etc/passwd` (que é legível por
todos), mas as senhas (hash) ficam armazenadas de forma segura em
`/etc/shadow`.

O arquivo `/etc/shadow` só pode ser lido pelo usuário **root**.

```bash
$ cat /etc/shadow
cat: /etc/shadow: Permissão negada

$ sudo cat /etc/shadow
root:$6$S.gT5...:19000:0:99999:7:::
usuario:$6$K9dL...:19000:0:99999:7:::
```

Cada linha contém o hash da senha, data da última alteração e políticas de
expiração.

## Boas Práticas

1. **Senhas Fortes**: Use uma mistura de letras maiúsculas, minúsculas,
   números e símbolos. Evite palavras comuns.
2. **Não Reutilize Senhas**: Use senhas diferentes para serviços diferentes.
3. **Gerenciadores de Senha**: Utilize ferramentas como `keepassxc` ou `pass`
   para gerenciar suas senhas de forma segura.

## Alterando sua Senha

Para alterar sua própria senha, use o comando `passwd`:

```bash
$ passwd
Changing password for usuario.
Current password:
New password:
Retype new password:
passwd: password updated successfully
```

Como administrador, você pode alterar a senha de outros usuários:

```bash
$ sudo passwd outro_usuario
passwd: password updated successfully
```
