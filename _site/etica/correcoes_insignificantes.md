# Erratas inúteis que eu não irei corrigir.

## "O certo é GNU/Linux ao invés de só "Linux"

Pode até ser em alguns casos, caso você esteja principalmente se referindo ao `coreutils` e outras ferramentas básicas e fundamentais para o funcionamento, mas hoje em dia há diversos planos para "aposentar" elas, principalmente na "Oxidação" (`Rustification`) dela.

Em outras palavras, o vovô GNU tá se aposentado e logo logo vai voltar pra Savannah dele.

### Alternativas... tipo?

Tem um monte de projetos novos, o próprio Ubuntu quer substituir o `coreutils` e outras ferramentas por uma versão escrita um Rust, parece interessante no papel, mas qualquer mudança mínima pode dar um problemão em alguns sistemas complexos.

De acordo com uma pesquisa rápida no Google:

> "Rustificação do Ubuntu" refere-se ao projeto em andamento da Canonical para substituir componentes essenciais do sistema operacional Ubuntu, tradicionalmente escritos em C, por alternativas modernas e seguras em termos de memória, escritas na linguagem de programação Rust.
>
> Detalhes principais
> Motivação: Os principais motivadores para essa transição são a segurança aprimorada (o Rust elimina classes inteiras de vulnerabilidades de memória comuns em C) e os potenciais benefícios de desempenho em cenários específicos por meio de uma melhor otimização de hardware moderno, como multithreading.
>
> Componentes principais:
> `sudo-rs`: Uma substituição baseada em Rust para o utilitário sudo clássico, que foi adotada por padrão no Ubuntu 25.10 "Questing Quokka".
`uutils` & `coreutils`: O Ubuntu 25.10 está em processo de substituição do GNU Coreutils (utilitários essenciais do sistema, como `ls, cat e sort`) por suas contrapartes multiplataforma em Rust, conhecidas como `uutils`.
>
> Cronograma: Este esforço ganhou impulso significativo com planos definidos para o lançamento do Ubuntu 25.10 e com o objetivo de ter componentes-chave implementados para o lançamento crítico do Ubuntu 26.04 LTS (Suporte de Longo Prazo).
>
> Desafios: A transição não foi isenta de obstáculos, com relatos de alguns problemas iniciais de desempenho e quebra de compatibilidade para certos executáveis com o núcleo Rust (`coreutils`), embora os desenvolvedores estejam trabalhando para resolvê-los rapidamente.
>
> Ferramenta de gerenciamento: Para gerenciar os testes e a troca desses componentes, os desenvolvedores da Canonical criaram um utilitário de linha de comando chamado `oxidizr`.