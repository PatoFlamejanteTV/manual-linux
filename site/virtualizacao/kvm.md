# KVM (Kernel-based Virtual Machine)

**KVM** (Kernel-based Virtual Machine) é uma solução de virtualização completa
para Linux em hardware x86 contendo extensões de virtualização (Intel VT ou
AMD-V).

## Como funciona

O KVM transforma o kernel do Linux em um hypervisor do **Tipo 1** (Bare Metal).
Ao usar o KVM, o próprio kernel do Linux gerencia o acesso das máquinas
virtuais aos recursos de hardware. Cada máquina virtual é implementada como um
processo regular do Linux, agendado pelo agendador de processos padrão, com
hardware virtual dedicado como placa de rede, adaptador gráfico, CPU(s),
memória e discos.

## Requisitos

Para usar o KVM, seu processador deve suportar virtualização de hardware.
Você pode verificar isso com o seguinte comando:

```bash
lscpu | grep Virtualization
```

Ou verificando as flags da CPU:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

Se o resultado for maior que 0, seu processador suporta virtualização.

## Ferramentas relacionadas

Embora o KVM forneça a capacidade de virtualização, ele geralmente não é usado
sozinho. Ferramentas comuns usadas com KVM incluem:

* **QEMU**: Usado para emulação de hardware e interação com o KVM.
* **Libvirt**: Uma API e daemon para gerenciar plataformas de virtualização.
* **Virt-Manager**: Uma interface gráfica para gerenciar máquinas virtuais
  via Libvirt.
