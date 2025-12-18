# DNS

**DNS** (Domain Name System) é um sistema hierárquico e distribuído de gestão
de nomes para computadores, serviços ou qualquer recurso conectado à Internet
ou a uma rede privada.

## Função principal

A principal função do DNS é traduzir nomes de domínio legíveis por humanos
(como `www.exemplo.com`) em endereços IP numéricos (como `192.0.2.1`) que os
computadores usam para se comunicar entre si.

## Tipos de registros comuns

* **A (Address)**: Mapeia um nome de host para um endereço IPv4.
* **AAAA**: Mapeia um nome de host para um endereço IPv6.
* **CNAME (Canonical Name)**: Cria um alias para outro nome de domínio.
* **MX (Mail Exchange)**: Especifica os servidores de e-mail para o domínio.
* **TXT**: Permite associar texto arbitrário a um nome de domínio (usado para
  verificação SPF, DKIM, etc.).
* **NS (Name Server)**: Indica os servidores DNS autoritativos para o domínio.

## Ferramentas de diagnóstico

No Linux, ferramentas comuns para interagir com o DNS incluem `dig`, `nslookup`
e `host`.

Exemplo de uso do `dig`:

```bash
dig exemplo.com
```

Exemplo para consultar um registro específico:

```bash
dig exemplo.com MX
```
