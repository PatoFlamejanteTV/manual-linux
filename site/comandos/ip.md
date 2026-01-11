# ip

O comando **ip** (parte do pacote iproute2) é usado para manipular rotas, dispositivos de rede, interfaces e túneis. Ele substitui o antigo `ifconfig`.

## Visualizar endereços IP

Mostrar todos os endereços IP:

```bash
ip addr show
```

## Visualizar rotas

Mostrar a tabela de roteamento:

```bash
ip route show
```

## Ativar/Desativar interface

```bash
sudo ip link set eth0 up
sudo ip link set eth0 down
```
