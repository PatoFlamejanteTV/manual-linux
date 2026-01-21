# Void Linux

O Void Linux é um sistema operacional de propósito geral, desenvolvido de forma independente (não é baseado em Debian, Arch ou qualquer outra). É uma distribuição *rolling release* (atualização contínua) que foca na estabilidade, velocidade e simplicidade.

Desenvolvido originalmente por um ex-mantenedor do NetBSD, o Void carrega uma filosofia similar aos sistemas BSD.

## Características Únicas

1. **Runit:** Ao invés do onipresente systemd, o Void usa o **runit** como sistema de init e supervisão de serviços. Ele é extremamente rápido no boot, simples de configurar e muito leve.
2. **XBPS (X Binary Package System):** O gerenciador de pacotes, escrito do zero em C. É incrivelmente rápido na instalação e atualização de softwares.
3. **LibreSSL:** O Void foi uma das primeiras distros a trocar o OpenSSL pelo LibreSSL (embora tenha voltado ao OpenSSL recentemente por compatibilidade, a filosofia de segurança permanece).

## Prós (Vantagens)

1. **Performance:** Devido à falta de bloatware e ao uso do runit, é um dos sistemas mais rápidos para ligar e operar.
2. **Estabilidade Rolling:** Consegue trazer software novo sem quebrar o sistema constantemente, algo difícil de equilibrar.
3. **Independência:** Não sofre influência de grandes corporações ou decisões polêmicas de distros "mãe".

## Contras (Desvantagens)

1. **Documentação:** Embora boa, é menor que a do Arch ou Ubuntu.
2. **Repositórios:** Menos pacotes disponíveis nos repositórios oficiais se comparado ao Debian ou Arch, embora exista o `XBPS-src` para compilar pacotes extras.
3. **Diferente:** Comandos de serviço e pacotes são únicos do Void, exigindo reaprendizado.

## Para Quem é?

* Usuários intermediários/avançados que querem um sistema Rolling Release estável.
* Pessoas que buscam alternativas ao systemd.
* Quem gosta de sistemas rápidos e responsivos em hardware antigo ou novo.
