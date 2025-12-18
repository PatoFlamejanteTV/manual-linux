# QEMU

**QEMU** (Quick Emulator) é um emulador e virtualizador de máquina genérico e
de código aberto.

## Modos de operação

O QEMU pode operar em dois modos principais:

* **Emulação de sistema completo**: O QEMU emula uma máquina completa (CPU e
  periféricos), permitindo rodar sistemas operacionais feitos para uma
  arquitetura (ex: ARM) em outra (ex: x86).

* **Emulação de modo de usuário**: O QEMU pode rodar processos compilados
  para uma CPU em outra CPU.

## Relação com KVM

Quando usado em conjunto com o **KVM** (Kernel-based Virtual Machine), o QEMU
pode executar o código do sistema convidado diretamente no hardware do host,
atingindo desempenho próximo ao nativo.

Neste cenário (QEMU + KVM), o KVM atua como o hypervisor (gerenciando a CPU
e a memória), enquanto o QEMU emula os dispositivos de hardware (discos,
rede, USB, etc.) para a máquina virtual.

## Uso básico

Para criar uma imagem de disco:

```bash
qemu-img create -f qcow2 disco.qcow2 10G
```

Para iniciar uma máquina virtual (com KVM habilitado):

```bash
qemu-system-x86_64 -enable-kvm -hda disco.qcow2 -m 2G -cdrom instalador.iso
```
