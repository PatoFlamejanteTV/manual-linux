---
layout: default
---

## Como (não) ser um bom membro da comunidade
Vou escrever este guia no âmbito de dar a entender alguns dos principais problemas que vejo atualmente nas comunidades de software aberto(e não só).
Trata-se de um guia critico baseado na minha opinião pessoal, que pode não ser igual á vossa opinião. Quem discorde sugiro que expresse o ponto-de-vista de seguida devidamente argumentado, e se quiser que proponha uma edição dês de que devidamente justificada.

- ### **Linux é a única coisa boa na terra, é meu dever evangelizar!**
Algo importante de aceitar é que os sistemas Linux não fazem tudo. Seja culpa própria ou de empresas/comunidades que não os querem suportar pouco interessa para o argumento. Há que reconhecer que há alturas em que o melhor SO para uma determinada tarefa **neste preciso instante** pode não ser de base Linux.
```
É possível fazer edição gráfica em Linux?
É possível fazer documentos de Office em Linux?
É possível jogar XYZ em Linux?
```
Até que pode ser, mesmo que com ferramentas alternativas, ou com softwares como o Wine, mas há que entender que muitos dos utilizadores não estão virados para correr o Wine (porque tem bugs, porque é lento, porque envolve truques e experimentação que custa tempo, porque não tem uma experiência nativa), e definitivamente ninguém quer ter problemas no local de trabalho por entregar um documento `.ODT` que o chefe não consegue abrir, ou um documento de Word com problemas de formatação.
(Isso passa por ser outro problema distinto, que é educar as pessoas e os locais de trabalho para preferir os formatos abertos.)
Já se todos os softwares que determinado utilizador quiser estiverem disponíveis nativamente, ai não há motivo para não incentivar os utilizadores a mudar caso os mesmos demonstrem descontentamento com o que tem.
> **Exemplo**: Não devem de dizer a um designer que tem que aprender a fazer as coisas com o GIMP ou que pode utilizar o Wine para correr o Photoshop, o procedimento correto é explicar-lhe que se o sistema não tiver utilizadores nunca vai ter o Photoshop nativo, e que se estiver disposto a experimentar o deverá de fazer á parte do trabalho que assim dá cota de mercado que pressiona a Adobe a portar o Photoshop.
> **Exemplo2**: `Utilizo o computador para ir à Internet, e praticamente só jogo Counter Strike[Ou outro jogo já portado]. O meu trabalho passa por envolver ferramentas que funcionam no navegador. Acho o Windows lento e tenho montes de problemas com vírus.` É uma boa situação para sugerir o utilizador a mudar para um sistema de base Linux.


