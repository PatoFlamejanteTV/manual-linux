# ping

O comando `ping` é usado para testar a conectividade de rede entre dois dispositivos. Ele envia pacotes de dados para um endereço IP ou nome de domínio e mede o tempo que leva para receber uma resposta. É uma ferramenta essencial para diagnosticar problemas de rede.

## Exemplos

```bash
$ ping google.com
PING google.com (142.250.218.142) 56(84) bytes of data.
64 bytes from lax17s01-in-f14.1e100.net (142.250.218.142): icmp_seq=1 ttl=111 time=15.9 ms
64 bytes from lax17s01-in-f14.1e100.net (142.250.218.142): icmp_seq=2 ttl=111 time=16.2 ms
```

## Argumentos Suportados

O `ping` tem vários argumentos, mas alguns dos mais comuns são:

*   `-c <número>`: Envia um número específico de pacotes e para.
*   `-i <intervalo>`: Define o intervalo em segundos entre o envio de cada pacote.
*   `-W <timeout>`: Define o tempo de espera por uma resposta em segundos.

## Fontes

*   [Manual do `ping`](https://man7.org/linux/man-pages/man8/ping.8.html)

## BusyBox/Toybox

O comando `ping` está disponível tanto no BusyBox quanto no Toybox, sendo uma ferramenta de rede fundamental em ambos.
