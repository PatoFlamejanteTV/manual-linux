# Containers

**Containers** são uma forma de virtualização no nível do sistema operacional.
Diferente das máquinas virtuais (VMs), que virtualizam o hardware, os
containers virtualizam o sistema operacional.

## Containers vs Máquinas Virtuais

* **Máquinas Virtuais**: Cada VM possui seu próprio sistema operacional
  completo (kernel + userspace), o que consome mais recursos (RAM, CPU, Disco)
  e leva mais tempo para iniciar.
* **Containers**: Compartilham o kernel do sistema operacional host, mas
  mantêm o espaço do usuário (userspace) isolado (bibliotecas, executáveis).
  São muito mais leves e iniciam quase instantaneamente.

## Tecnologias comuns

* **LXC (Linux Containers)**: Fornece containers de sistema, que se comportam
  como máquinas virtuais leves.
* **Docker**: Popularizou o uso de containers de aplicação, facilitando o
  empacotamento e distribuição de software. Veja mais em [Docker](/tools/docker).
* **Podman**: Uma alternativa ao Docker, daemonless e rootless, compatível com
  imagens OCI (Open Container Initiative).

## Vantagens

* **Leveza**: Menor consumo de recursos.
* **Portabilidade**: "Build once, run anywhere" (especialmente com Docker).
* **Escalabilidade**: Fácil de escalar horizontalmente.
