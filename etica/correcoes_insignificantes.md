# Sobre "Erratas" que eu não ligo muito

## "O certo é GNU/Linux, e não só 'Linux'!"

Olha, pode até ser, principalmente se você está se referindo aos `coreutils` e outras ferramentas básicas do sistema. Mas hoje em dia, há vários planos para "aposentar" essas ferramentas, principalmente com a "Oxidação" (`Rustification`) do sistema.

Em outras palavras, o vovô GNU tá se aposentando e logo, logo vai voltar pra Savannah dele.

### E as alternativas?

Tem um monte de projetos novos. O próprio Ubuntu quer substituir os `coreutils` por uma versão escrita em Rust. Parece interessante no papel, mas qualquer mudança mínima pode dar um problemão em sistemas complexos.

De acordo com uma pesquisa rápida no Google sobre a "Rustificação do Ubuntu":

> O projeto da Canonical visa substituir componentes essenciais do Ubuntu, tradicionalmente escritos em C, por alternativas em Rust, uma linguagem mais segura.
>
> **Motivação:** A principal razão é a segurança. Rust elimina várias classes de vulnerabilidades de memória comuns em C.
>
> **Componentes:**
> *   `sudo-rs`: Uma substituição para o `sudo` clássico.
> *   `uutils`: Uma substituição para os `coreutils` (comandos como `ls`, `cat`, `sort`, etc.).
>
> **Cronograma:** A transição está ganhando força, com planos para implementação no Ubuntu 25.10 e consolidação no Ubuntu 26.04 LTS.

Então, sim, o nome "GNU" é importante, mas o cenário está sempre mudando.
