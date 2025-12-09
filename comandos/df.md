# df

O comando `df` (abreviação de **d**isk **f**ree) é usado para exibir o espaço em disco disponível no sistema de arquivos. Ele mostra o espaço total, o espaço usado e o espaço livre de cada partição montada.

É uma ferramenta muito útil para monitorar o uso do disco e garantir que você não fique sem espaço.

## Exemplo com `-h`

A opção `-h` (**h**uman-readable) formata a saída em um formato mais legível para humanos (por exemplo, exibindo os tamanhos em KB, MB, GB em vez de blocos).

```bash
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           1.5G  2.4M  1.5G   1% /run
/dev/sda1        50G   15G   32G  32% /
tmpfs           7.7G     0  7.7G   0% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
/dev/sda15      105M  6.1M   99M   6% /boot/efi
tmpfs           1.5G  140K  1.5G   1% /run/user/1000
```

**Entendendo a saída:**

*   **Filesystem**: O nome da partição.
*   **Size**: O tamanho total da partição.
*   **Used**: O espaço em disco que está sendo usado.
*   **Avail**: O espaço em disco disponível.
*   **Use%**: A porcentagem de espaço em disco usado.
*   **Mounted on**: O ponto de montagem (onde a partição está acessível no sistema de arquivos).

No exemplo acima, a partição principal (`/dev/sda1`) tem 50GB de tamanho total, com 15GB em uso, deixando 32GB livres.
