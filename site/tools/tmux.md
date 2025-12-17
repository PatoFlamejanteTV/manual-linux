# TMux, `tmux`, _(não confundir com Termux)_

É meio complexo de explicar ele, é praticamente uma ferramenta que permite você executar mini-terminais dentro do seu terminal atual.

```
╭─quack @ termux in ~
╰─❯ tmux                                                                   [exited]
╭─quack @ termux in ~ took 2m51s277ms
╰─❯ tmux --help
tmux: unknown option -- -
usage: tmux [-2CDhlNuVv] [-c shell-command] [-f file] [-L socket-name]
            [-S socket-path] [-T features] [command [flags]]
╭─quack @ termux in ~
╰─✗
```

## Exemplos

```
╭─quack @ termux in ~                                             │╭─quack @ termux in ~
╰─❯ fastfetch                                                     │╰─❯ neofetch
         -o          o-             u0_a502@localhost             │         -o          o-            u0_a502@localhost
          +hydNNNNdyh+              -----------------             │          +hydNNNNdyh+             -----------------
        +mMMMMMMMMMMMMm+            OS: Android REL 15 aarch64    │        +mMMMMMMMMMMMMm+           OS: Android 15 aarch64
      `dMMm:NMMMMMMN:mMMd`          Host: realme RMX3710          │      `dMMm:NMMMMMMN:mMMd`         Host: realme RMX3710
      hMMMMMMMMMMMMMMMMMMh          Kernel: Linux 6.6.82-android1k│      hMMMMMMMMMMMMMMMMMMh         Kernel: 6.6.82-android15-8-o-
  ..  yyyyyyyyyyyyyyyyyyyy  ..      Uptime: 3 days, 22 hours, 38 s│  ..  yyyyyyyyyyyyyyyyyyyy  ..     Uptime: 3 days, 22 hours, 38
.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.    Packages: 385 (dpkg)          │.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.   Packages: 385 (dpkg), 1 (pkg)
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:    Shell: bash 5.3.3             │:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   Shell: bash 5.3.3
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:    WM: WindowManager (SurfaceFli)│:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   Terminal: tmux
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:    Terminal: tmux 3.6            │:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   CPU: (8) @ 1.800GHz
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:    CPU: MT6769H (8) @ 2.00 GHz   │:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:   Memory: 4100MiB / 7723MiB
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-    GPU: Mesa llvmpipe (LLVM 21.1)│-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+     Memory: 4.41 GiB / 7.54 GiB ()│ +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm          Swap: 1.01 GiB / 5.50 GiB (18)│      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`          Disk (/): 727.92 MiB / 727.92]│      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM              Disk (/storage/emulated): 217e│          MMMMo  oMMMM
          MMMMo  oMMMM              Local IP (wlan0): 192.168.0.14│          MMMMo  oMMMM
          oNMm-  -mMNs              Locale: en_US.UTF-8           │          oNMm-  -mMNs                                                                                                             │                                                                                                                                   │╭─quack @ termux in ~
                                                                  │╰─❯
╭─quack @ termux in ~                                             │
╰─❯                                                               │
                                                                  │                                                                                                                                   │
                                                                  │
                                                                  │                                                                                                                                   │
                                                                  │
                                                                  │
                                                                  │                                                                                                                                   │                                                                                                                                   │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
                                                                  │
[0] 0:bash*                                                                                              "localhost" 12:24 17-Dec-25
```