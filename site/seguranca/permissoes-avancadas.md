# Permissões Avançadas

Além do `rwx` (Leitura, Escrita, Execução) padrão, o Linux possui permissões especiais e Listas de Controle de Acesso (ACLs).

## Bits Especiais

### SUID (Set User ID)

Permite que um arquivo seja executado com as permissões do dono do arquivo, não do usuário que o executa.
Exemplo: `passwd`.

```bash
chmod u+s arquivo
```

### SGID (Set Group ID)

Em arquivos: similar ao SUID, mas para o grupo.
Em diretórios: novos arquivos criados herdam o grupo do diretório, não do usuário criador.

```bash
chmod g+s diretorio
```

### Sticky Bit

Em diretórios (como `/tmp`), impede que usuários apaguem arquivos de outros usuários.

```bash
chmod +t /tmp
```

## ACLs (Access Control Lists)

Permite permissões granulares para múltiplos usuários.

```bash
# Adicionar permissão
setfacl -m u:joao:rw arquivo

# Ver permissões
getfacl arquivo
```
