# C

A linguagem C é fundamental para o ecossistema Linux. O próprio kernel do Linux
foi escrito (e continua sendo mantido) majoritariamente em C. É uma linguagem
compilada, de baixo nível, que oferece controle total sobre a memória e o
hardware.

Para compilar programas em C no Linux, geralmente usamos o compilador `gcc`
(GNU Compiler Collection).

## Exemplo de Código

Um arquivo `ola.c`:

```c
#include <stdio.h>

int main() {
    printf("Olá, Linux!\n");
    return 0;
}
```

## Compilando e Executando

```bash
$ gcc ola.c -o ola
$ ./ola
Olá, Linux!
```
