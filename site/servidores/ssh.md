# SSH

O **SSH** (Secure Shell) é a porta de entrada pro seu servidor. É com ele que
você acessa o terminal da máquina remotamente de forma segura e criptografada.

Sem ele, você teria que plugar um monitor e teclado no servidor lá no data
center (o que não é nada prático, né?).

## Instalação

Geralmente já vem instalado, mas se precisar:

No Debian/Ubuntu:

```bash
sudo apt update
sudo apt install openssh-server
```

## Conectando

Do seu computador, você usa o comando `ssh`:

```bash
ssh usuario@ip-do-servidor
```

## Configuração e Segurança

O arquivo mestre é o `/etc/ssh/sshd_config`.

Dicas de segurança básicas:

1. **Mude a porta padrão (22)**: Evita muitos bots chatos tentando entrar.
2. **Desabilite root login**: `PermitRootLogin no`.
3. **Use chaves SSH**: É bem mais seguro que senha.

Sempre que mexer nesse arquivo, reinicie o serviço pra valer:

```bash
sudo systemctl restart ssh
```
