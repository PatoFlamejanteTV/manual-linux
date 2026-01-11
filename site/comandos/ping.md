# ping

O **ping** é usado para testar a conectividade com outro host na rede. Ele envia pacotes ICMP ECHO_REQUEST.

## Uso Básico

Testar conexão com um site:

```bash
ping google.com
```

## Limitar número de pacotes

Enviar apenas 5 pacotes:

```bash
ping -c 5 google.com
```

## Intervalo

Alterar o intervalo entre pacotes (em segundos):

```bash
ping -i 2 google.com
```
