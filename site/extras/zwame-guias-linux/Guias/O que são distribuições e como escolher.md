---
layout: default
---

##O que são distribuições e como escolher

Este é um guia que se destina a iniciantes.
Para alguém que se quer introduzir ao mundo Linux, este é um bom sitio para começar.

###Introdução:
Não há um sistema operativo chamado 'Linux', Linux é o nome da peça de software central nos sistemas operativos comummente chamados por este nome. Os restantes componentes de software variam consoante o sistema operativo, e a cada sistema operativo baseado em Linux dá-se o nome de uma 'distribuição', ou abreviando 'distro'.

Imagine uma distribuição como um veiculo, que a única coisa que partilha obrigatoriamente com os restantes veículos é o motor.
Pode ter um formato diferente; ter proteção contra chuva ou não ter qualquer proteção; bastante conforto ou ser otimizado para ser rápido (não ter conforto nenhum); ter uma pintura branca, verde, amarela, cinzenta... etc..

Normalmente há um grupo grande de ferramentas essenciais para o sistema ou para administradores que são partilhadas entre as distribuições, as ferramentas GNU, e dai o nome GNU/Linux, que apesar de não ser utilizado frequentemente por comodidade, é o nome correto dos sistemas operativos chamados de Linux.

###Então e entre essas distribuições, o que muda?
Pode mudar muita coisa, como pode mudar pouca coisa.
Há distribuições cujo único propósito é dar um aspeto diferente á interface de outras distribuições com um tema.
Há distribuições que são otimizadas para computadores antigos muito lentos.
Há distribuições que se focam em ter uma grande estabilidade para computadores que tenham que correr por longos períodos de tempo.
Há distribuições que procuram inovar.
E por ai em diante.
Há uma infinidade de motivos haverem varias distribuições, uns mais validos que outros.

Enquanto que num sistema operativo como o Windows ou o Mac OS X, o sistema vem sempre da mesma forma e tem que ser adaptado para as necessidades dos utilizadores, em GNU/Linux há distribuições que já vem praticamente adaptadas ás necessidades dos utilizadores.

Eu poderia-me alongar mais, mas é uma vertente técnica enorme que eventualmente sai do âmbito do tópico.
Para qualquer duvida não hesitem em fazer um post a perguntar.

###Que distribuição devo de escolher?
Certamente que no Windows e Mac OS X gosta de conseguir procurar por duvidas facilmente na Internet.
Coloca o problema no motor de busca eleito, e provavelmente a sua questão já foi respondida.

Isso passa-se por serem sistemas muito utilizados. São tantos milhões de utilizadores que mais cedo ou mais tarde alguém haverá de fazer determinada pergunta, ou de ter determinado problema.

Da mesma forma e pelo mesmo motivo, também vai querer uma distribuição tão bem suportada quanto possível, que esteja polida para que as coisas simplesmente funcionem, e ao mesmo tempo tenha uma grande comunidade para obter ajuda.

Existem alguns milhões de utilizadores de Linux, mas também existem centenas de distribuições, e muitas delas são projetos pessoais com pouca ou mesmo sem comunidade. O ideal é escolher uma das distribuições mais populares, mas que ao mesmo tempo seja orientada a ser simples e intuitiva a novos utilizadores.

Antes de escolher, veja qual é o ambiente gráfico que quer utilizar, neste artigo.

