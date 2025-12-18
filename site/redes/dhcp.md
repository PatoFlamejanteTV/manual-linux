# DHCP

**DHCP** (Dynamic Host Configuration Protocol) é um protocolo de rede
cliente/servidor que fornece automaticamente um host IP (Internet Protocol)
com seu endereço IP e outras informações de configuração relacionadas, como a
máscara de sub-rede e o gateway padrão.

## Como funciona

O processo de DHCP envolve quatro etapas principais (DORA):

1. **Discover**: O cliente envia um pacote de transmissão (broadcast)
   procurando por servidores DHCP disponíveis.
2. **Offer**: O servidor DHCP responde com uma oferta de configuração IP.
3. **Request**: O cliente solicita o endereço IP oferecido.
4. **Acknowledge**: O servidor confirma a solicitação e o cliente configura a
   interface de rede.

## Vantagens

* **Automação**: Elimina a necessidade de configuração manual de IP em cada
  dispositivo.
* **Gerenciamento centralizado**: Facilita a alteração de parâmetros de rede
  para todos os dispositivos.
* **Eficiência**: Reutiliza endereços IP que não estão mais em uso.

## Arquivos de configuração comuns

No Linux, o cliente DHCP geralmente é o `dhclient` ou parte do
`NetworkManager` ou `systemd-networkd`.

Exemplo de renovação de IP com `dhclient`:

```bash
sudo dhclient -r  # Libera o IP atual
sudo dhclient     # Solicita um novo IP
```
