# Root e Sudo

No Linux, o usuário **root** (também conhecido como superusuário) tem acesso
irrestrito a todo o sistema. Ele pode ler qualquer arquivo, instalar programas,
alterar configurações vitais e até mesmo apagar todo o sistema operacional.

## Por que não usar o Root o tempo todo?

Usar o sistema logado como root é perigoso por vários motivos:

1. **Risco de Danos**: Um comando errado pode destruir o sistema sem aviso.
2. **Segurança**: Se um programa malicioso for executado como root, ele terá
   controle total da máquina.
3. **Princípio do Menor Privilégio**: Usuários e programas devem ter apenas as
   permissões necessárias para realizar suas tarefas, e nada mais.

## O comando Sudo

O `sudo` (**S**uper**U**ser **DO**) permite que usuários comuns executem
comandos com privilégios de root de forma temporária e controlada.

Ao invés de logar como root, você usa sua própria conta e prefixa os comandos
administrativos com `sudo`.

```bash
# Tentando atualizar o sistema (vai falhar sem sudo)
$ apt update
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)

# Usando sudo (vai pedir sua senha de usuário)
$ sudo apt update
[sudo] senha para usuario:
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
...
```

O `sudo` registra todos os comandos executados, permitindo auditoria, e pode ser
configurado para dar acesso apenas a comandos específicos para certos usuários.