###E os candidatos são:
###Ubuntu
![Ubuntu](https://upload.wikimedia.org/wikipedia/commons/1/1c/Ubuntu_14.10_Desktop.png)
A distro mais utilizada. É desenvolvida por uma empresa chamada Canonical que presta suporte pago, no entanto tem uma grande comunidade que presta ajuda gratuita.
Tem uma distribuição principal, e [varias secundarias](https://wiki.ubuntu.com/UbuntuFlavors), sendo que nas secundarias a unica coisa que muda é o ambiente gráfico[link para o artigo]. As distribuições secundarias relevantes a utilizadores novos passam por ser o "Kubuntu"(ambiente KDE), "Xubuntu"(ambiente XFCE) e "Lubuntu"(ambiente LXDE). A principal utiliza um ambiente chamado de "Unity".

O Ubuntu tem uma versão nova a cada mês de Abril e de Outubro, sendo que as versões são "ano.mês". Por exemplo, Abril de 2015 é a versão 15.04.
A cada abril de um ano par sai uma LTS, ou seja, uma versão que vai ser suportada durante mais tempo, comparável ás versões de Windows/Mac OS X

####Vantagens:
- Facilidade a obter ajuda
- Facilidade de utilização
- Oficialmente suportado por muitos softwares (como a Steam).
- Os poucos softwares que não estiverem em repositórios, estão em [PPA's](https://en.wikipedia.org/wiki/Personal_Package_Archive)
- Interface gráfica para práticamente tudo
- A única distribuição com uma implementação completa de Unity
- Varias versões alternativas para escolher

####Desvantagens:
- O Unity desagrada a muitos, e não é familiar com mais nenhum SO
- O Unity é considerado algo pesado e lento. Computadores mais antigos ou com pouca memoria devem de optar por outro ambiente gráfico[link artigo].
- Por vezes a Canonical toma decisões questionáveis, como colocar publicidade da Amazon no menu de aplicações (resolvido), e demonstra alguma aversão a soluções que não tenham sido criadas por eles mesmos, mesmo que toda a comunidade as apoie.
- Pouco personalizável.

Download: http://www.ubuntu.com/

###Linux Mint
![Mint](https://upload.wikimedia.org/wikipedia/commons/a/a2/Linux_Mint_17_%28Qiana%29_Cinnamon.png)
Uma distro derivada do Ubuntu, cuja principal diferença passa pelos ambientes gráficos que foram criados pela própria comunidade. Tem dois principais, o Cinnamon(imagem a cima) e o MATE.

####Vantagens:
- A distro com as melhores implementações de Cinnamon e MATE.
- Projeto inteiramente de comunidade sem interesses secundários.
- Versão MATE é bastante leve.
- Os poucos softwares que não estiverem em repositórios, estão em PPA's
- Interface gráfica para praticamente tudo
- O Cinnamon é algo familiar aos utilizadores de Windows XP/Vista/7.

####Desvantagens:
- Para quem não gostar de verde lima, dificilmente vai gostar do tema que vem por defeito. (Simples de mudar nas definições do sistema)

Download: http://linuxmint.com/

###Fedora
![Fedora](https://upload.wikimedia.org/wikipedia/commons/c/cf/Fedora21.png)
Uma distribuição pertencente a uma empresa chamada Red Hat. O Fedora é a distribuição utilizada para testar o que virá a estar presente no Red Hat Enterprise Linux, que é a distribuição de Linux empresarial mais bem sucedida.
Assim sendo tem bastantes desenvolvedores a trabalhar nela e por norma é bastante estável exceto em certas versões pontuais em que as coisas correm menos bem.

####Vantagens:
- Melhor implementação de GNOME em uma distribuição considerada estável
- Similaridades ao Red Hat EL num ambiente empresarial.

####Desvantagens:
- Considerada em algumas versões passadas como algo instável.
- Softwares empacotados [link artigo] apenas para sistemas de base Debian (Ubuntu, Mint) não vão funcionar e vice-versa. Não deverá de afetar utilizadores novos.

Download: https://getfedora.org/ (A versão para desktop é a 'Fedora Workstation')

###OpenSUSE
Similarmente ao Fedora, também é concebida por uma empresa chamada SUSE.
É uma distribuição das mais populares ainda que não tenha os números de utilizadores que tem por exemplo o Ubuntu.
![OpenSUSE](https://upload.wikimedia.org/wikipedia/commons/9/96/OpenSUSE13_2.png)
####Vantagens
- Uma das melhores implementações de KDE
- Instaladores de 1 clique para boa parte dos softwares
- O painel de controlo (YaST) tem interfaces graficas para a configuração de grande parte do sistema
- Similaridades ao SUSE EL.

####Desvantagens
- Comunidade comparativamente pequena.
- Pequena quantidade de softwares empacotados comparativamente ás restantes distros.

Download: https://www.opensuse.org/

###Elementary
![Elementary](https://upload.wikimedia.org/wikipedia/commons/9/95/Screenshot_from_2013-08-11_15_57_35.png)
Uma distribuição criada por um pequeno grupo de desenvolvedores, que entenderam que os ambientes gráficos não tem o polimento e a elegância que um utilizador esperaria. Assim sendo começaram por fazer temas, e acabaram com o seu próprio ambiente gráfico, o Pantheon.
Uma das distribuições mais recentes e promissoras.
####Vantagens
- Única distribuição com uma implementação completa do Pantheon
- Interface algo familiar a utilizadores de Mac OS X.
- Considerada por muitos como a distribuição mais polida em aspeto gráfico
- Herda boa parte das vantagens do Ubuntu por se tratar de um Ubuntu personalizado.

####Desvantagens
- Algo instável
- Equipa pequena por traz
- Comunidade comparativamente pequena

Download: https://elementary.io/

###Antergos/Manjaro
![Manjaro](https://upload.wikimedia.org/wikipedia/commons/5/59/Manjaro_Linux_Xfce_0.8.11.jpg)
####Vantagens
- Sistemas mínimos sem muito conteúdos por defeito que venham a ser desnecessários ao utilizador
- Virtualmente todos os softwares disponíveis em Linux ou nos repositórios ou no AUR(repositório publico, não oficialmente suportado)
- Capacidade de personalização do sistema.
- Rolling-Release (A distro não tem versões e os softwares atualizam sempre até á ultima versão)
- Hipóteses maiores de suportar o hardware mais recentes

####Desvantagens
- Considerados instáveis por praticamente não haver teste antes de os softwares chegarem aos utilizadores.
- Requerem noção básica de como funciona o gestor de pacotes do Arch Linux(distribuição pai de ambos)
- Podem requerer intervenções do utilizador quando algo corre mal, e as mesmas podem requerer conhecimentos médio-avançados que um utilizador iniciante não vai ter.

Download: http://antergos.com/ e https://manjaro.github.io/

###Fatores a ter em conta na escolha:
- Qual a idade do hardware: Se o hardware a instalar for recente, certifique-se que a ultima versão da distribuição saiu pelo menos dois a seis meses depois do hardware. Isto porque por questões de estabilidade, a maior parte das distros congela o código(ou seja deixa de adicionar funcionalidade, apenas corrigindo erros) nas versões beta cerca de um mês antes de serem lançadas. Por isso se as drivers forem muito recentes podem não estar incluídas nas distribuições.<br>
Se a versão da distribuição for mais do que 6 meses mais nova que o hardware é uma boa garantia(muito provável) em como vai funcionar. Note que por 'hardware' entende-se por CPU, GPU e Motherboard. Trata-se assim de uma generalização visto que tanto a AMD, Intel, e a Nvidia são empresas favoráveis ao suporte em Linux, o que perfaz 99,*% do mercado desktop.
A mesma regra só se aplica ao restante hardware (placas WI-FI, periféricos mais elaborados, ...) no caso de o fabricante ser favorável a Linux, como é o caso de boa parte deles. É uma boa ideia confirmar antes ou perguntar.<br>
A idade perfeita de determinado hardware em Linux (afirmação subjetiva) é entre um ano e dois anos de idade, visto que trata-se ainda de hardware recente mas no entanto as drivers já tiveram tempo de amadurecer.

- Versões de suporte longo (LTS):
Essas versões tendem a ficar paradas no tempo, sendo a benesse das mesmas a estabilidade.
Se procurar um local de trabalho estável, e o seu hardware já tiver drivers em uma versão LTS, é uma boa opção.
São também boas para quem não quer ter que atualizar o sistema de alguns em alguns meses. E por atualizar o sistema refiro-me literalmente ao sistema todo, porque ir colocando as atualizações de segurança é sempre bom, seja qual seja o sistema operativo.

- O meu hardware é demasiado recente:
Ai está o motivo de ter incluído Antergos e Manjaro na lista. Não são distribuições ambicionadas a utilizadores novos, há demasiada coisa que pode correr mal, no entanto o fato de não terem versões('rolling-release', estarem sempre atualizadas) e de poderem ser o que o utilizador quiser implica que podem-se tornar em algo parecido a qualquer uma das outras, e isto sempre com as ultimas drivers.
Ambas são variações(sendo a primeira pouco mais que um instalador) de Arch Linux, que é uma das distribuições ambicionadas a utilizadores com experiência que querem personalizar o sistema, só que com uma interface gráfica para ajudar a configurar o sistema aquando da instalação. A partir dai é por conta própria com a ajuda da [wiki do Arch](http://wiki.archlinux.org).
O OpenSUSE tambem tem uma versão 'rolling release', mas é secundaria e não é tão bem mantida. Tal como o Fedora também tem um canal de testes "Fedora Rawhide", mas não recomendo por ser demasiado instável para o dia-a-dia.

- O melhor suporte oficial a software:
O melhor suporte será (no futuro previsível) com as distribuições de base Debian; Ou seja: Ubuntu, Mint e Elementary. As restantes possivelmente também terão o mesmo software, seja nos repositórios oficiais ou não oficiais, mas alguns softwares adaptados não são oficialmente suportados pelo desenvolvedor.
>Exemplificando: A Steam só é suportada oficialmente em Ubuntu, no entanto práticamente todas as distribuições a têm e a mesma funciona bem.
>Neste caso em especifico, os desenvolvedores tem sido suportivos, e ajudam mesmo que não se utilize a distribuição oficialmente suportada. No entanto isto significa que se os responsáveis pela Steam, ou pelos jogos que a mesma tem, decidirem não prestar suporte a problemas que aconteçam em outras distribuições que não Ubuntu, o podem fazem e o utilizador não tem qualquer direito a contestar o mau funcionamento dos bens adquiridos enquanto não estiver em uma distribuição oficialmente suportada.