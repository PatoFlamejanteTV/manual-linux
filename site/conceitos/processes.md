# Processos

Um processo é um programa em execução, assim como em outros sistemas, podem haver diversos em segundo plano, como daemons e apĺicativos em segundo plano.

## Comandos relacionados

### `ps`

Lista os processos em execução.

```
➜  manual-linux git:(main) ✗ ps   
    PID TTY          TIME CMD
  91060 pts/2    00:00:00 zsh
  91992 pts/2    00:00:00 ps
➜  manual-linux git:(main) ✗ 

```

### `kill`

Termina um processo.

```
➜  manual-linux git:(main) ✗ kill --help
kill: unknown signal: SIG-HELP
kill: type kill -l for a list of signals
➜  manual-linux git:(main) ✗ kill -l    
HUP INT QUIT ILL TRAP IOT BUS FPE KILL USR1 SEGV USR2 PIPE ALRM TERM STKFLT CHLD CONT STOP TSTP TTIN TTOU URG XCPU XFSZ VTALRM PROF WINCH POLL PWR SYS
➜  manual-linux git:(main) ✗ 

```

### `top`

Exibe os processos em tempo real.

```
top - 18:39:23 up  2:54,  1 user,  load average: 1,02, 1,57, 1,32
Tasks: 314 total,   1 running, 310 sleeping,   0 stopped,   3 zombie
%Cpu(s):  1,3 us,  0,9 sy,  0,0 ni, 97,3 id,  0,4 wa,  0,0 hi,  0,0 si,  0,0 st 
MiB Mem :  15874,2 total,   1555,0 free,   4757,2 used,  10329,5 buff/cache     
MiB Swap:      0,0 total,      0,0 free,      0,0 used.  11117,0 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND  
  89284 quack     20   0 4813680 269056  79356 S   3,7   1,7   0:23.28 languag+ 
  89853 quack     20   0 4804708 180580  75476 S   3,7   1,1   0:09.27 languag+ 
   1540 quack     20   0 4734784 315044 128808 S   2,7   1,9  11:49.70 cinnamon 
  89495 quack     20   0 1408,0g 199812 106272 S   2,7   1,2   0:58.29 antigra+ 
  87308 quack     20   0   32,6g 171968 114468 S   2,3   1,1   0:36.49 antigra+ 
   1073 root      20   0  638736 159480  71960 S   2,0   1,0   6:20.99 Xorg     
  91049 quack     20   0  695096  43400  35112 S   1,3   0,3   0:00.70 gnome-t+ 
  87340 quack     20   0 1411,3g 454660 123376 S   1,0   2,8   1:23.62 antigra+ 
  89011 quack     20   0 1393,6g 339012  91264 S   1,0   2,1   0:19.73 antigra+ 
  87270 quack     20   0 1393,9g 230712 142956 S   0,7   1,4   0:17.61 antigra+ 
  89524 quack     20   0 1393,6g 216408  89428 S   0,7   1,3   0:08.56 antigra+ 
  91741 quack     20   0   20084   6008   3796 R   0,7   0,0   0:00.15 top      
    762 root      20   0  258688  14780  12576 S   0,3   0,1   0:12.56 touchegg 
   1409 quack     20   0  236148   8276   7436 S   0,3   0,1   0:02.83 at-spi2+ 
   2005 quack     20   0 1393,9g 233344 143924 S   0,3   1,4   0:57.93 antigra+ 
   3058 quack     20   0 1393,7g 118896  80756 S   0,3   0,7   0:28.16 antigra+ 
  87488 quack     20   0 1393,7g 119744  81208 S   0,3   0,7   0:02.94 antigra+ 


```
