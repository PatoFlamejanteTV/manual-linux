# Init

O **init** (abreviação de *initialization*) é o primeiro processo que o kernel do Linux inicia quando o sistema é inicializado. Ele tem o ID de processo (PID) 1 e é o ancestral de todos os outros processos do sistema.

## Funções do init

A principal responsabilidade do processo `init` é colocar o sistema em um estado funcional. Suas funções incluem:

* **Iniciar serviços do sistema:** O `init` é responsável por iniciar todos os daemons e serviços essenciais em segundo plano, como rede, log do sistema e serviços de interface gráfica.
* **Gerenciar processos do sistema:** O `init` supervisiona todos os outros processos. Se um processo "órfão" (um processo cujo pai terminou) for deixado no sistema, o `init` o adota e se torna seu pai.

## Sistemas de Init

Ao longo dos anos, diferentes sistemas de `init` foram desenvolvidos para o Linux. Os mais conhecidos são:

* **SysVinit:** O sistema de `init` tradicional, baseado em scripts de shell localizados em `/etc/init.d`. Ele usa "runlevels" para determinar quais serviços iniciar.
* **Upstart:** Um sistema de `init` baseado em eventos, desenvolvido pela Canonical para o Ubuntu. Ele foi projetado para ser mais rápido e flexível que o SysVinit.
* **systemd:** O sistema de `init` mais moderno e amplamente adotado, usado pela maioria das distribuições Linux atuais (incluindo Debian, Ubuntu, Fedora e Arch Linux). O `systemd` gerencia não apenas a inicialização de serviços, mas também o log do sistema, a rede, os dispositivos e muito mais.

## Interagindo com o systemd

Como o `systemd` é o padrão na maioria dos sistemas modernos, é útil saber como interagir com ele. O principal comando para controlar o `systemd` é o `systemctl`.

### Exemplos de `systemctl`

```bash
# Iniciar um serviço
$ sudo systemctl start apache2.service

# Parar um serviço
$ sudo systemctl stop apache2.service

# Reiniciar um serviço
$ sudo systemctl restart apache2.service

# Verificar o status de um serviço
$ sudo systemctl status apache2.service

# Habilitar um serviço para iniciar no boot
$ sudo systemctl enable apache2.service

# Desabilitar um serviço de iniciar no boot
$ sudo systemctl disable apache2.service
```
