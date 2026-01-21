# Kernel

O **Kernel** (núcleo) é a parte mais importante de um sistema operacional. Ele é o primeiro programa a ser carregado (após o [bootloader](bootloaders.md)) e permanece na memória o tempo todo.

Você pode pensar no kernel como o **maestro de uma orquestra**. Ele não toca os instrumentos (os aplicativos), mas diz a eles quando tocar, por quanto tempo e garante que não toquem uns sobre os outros.

## O que ele faz?

Ele atua como uma "ponte" entre o **Software** (seus programas, navegador, jogos) e o **Hardware** (processador, memória, disco, placa de vídeo).

### Principais Responsabilidades

1. **Gerenciamento de Processos:** Decide qual programa pode usar a CPU e por quanto tempo (escalonamento).
2. **Gerenciamento de Memória:** Aloca memória RAM para os programas e garante que um programa não invada a memória de outro.
3. **Drivers de Dispositivos:** Controla o hardware físico (mouse, teclado, placa de rede) através de *drivers*.
4. **Gerenciamento de Arquivos:** Permite que os aplicativos leiam e gravem arquivos no disco sem precisarem saber como o disco funciona fisicamente.

## Arquitetura: Monolítico vs Microkernel

O Linux é um **Kernel Monolítico**. Isso significa que todo o núcleo (gerenciamento de memória, drivers, sistema de arquivos) roda em um único espaço de memória grande e privilegiado (Kernel Space). Isso o torna extremamente rápido.

* **Monolítico (Linux):** Tudo roda junto. Performance alta. Se um driver falhar gravemente, pode derrubar o sistema todo (Kernel Panic).
* **Microkernel (Minix, GNU Hurd):** Apenas o mínimo absoluto roda no núcleo. Drivers e sistemas de arquivos rodam como processos separados. Mais estável (se um driver falhar, o kernel continua), mas geralmente mais lento devido à comunicação entre processos.

### Módulos do Kernel (LKM)

Embora seja monolítico, o Linux é **modular**. Isso significa que ele pode carregar e descarregar funcionalidades (drivers) sob demanda, sem precisar reiniciar. Esses pedaços de código são chamados de **Módulos do Kernel** (arquivos `.ko`).

## Verificando sua versão

Para saber qual versão do Linux seu sistema está rodando, você pode usar o comando:

```bash
uname -r
```

Exemplo de saída: `6.5.0-14-generic`
