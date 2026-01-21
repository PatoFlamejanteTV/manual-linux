# Auditoria de Sistema (Auditd)

O `auditd` é o daemon de auditoria do Linux. Ele registra eventos de segurança detalhados no kernel.

## Instalação

Geralmente via pacote `audit` ou `auditd`.

## Configuração

As regras ficam em `/etc/audit/audit.rules` ou `/etc/audit/rules.d/`.

## Exemplos de Regras

Monitorar acesso (leitura/escrita) a um arquivo sensível:

```bash
auditctl -w /etc/passwd -p wa -k passwd_changes
```

- `-w`: Arquivo a monitorar.
- `-p`: Permissões (w=write, a=attribute change).
- `-k`: Chave para facilitar busca nos logs.

## Pesquisando Logs

Use o comando `ausearch`:

```bash
ausearch -k passwd_changes
```

Para relatórios:

```bash
aureport
```
