# AppArmor (Application Armor)

O AppArmor é um módulo de segurança do kernel Linux (LSM) que permite ao administrador restringir as capacidades de programas com perfis por programa.

## Funcionamento

Ele funciona associando perfis de segurança a executáveis.

- **Modo Enforce**: Bloqueia ações não permitidas e loga.
- **Modo Complain**: Apenas loga violações, sem bloquear.

## Comandos Básicos

Verificar status:

```bash
sudo apparmor_status
```

Colocar perfil em modo complain:

```bash
sudo aa-complain /caminho/do/binario
```

Colocar perfil em modo enforce:

```bash
sudo aa-enforce /caminho/do/binario
```

Os perfis geralmente ficam em `/etc/apparmor.d/`.
