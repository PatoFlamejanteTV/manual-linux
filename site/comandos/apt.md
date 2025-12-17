# `apt`

"apt" (_**A**dvanced **P**ackage **T**ool_) é um gerenciador de pacotes para distribuições Linux como Debian e Ubuntu, usado para instalar, remover e atualizar software por meio da linha de comando.

Ele gerencia dependências automaticamente e é uma alternativa mais moderna e interativa ao comando `apt-get`, oferecendo recursos como barras de progresso coloridas. Para usar a maioria dos comandos, é necessário ter privilégios de administrador, geralmente usando `sudo`. 

```
╭─quack @ termux in ~
╰─❯ apt
apt 2.8.1 (aarch64)
Usage: apt [options] command

apt is a commandline package manager and provides commands for
searching and managing as well as querying information about packages.
It provides the same functionality as the specialized APT tools,
like apt-get and apt-cache, but enables options more suitable for
interactive use by default.

Most used commands:
  list - list packages based on package names
  search - search in package descriptions
  show - show package details
  install - install packages
  reinstall - reinstall packages
  remove - remove packages
  autoremove - automatically remove all unused packages
  update - update list of available packages
  upgrade - upgrade the system by installing/upgrading packages
  full-upgrade - upgrade the system by removing/installing/upgrading packages
  edit-sources - edit the source information file
  satisfy - satisfy dependency strings

See apt(8) for more information about the available commands.
Configuration options and syntax is detailed in apt.conf(5).
Information about how to configure sources can be found in sources.list(5).
Package and version choices can be expressed via apt_preferences(5).
Security details are available in apt-secure(8).
                                        This APT has Super Cow Powers.
╭─quack @ termux in ~
╰─✗
```