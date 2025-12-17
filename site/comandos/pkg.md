# `pkg`

No Linux, "`pkg`" se refere a pacotes de software, que são arquivos contendo um programa completo (executáveis, bibliotecas, configs) para facilitar instalação/remoção, e também pode se referir ao utilitário `pkg-config`, uma ferramenta para desenvolvedores que ajuda a encontrar informações de bibliotecas e dependências durante a compilação de outros programas, ou ainda a comandos específicos em alguns ambientes como o Termux (um wrapper para `apt`) ou o `Pacman` (do Arch Linux). 

```
╭─quack @ termux in ~
╰─❯ pkg
Usage: pkg [--check-mirror] command [arguments]

A tool for managing apt packages.                               --check-mirror forces a re-check of availability of mirrors

Commands:

  autoclean            - Remove all outdated packages from apt
                         cache.

  clean                - Remove all packages from apt cache.

  files <packages>     - Show all files installed by packages.

  install <packages>   - Install specified packages.

  list-all             - List all packages available in repositories.

  list-installed       - List installed packages.

  reinstall <packages> - Reinstall specified installed packages at the
                         latest version.

  search <query>       - Search package by query, for example by name or
                         description part.

  show <packages>      - Show basic metadata, such as dependencies.

  uninstall <packages> - Uninstall specified packages. Configuration files
                         will be left intact.

  upgrade              - Upgrade all installed packages to the latest
                         version.

  update               - Update apt databases from configured
                         repositories.

╭─quack @ termux in ~
╰─✗
```