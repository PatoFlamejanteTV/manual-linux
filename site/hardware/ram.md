# RAM (Random Access Memory)

A Memória de Acesso Aleatório (RAM) é onde o computador armazena dados temporários que estão sendo usados ativamente pelos programas e pelo sistema operacional.

Diferente do disco rígido (HDD ou SSD), a RAM é volátil, o que significa que os dados são perdidos quando o computador é desligado. Ela é muito mais rápida que o armazenamento permanente.

## No Linux

O Linux gerencia a RAM de forma eficiente. Memória não usada é memória desperdiçada, então o Linux frequentemente usa RAM livre para cache de disco, acelerando o sistema.

Você pode ver o uso de RAM com o comando `free`:

```bash
$ free -h
```
