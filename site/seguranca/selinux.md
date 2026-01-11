# SELinux

Security-Enhanced Linux (SELinux) é uma arquitetura de segurança para sistemas Linux que permite aos administradores ter mais controle sobre quem pode acessar o sistema.

## Modos

- **Enforcing**: Políticas de segurança são aplicadas.
- **Permissive**: Imprime avisos em vez de aplicar.
- **Disabled**: Desligado.

## Checar status

```bash
sestatus
```

## Alterar modo temporariamente

```bash
sudo setenforce 0  # Permissive
sudo setenforce 1  # Enforcing
```
