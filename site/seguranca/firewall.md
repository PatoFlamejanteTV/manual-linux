# Firewall

Um firewall é uma ferramenta de segurança de rede que monitora e controla o
tráfego de entrada e saída com base em regras de segurança predeterminadas. Ele
atua como uma barreira entre uma rede interna confiável e uma rede externa não
confiável, como a Internet.

No Linux, a ferramenta mais comum e poderosa para gerenciar firewalls é o
`iptables` (ou seu sucessor `nftables`), que opera a nível de kernel. No
entanto, sua configuração pode ser complexa.

Para facilitar o uso, muitas distribuições (como o Ubuntu) vêm com o **UFW**
(Uncomplicated Firewall), que fornece uma interface amigável para o `iptables`.

## UFW (Uncomplicated Firewall)

O UFW foi projetado para ser fácil de usar, permitindo configurar um firewall
básico rapidamente.

### Comandos Básicos

Habilitar o firewall:

```bash
$ sudo ufw enable
Firewall is active and enabled on system startup
```

Verificar o status:

```bash
$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip
```

Permitir tráfego SSH (porta 22):

```bash
$ sudo ufw allow ssh
Rule added
Rule added (v6)
# Ou especificando a porta
$ sudo ufw allow 22
Rule added
Rule added (v6)
```

Bloquear tráfego de uma porta específica:

```bash
$ sudo ufw deny 80
Rule added
Rule added (v6)
```

Desabilitar o firewall:

```bash
$ sudo ufw disable
Firewall stopped and disabled on system startup
```

É importante ter cuidado ao habilitar o firewall remotamente (via SSH), pois se
você não permitir a porta SSH antes de habilitar, poderá perder o acesso à
máquina.
