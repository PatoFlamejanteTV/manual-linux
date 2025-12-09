# ps

O comando `ps` (abreviação de **p**rocess **s**tatus) é usado para tirar uma "foto" dos processos que estão rodando no sistema no momento em que é executado.

É uma ferramenta essencial para monitorar e gerenciar o que está acontecendo no seu Linux.

## Exemplo com `aux`

A forma mais comum de usar o `ps` é com as opções `aux`:
*   `a`: Mostra os processos de **t**odos os usuários.
*   `u`: Exibe informações detalhadas sobre cada processo (como usuário, uso de CPU/memória).
*   `x`: Inclui processos que não estão atrelados a um terminal (como serviços que rodam em segundo plano).

```bash
$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1 169524 12892 ?        Ss   10:00   0:02 /sbin/init
root           2  0.0  0.0      0     0 ?        S    10:00   0:00 [kthreadd]
...
jules     1234  0.4  1.2 654321 98765 ?        Sl   10:30   0:01 gedit
jules     5678  0.0  0.2 230428 19876 pts/0    Ss   11:00   0:00 bash
jules     9101  0.0  0.1 223880 10123 pts/0    R+   11:05   0:00 ps aux
```

**Entendendo as colunas principais:**

*   **USER**: O usuário que iniciou o processo.
*   **PID**: O **ID do Processo**, um número único para cada processo. Essencial para usar com o comando `kill`.
*   **%CPU**: A porcentagem de uso da CPU pelo processo.
*   **%MEM**: A porcentagem de uso da memória RAM.
*   **COMMAND**: O comando que iniciou o processo.

## Encontrando um processo específico

A saída do `ps aux` pode ser enorme. Para encontrar um processo específico, a melhor abordagem é combinar o `ps` com o `grep`. Por exemplo, para encontrar todos os processos relacionados ao `firefox`:

```bash
$ ps aux | grep firefox
jules    2345  4.5 10.2 1234567 876543 ?       Sl   10:45   1:30 /usr/lib/firefox/firefox
```
Isso filtra a lista e mostra apenas as linhas que contêm a palavra "firefox", facilitando a vida na hora de encontrar o PID de um programa.
