# Linux Mint

Linux Mint é uma distribuição baseada no [Ubuntu](ubuntu.md) (que por sua vez é baseada no [Debian](debian.md)), extremamente popular e recomendada para iniciantes. Ela foca em ser fácil de usar, elegante e "pronta para o uso" (*out-of-the-box*) assim que instalada, incluindo codecs multimídia e drivers proprietários que outras distros podem evitar por padrão.

O lema do projeto é "From freedom came elegance" (Da liberdade veio a elegância).

## Edições Principais

O Linux Mint é distribuído em três edições principais, cada uma com um [Ambiente de Desktop](../interface/de.md) diferente:

1. **Cinnamon:** A edição principal e mais moderna. O desktop Cinnamon é desenvolvido pela própria equipe do Mint. Ele oferece uma interface tradicional (barra de tarefas, menu iniciar), mas com tecnologias modernas e muitos efeitos visuais. É ideal para quem vem do Windows 7 ou 10.
2. **MATE:** Uma continuação do clássico GNOME 2. É mais leve que o Cinnamon e muito estável, ideal para computadores um pouco mais antigos ou para quem prefere uma interface mais "conservadora" e rápida.
3. **Xfce:** A edição mais leve e rápida. Foca em estabilidade e baixo consumo de recursos, sendo perfeita para computadores antigos ou com hardware limitado.

Existe também o **LMDE (Linux Mint Debian Edition)**, que é baseado diretamente no Debian Stable em vez do Ubuntu. O objetivo do LMDE é garantir que o Mint possa continuar existindo caso o Ubuntu desapareça ou tome decisões drásticas que a equipe do Mint não concorde.

## Diferenciais e Ferramentas (Mint Tools)

O Mint se destaca por desenvolver suas próprias ferramentas para facilitar a vida do usuário, os chamados "X-Apps":

* **Gerenciador de Atualizações:** Classifica as atualizações por níveis de segurança e permite configurar atualizações automáticas de forma granular.
* **Gerenciador de Software:** Uma loja de aplicativos visualmente agradável que suporta tanto pacotes `.deb` quanto **Flatpaks** por padrão (o Mint bloqueia os Snaps do Ubuntu por padrão por discordar da filosofia centralizada da Canonical).
* **Timeshift:** Uma ferramenta de backup pré-instalada que permite criar "snapshots" do sistema. Se uma atualização quebrar algo, você pode restaurar o sistema para um estado anterior com poucos cliques.
* **Warpinator:** Uma ferramenta simples para compartilhar arquivos na rede local entre computadores Linux (e até Android/Windows).

## Prós (Vantagens)

1. **Extremamente Amigável:** Provavelmente a transição mais suave para usuários de Windows. A interface é familiar e intuitiva.
2. **Pronto para Usar:** Codecs de áudio/vídeo, suporte a Flash (antigamente) e drivers proprietários são fáceis de instalar ou já vêm prontos.
3. **Estabilidade:** Por ser baseado nas versões LTS (Long Term Support) do Ubuntu, o Mint é muito estável.
4. **Controle sobre Atualizações:** O usuário decide quando e o que atualizar, sem interrupções forçadas.
5. **Comunidade Ativa:** Sendo baseado no Ubuntu, quase qualquer tutorial para Ubuntu funciona no Mint.

## Contras (Desvantagens)

1. **Ciclo de Atualização:** Como baseia-se em versões LTS, os pacotes de software (como versões do kernel ou ambientes de desktop) podem ficar um pouco defasados em comparação com distros *rolling release* como o [Arch Linux](arch-linux.md).
2. **Visual:** Alguns usuários acham o visual padrão um pouco datado ou "clássico demais" em comparação com o GNOME moderno ou o KDE Plasma (embora seja altamente customizável).
3. **Incerteza do Ubuntu:** Embora o Mint filtre muitas decisões da Canonical, ele ainda depende da base do Ubuntu (exceto a versão LMDE).

## Para Quem é?

* **Iniciantes absoluta no Linux:** É a recomendação padrão "número 1" para quem está começando.
* **Usuários que querem produtividade:** Para quem quer um sistema que "simplesmente funcione" sem precisar configurar nada.
* **Fãs de interfaces clássicas:** Quem prefere o paradigma de "Menu Iniciar + Barra de Tarefas".
