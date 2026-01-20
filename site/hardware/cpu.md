# CPU

A CPU (Unidade Central de Processamento) é o cérebro do computador. No Linux,
você pode ver informações sobre ela de várias formas.

Um comando comum para ver detalhes da CPU é:

```bash
$ lscpu
```

Ou olhando o arquivo `/proc/cpuinfo`.

## Arquiteturas

Cada modelo de CPU tem sua própria arquitetura, as mais comuns são AMD64 (Intel64, x64, etc.), 32 bits, e as arquiteturas ARM.

## Exemplos

```
~ $ lscpu
Architecture:             aarch64
  CPU op-mode(s):         32-bit, 64-bit
  Byte Order:             Little Endian
CPU(s):                   8
  On-line CPU(s) list:    0-7
Vendor ID:                ARM
  Model name:             Cortex-A55
    Model:                0
    Thread(s) per core:   1
    Core(s) per socket:   6
    Socket(s):            1
    Stepping:             r1p0
    CPU(s) scaling MHz:   53%
    CPU max MHz:          1800.0000
    CPU min MHz:          500.0000
    BogoMIPS:             26.00
    Flags:                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
  Model name:             Cortex-A75
    Model:                1
    Thread(s) per core:   1
    Core(s) per socket:   2
    Socket(s):            1
    Stepping:             r3p1
    CPU(s) scaling MHz:   81%
    CPU max MHz:          2000.0000
    CPU min MHz:          850.0000
    BogoMIPS:             26.00
    Flags:                fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm lrcpc dcpop asimddp
Vulnerabilities:
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Not affected
  Spectre v1:             Mitigation; __user pointer sanitization
  Spectre v2:             Vulnerable: Unprivileged eBPF enabled
  Srbds:                  Not affected
  Tsx async abort:        Not affected
~ $
```