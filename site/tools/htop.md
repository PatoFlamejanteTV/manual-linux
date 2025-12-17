# htop

O `htop` é uma versão mais interativa e colorida do clássico `top`. Ele serve para monitorar os processos do sistema, uso de CPU, memória e swap.

Com ele você pode ver o que está consumindo recursos e matar processos travados facilmente.

```bash
$ htop
```

```

    0[                          0.0%]   4[                       offline]
    1[                       offline]   5[                       offline]
    2[                       offline]   6[                       offline]
    3[                       offline]   7[                       offline]
  Mem[|||||||||||||||||||4.00G/7.54G] Tasks: 2, 0 thr, 0 kthr; 1 running
  Swp[||||||              876M/5.50G] Load average: nan nan nan
                                      Uptime: (unknown)

  [Main] [I/O]
    PID USER       PRI  NI  VIRT   RES   SHR S  CPU%▽MEM%   TIME+  Command
  24695 u0_a502     10 -10 2117M  5376  4224 S   N/A  0.1  0:00.38 /data/da
  26787 u0_a502     10 -10 2135M  4608  3584 R   N/A  0.1  0:00.11 htop













F1Help  F2Setup F3SearchF4FilterF5Tree  F6SortByF7Nice -F8Nice +F9Kill  F10
```