- ### **Esse projeto é horrível, não fazem as coisas consoante os meus interesses.**
Discurso de ódio, é o que muitos utilizadores gostam de exprimir cada vez que alguém faz um projeto ou uma alteração a um projeto que os mesmos não gostam. Ou por [FUD](https://pt.wikipedia.org/wiki/Medo,_incerteza_e_d%C3%BAvida), ou seja, medo de não virem a gostar e de ter potencial para ser mau; porque acham que é anti-produtivo; porque acham que teriam uma forma melhor de fazer o mesmo; ou mesmo porque acreditam que o software que utilizam venha a ser influenciado por essa alteração que não gostaram de futuro.
O que mais se nota nesses utilizadores, é que muito facilmente falam que fariam melhor, que se se fossem eles isto, se fossem eles aquilo, mas nunca vão contribuir. Os projetos opensource, maior parte das vezes tem uma comunidade em volta dos mesmos, e essas comunidades aceitam contribuições de código. No entanto esses utilizadores de imaginação imensa arranjam todos os argumentos falaciosos possíveis para argumentarem motivos para não contribuírem, como "o projeto já está perdido", "eu contra um bando de imbecis", "tenho coisas melhores que fazer"(no entanto tem tempo para criticar sem qualquer retorno).
Esta atitude é condenável, e não passa de egoísmo ou de alguém a querer inserir flame para dentro de uma comunidade para proveito próprio(Trolling).
>**Exemplo**: Existe um projeto especialmente criticado que sucedeu o GNOME nas criticas em massa, que é o SystemD.
>O SystemD é uma tentativa de uniformização dos sistemas de arranque(init) que existem, entre mais alguns softwares, muitos deles com décadas e décadas em cima. Como foi feito do zero, o design no mesmo não seguiu à letra os anteriores, e funciona de formas diferentes para fazer o mesmo. Talvez melhores, talvez piores,(é discutível) mas diferentes.
>Claro que teve um inicio difícil, é uma peça considerável de software e tinha bugs, mas entretanto amadureceu para uma das peças mais estáveis e funcionais de software num sistema Linux.
>O mesmo é desenvolvido em comunidade, e como tal as decisões passam por ser um julgamento do que os desenvolvedores consideram melhor. Nada impede impede alguém de se tornar um desenvolvedor, dês de que seja um programador decente.
>No entanto ainda hoje há utilizadores que adoram provocar ódio, e sem qualquer motivo falarem mal, no entanto recusam-se a contribuir.
>O SystemD é nada mais do que um reflexo do que a comunidade quer, no entanto um utilizador satisfeito raramente é vocal, principalmente se o software nem visível for como é o caso do SystemD.
Danifica-nos gravemente a reputação, ter o próprio Lennart Poettering(criador do SystemD) a dizer que uma comunidade opensource é "Um lugar doentio para estar"

- ### **Li uma noticia na diagonal, mas vou criticar um projeto pelo pouco que sei.**
Os adoráveis utilizadores desinformados que se juntam á critica prévia. Estão satisfeitos, ninguém lhes tira o comer do prato, no entanto lêm uma noticia que é escrita em teor sensacionalista, ou leem da fonte mas interpretam mal, e tem logo que partir á batalha.
`"O não-faço-ideia-do-que-isto-é foi adicionado ao SystemD"` - `"Oh meu deus, aquela gente é maluca. Querem meter tudo dentro da aberração do SystemD"`
`"O GTK adiciona suporte a algo-que-desconheço-nem-vou-procurar"` - `"Vai ficar super pesado se adicionam mais coisas. Os dev's não sabem o que fazem!"`
`"O AdBlock Plus recebe xxx$ da Google/Microsoft/[...]"` - `"Comprados comprados comprados!!!"`
Para sustentar a critica, este ultimo exemplo que foi uma das ultimas escândaleiras, refere-se à política de cobrar aos grandes sites que queiram ter anúncios na lista dos "aceitáveis" ([dês de que o sejam](https://adblockplus.org/en/acceptable-ads#criteria)) para sustentar o projeto e foi uma [desição aceite pela comunidade em votação](https://adblockplus.org/blog/adblock-plus-user-survey-results-part-3). Os utilizadores desinformados correram a criticar, sem se terem apercebido que tal política dos anúncios aceitáveis era "gratuita de aplicar aos pequenos e médios websites" e que não se trataria de suborno nenhum, apenas de tirar sustento dos grandes anunciantes e não dos pequenos blogues.
Ainda para mais não se davam por contentes com a solução de terem uma opção nas configurações para desativar a política de anúncios aceitáveis na integra.

- ### **"A não funciona como resolvo? Experimenta B!" ou "O meu é melhor que o teu."**
Estas sugestões criticas ou comparações são muito vistas. Seja na comunidade opensource ou não, mas como a comunidade opensource tem menos barreiras á mudança (como questões de custo) muitos as fazem sem pensar.
Dês da simples discussão do editor de texto a utilizar:
`"Utilizas o gedit/nano/eclipse/[inserir nome de editor de texto]?Isso é tão improdutivo, utilizadores a sério utilizam o VIM/Emacs."`até ao`"Ubuntu? Eu utilizo o Arch/Gentoo/Slackware com muito orgulho!"`
Há alturas coerentes para argumentar que um utilizador deve de mudar os softwares que utiliza, mas muitas das vezes estas sugestões apenas vão arranjar mais problemas ao utilizador que aparentemente só tinha um único problema, ou que nem problemas sabia ter.<br>
Ora imaginem-se como novos utilizadores. Provavelmente começam pelo Ubuntu, é a distribuição mais conhecida, razoavelmente simples e intuitiva de utilizar.
Se alguns dias depois de começarem a utilizar já alguém vos disse `"Ubuntu?!? Mas isso é tão bloated e o Unity é uma interface péssima... O mint é igual mas melhor!"`, lá vocês confiam e vão a trocar o Ubuntu por um Mint.
Depois mais cedo ou mais tarde aparece alguém a argumentar
`"Ubuntu? Mint? Isso são tudo derivados do Debian... o original é melhor e mais leve!"`.
Troca-se o Mint pelo Debian.
`"Debian?!? Mas isso é tão desatualizado... Tens algum servidor? Atualiza isso para um Fedora!"`
Troca-se o Debian por um Fedora.
`"Fedora? Eu não confiaria em algo da Red Hat, são uma corporação, certamente mais cedo ou mais tardo nos fazem mal. Se queres tudo atualizado instala o Arch!"`
Troca-se o Fedora pela grande wiki do Arch.
`"Não consegues instalar o Arch? Experimenta o Antergos, é o mesmo mas mais fácil."`
Instala-se o Antergos.
`"Antergos? Quem quer um Arch simples e estável utiliza o Manjaro!"`
Siga o Manjaro
`"Devias de ter controlo de tudo o que tens no computador. Só compilando! Experimenta o Gentoo que é uma excelente experiência de vida!"`
O utilizador suicida-se. Menos um ex-utilizador de Windows.<br>
Um utilizador quando quiser partir à aventura, fá-lo, não é necessário de o incentivar. No software opensource o que menos custa é partir à aventura, no entanto ninguém quer trocar um problema por outros tantos quando não está para isso, ou por não ter paciência, ou porque necessita de trabalhar.


- ### **Sugerir sistemas mal suportados(ou outros softwares)**
Este problema é uma vertente do problema anterior.
Comecemos por pressupor que se alguem tiver que perguntar o que deve de utilizar, é porque não tem grande experiência.
Eu não perguntaria `"que leitor multimédia devo de utilizar?"` se visse multimédia com frequência e já à algum tempo.
Pelo mesmo motivo sugerir uma distribuição nova (ou antiga mas pouco popular), que não seja baseada em uma das grandes (ou que seja mas insira mudanças radicais) a um utilizador que não consegue estár à vontade, ser autónomo e desenrascar-se por conta própria, é o mesmo que fazer o utilizador têr uma má experiência de utilização, porque garantidamente vai ter problemas, e não vai ter grandes ajudas para os resolver.
>**Experiência pessoal:** Eu quando me iniciei(sensivelmente meia década) também fui pelos caminhos comuns. Ubuntu por algum tempo, e como era miúdo e queria experimentar mais coisas passei pelo Mint (que na altura estava muito menos maturo do que agora está) até que acabei por me ficar em OpenSUSE por um bom bocado.
>O OpenSUSE é uma distribuição das grandes, mais pela vertente de vir do SUSE que é suportado em ambiente empresarial do que por ter uma grande comunidade, que não tem nem de perto o tamanho da comunidade de um Debian/Ubuntu/Mint/Arch.
>É basicamente para o SUSE o mesmo que o Fedora é para o Red Hat, só que menos utilizado, e ainda menos era à uns anos atrás.
>O OpenSUSE tem uma wiki na qual estão as instruções para o essencial, como instalar as drivers da gráfica, e não muito mais, mas felizmente tem um painel de controlo (chamado YaST) exemplar que ajuda na maior parte das coisas.
>Apesar dessas ajudas, não haviam fórums enormes onde pudesse obter ajuda, e na altura não sabia utilizar o IRC (que mesmo que soubesse ainda teria que saber expressar o meu problema e interpretar o que me indicassem). O OpenSUSE tem um fórum próprio, mas que não é ridiculamente copulado como um AskUbuntu ou outros canais de ajuda que por ai andam.
>Eventualmente lá me consegui entender com a coisa (e uns tempos mais tarde mudei novamente para continuar a experimentar), mas a quantidade de tempo que gastei para aprender a fazer certas coisas (que muito facilmente se encontram tutoriais para as distribuições com maiores comunidades) para muita gente é suficiente para desincentivar a experimentar coisas novas de futuro. Eu felizmente como era miúdo considerava aquilo um desafio e dei para o teimoso até ter o que quisesse feito, mas muita gente não é assim.

- ###Distro fanboys
Refiro-me a utilizadores que patrocinam uma distribuição cegamente.
Gostar de uma distribuição, pertencer à comunidade, e promover uma distribuição é bom; mas falar dessa distribuição como se fosse a única verdadeira, e trata-la como se não fosse maioritariamente igual ás restantes é mau.
Esse género de comportamento leva a ainda mais fragmentação da comunidade, e dificulta as pessoas novas a encontrar ajuda.
Eu por exemplo utilizo Arch Linux, utilizo porque me encaixa, no entanto é uma distro que devido à quantidade de distro fanboys que tem é reputada por ser uma comunidade de hipsters arrogantes, que não conseguem terminar uma frase sem dizer "no meu Arch Linux"
Ora alguém que vê, ou intuitivamente diz que se trata de um fanboy e evita experimentar a distribuição, ou vai na cantiga e vai com expectativas altíssimas a experimentar o tal magnifico Arch Linux, para vir a descobrir que sem conhecimentos vai levar 15 tentativas e cerca de 8 horas a instalar o sistema, e no final descobrir que foi mal instalado e é instável.
Felizmente ente os utilizadores de Gentoo e Slackware não aparentam haver tantos distro fanboys, porque senão estaria tudo muito mal encaminhado.
>**Exemplo do que (não) fazer:** `"Como instalar [nome de software do Windows] em [nome de distribuição linux]"`; Um guia para utilizar um script do PlayOnLinux, no qual os scripts são genéricos e dês de que satisfeitas as dependências funcionam em todas as distribuições.
>O que alguém entende quando vê é que as instruções só se aplicam á distribuição mencionada,


- - -
Não sejam maus membros da comunidade. Temos todos uma causa em comum, e mesmo que as nossas opiniões possam divergir temos que ser o mais assertivos possível para nos destacarmos pela positiva, e não pela negativa.