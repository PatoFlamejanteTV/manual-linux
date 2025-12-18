# Virtualização

**Virtualização** é o processo de criar uma representação baseada em software (ou
virtual) de algo, em vez de uma física. A virtualização pode ser aplicada a
aplicativos, servidores, armazenamento e redes e é a maneira mais eficaz de
reduzir as despesas de TI e aumentar a eficiência e a agilidade para empresas
de todos os tamanhos.

## Como funciona

A virtualização depende de um software para simular a funcionalidade do
hardware e criar um sistema de computador virtual. Isso permite que as
organizações de TI executem mais de um sistema virtual — e vários sistemas
operacionais e aplicativos — em um único servidor. As economias de escala e a
maior eficiência resultantes são fundamentais.

## Hypervisors

O software que permite a virtualização é chamado de **Hypervisor**. Existem
dois tipos principais:

* **Tipo 1 (Bare Metal)**: Executa diretamente no hardware do host para
  controlar o hardware e gerenciar sistemas operacionais convidados.
  Exemplos: KVM, Xen, ESXi.

* **Tipo 2 (Hosted)**: Executa como um software em um sistema operacional
  convencional. Exemplos: VirtualBox, VMware Workstation.

## Benefícios

* **Consolidação de servidores**: Executar múltiplas máquinas virtuais em um
  único servidor físico.
* **Isolamento**: Cada máquina virtual é isolada das outras.
* **Flexibilidade**: Fácil criação e destruição de ambientes de teste.
