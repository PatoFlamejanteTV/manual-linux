# VirtualBox

**Oracle VM VirtualBox** é um pacote de software de virtualização para
arquiteturas x86 e x86-64. É um hypervisor do **Tipo 2**, o que significa que
ele roda sobre um sistema operacional existente (como Linux, Windows ou macOS).

## Características

* **Multiplataforma**: Pode ser instalado em Linux, Windows, macOS e Solaris.
* **Gratuito e Open Source**: A versão base é lançada sob a licença GPLv2.
* **Fácil de usar**: Possui uma interface gráfica amigável para criação e
  gerenciamento de máquinas virtuais.
* **Snapshots**: Permite salvar o estado da máquina virtual em um determinado
  momento e restaurá-lo posteriormente.
* **Guest Additions**: Pacote de drivers e aplicativos de sistema que melhoram
  o desempenho e a usabilidade (ex: compartilhamento de área de transferência,
  pastas compartilhadas).

## Instalação (Exemplo no Debian/Ubuntu)

```bash
sudo apt update
sudo apt install virtualbox
```

## Extension Pack

Para suporte a dispositivos USB 2.0/3.0, criptografia de disco e boot PXE para
placas Intel, é necessário instalar o "VirtualBox Extension Pack" (proprietário).
