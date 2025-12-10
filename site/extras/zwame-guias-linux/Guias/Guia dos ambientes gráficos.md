---
layout: default
---

##Guia dos ambientes gráficos
Neste guia pretendo expor os principais ambientes gráficos que estão disponíveis em sistemas GNU/Linux.
Existem dois tipos de ambiente gráfico, 'ambientes de desktop'(do inglês 'desktop environments') e 'gestores de janelas'(window managers), que costumam ser abreviados para DE's e WM's.
Um ambiente de desktop é uma interface que gere janelas e cria um desktop, tendo também um conjunto de ferramentas agregadas, como um leitor multimédia, um explorador de ficheiros, etc...; enquanto que um gestor de janelas apenas se preocupa em dispor as janelas no ecrã muitas das vezes.

Como normalmente os gestores de janelas envolvem configuração adicional por parte dos utilizadores, vou exclui-los do guia, sendo que apenas vou mencionar os ambientes de desktop.

###GNOME3
![Gnome3](https://upload.wikimedia.org/wikipedia/commons/9/97/GNOME_Shell.png)
Um dos três grandes desktops em termos de comunidade. É um projeto maturo e já à muito tempo existente, ainda que a versão 3 tenha sido uma grande fonte de criticismo pela grande falta de usabilidade e polimento que o novo paradigma representou nas primeiras versões. Muitos consideram os problemas resolvidos, alguns ainda o consideram pouco funcional (é subjetivo).

####Vantagens
- Aspeto polido
- Interface minimalista
- Extensões para personalizar a shell
- Portado para Wayland
- Aplicações bem integradas com o ambiente

####Desvantagens
- Consumo de recursos do sistema
- Pode ser difícil para um utilizador habituar-se áo manuseio do GNOME.

####Onde encontrar:
- Uma das versões de algumas das principais distribuições
- Fedora (Melhor implementação na minha (subjetivo))

- - -
###Cinnamon
![Cinnamon](https://en.wikipedia.org/wiki/Cinnamon_%28software%29#/media/File:Linux_Mint_17_%28Qiana%29_Cinnamon.png)
Com o descontentamento que as primeiras versões de GNOME 3 trouxeram, formou-se uma comunidade em torno de bifurcar o mesmo para um projeto diferente, o Cinnamon, e assim nasceu este projeto que agora cresce independente do GNOME.

####Vantagens
- Personalizável
- Extensões
- Familiar a utilizadores de Windows

####Desvantagens
- Consumo de recursos do sistema
- Poucas implementações

####Onde encontrar:
- Linux Mint (Melhor implementação (subjetivo))
- Arch linux e derivados
- Repositorios não oficiais

- - -
###KDE4
![KDE4](https://upload.wikimedia.org/wikipedia/commons/5/54/KDE_4.png)
Um dos grandes desktops. Também já tem muitos anos, ainda que muitos questionem a maturidade. Quando o KDE 4 foi lançado era um íman de problemas, tinha bastantes bugs, mas a situação tem-se vindo a melhorar com os anos.
Há quem diga que dá demasiada preferência ao aspeto e pouca à eficiência e produtividade, mas é subjetivo.

####Vantagens
- Personalizável
- Familiar a utilizadores de Windows
- Aspeto polido

####Desvantagens
- Algo instável
- Consumo de recursos do sistema
- Será dentro de poucos anos descontinuado em favor do KDE5

####Onde encontrar:
- Uma das versões de algumas das principais distribuições
- OpenSUSE e Kubuntu são boas implementações

- - -
###KDE5
![KDE 5](https://upload.wikimedia.org/wikipedia/commons/2/2f/KDE_Plasma_5.png)
Próxima iteração do KDE. Já se encontra em desenvolvimento avançado e é considerado razoavelmente funcional.
Ambiciona resolver os problemas do KDE4, e para já aparenta ter sucesso.

####Vantagens
- Personalizável
- Familiar a utilizadores de Windows
- Aspeto polido, e modernizado em relação ao KDE4
- Mais leve nos recursos do sistema que o KDE4
- Porte para Wayland

####Desvantagens
- Consumo de recursos do sistema
- Ainda em desenvolvimento pesado. Pode não funcionar corretamente
- Poucas implementações

####Onde encontrar:
- Futuras versões de de algumas das principais distribuições
- Um dos spins a começar no Fedora 22.
- Kubuntu(Versão?) [Mais?]

- - -
###Unity
![Unity](https://upload.wikimedia.org/wikipedia/commons/1/1d/Ubuntu_14.10_Utopic_Desktop.png)
O ambiente com mais utilizadores por se tratar do ambiente por defeito no Ubuntu, sendo o ultimo dos grandes.
É alvo de muito criticismo por ser um projeto empresarial e não de comunidade, e como tal seguir as vontades da empresa, e não apenas as da comunidade que o usa. Há quem o adore, há quem o deteste, lá está, depende de cada um.

####Vantagens
- Aspeto polido
- Interface minimalista
- Integração

####Desvantagens
- Pouca personalização
- Consumo de recursos do sistema
- Uma implementação (Ubuntu)
- Provavelmente não será portado para Wayland em favor do Mir

####Onde encontrar:
- Ubuntu

- - -
###XFCE
![XFCE](https://upload.wikimedia.org/wikipedia/commons/1/1a/Xfce4.12.jpg)
Ambiente destinado a ser tão leve quão funcional. Muitos o adoram por ser um excelente ambiente para trabalhar, sem grandes distrações, e por simplesmente funcionar sem bugs e os restantes problemas que os ambientes de rápido desenvolvimento sofrem.

####Vantagens
- Bastante leve
- Interface minimalista
- Personalizável a fundo

####Desvantagens
- Lento ritmo de desenvolvimento. Praticamente abandonado.
- Pouca ou nenhuma integração com as aplicações
- Sem suporte a toolkits modernos (preso no GTK2 por falta de desenvolvedores)
- Baixa probabilidade de vir a suportar Wayland

####Onde encontrar:
- Uma das versões de algumas das principais distribuições

###LXDE
![LXDE](https://upload.wikimedia.org/wikipedia/commons/4/4c/LXDE_desktop_full.png)
Ambiente cujo principal foco é o de ser leve. Utiliza uma fração dos recursos dos restantes sendo capaz de fazer o mesmo. É também bastante estável.

####Vantagens
- Bastante leve
- Interface minimalista
- Personalizável a fundo

####Desvantagens
- Aspeto algo rudimentar (subjetivo)
- Pouca ou nenhuma integração com as aplicações
- Baixa probabilidade de vir a suportar Wayland

####Onde encontrar:
- Uma das versões de algumas das principais distribuições

- - -
###MATE
![MATE](https://upload.wikimedia.org/wikipedia/commons/8/88/MATE_Desktop_Environment_1.8_-_About.png)
Quase simultaneamente com o Cinnamon, o MATE foi uma bifurcação de GNOME, mas enquanto que o Cinnamon foi das primeiras versões de GNOME 3, o MATE foi das ultimas de GNOME 2. Tenta assim fornecer o ambiente clássico a quem o preferir, quer por ser consideravelmente mais leve que os modernos, ou apenas por ser funcional e funcionar.

####Vantagens
- Bastante leve
- Interface minimalista
- Personalizável a fundo
- Ambiciona brevemente o suporte a GTK3

####Desvantagens
- Pequena comunidade

####Onde encontrar:
- Algumas distribuições tem uma versão MATE:
- Linux Mint
- Ubuntu MATE
- Fedora MATE
- Arch
- Gentoo
- ...

- - -
###Pantheon
![Pantheon](https://upload.wikimedia.org/wikipedia/commons/9/95/Screenshot_from_2013-08-11_15_57_35.png)
Um pequeno grupo de designers que fazia temas em GNOME 2, começou a aumentar, e eventualmente chegaram ao ponto de bifurcar o GNOME 3 para fazerem a sua própria implementação. É considerado um dos ambientes mais visualmente atrativos, ainda que seja um projeto muito novo e com um desenvolvimento relativamente lento.

####Vantagens
- Aspeto moderno
- Polimento e integração
- Minimalista e intuitivo.
- Familiar a utilizadores de Mac OS X.

####Desvantagens
- Fraca capacidade de personalização
- Imaturo
- Pequena comunidade de desenvolvedores para um projeto muito popular.
- Uma única implementação (Elementary OS)

####Onde encontrar:
- Elementary OS

- - -
###Enlightnment
![Enlightenment](https://2.bp.blogspot.com/-uh-ZM1LM6Qg/VB7D6EOsm0I/AAAAAAAAJ-M/QuGI9bAujHM/s1600/enlightenment-19-2.jpg)
Um dos projetos mais antigos para desenvolver um ambiente. Já quase celebra 20 anos, e no entanto continua muito pouco conhecido por parte da comunidade, possivelmente por não seguir os standards de desenvolvimento e implementar os seus, o que dificulta a adoção ainda que seja perfeitamente funcional.

####Vantagens
- Altamente personalizável
- Porte para Wayland

####Desvantagens
- Aspeto algo inconsistente
- Pequena comunidade
- Implementa tecnologias pouco utilizadas
- Pouco implementado

####Onde encontrar:
- Principalmente nas distribuições personalizáveis como o Arch, Gentoo
- Repositórios e PPA's

- - -
###RazorQT / Futuro LXQT
![RazorQT](https://upload.wikimedia.org/wikipedia/commons/8/86/Razor_desktop.png)
Começou como um projeto similar aos restantes ambientes que ambicionam ser leves, e agora é o esforço de mover o LXDE de GTK2 para QT5 com a finalidade de o modernizar.

####Vantagens
- Personalizável
- Toolkit moderno(QT5), e potencial porte a wayland
- Leve

####Desvantagens
- Em desenvolvimento
- Pequena comunidade
- Pouco implementado

####Onde encontrar:
- Principalmente nas distribuições personalizáveis como o Arch, Gentoo

- - -
###Deepin
![Deepin](https://upload.wikimedia.org/wikipedia/commons/2/23/DeepinScreenshot20141114011107.png)
[Alguém que tenha utilizado que faça as honras de escrever algo para aqui]

####Vantagens
- ?

####Desvantagens
- Comunidade existente
- Uma procura pelo mesmo abre o site oficial, por defeito em chinês.
- Pouco implementado
- ?

####Onde encontrar:
- Deepin OS

- - -
###Budgie Desktop
![Budgie](http://www.omgubuntu.co.uk/wp-content/uploads/2014/11/budgie-desktop.jpg)
[Alguém que tenha utilizado que faça as honras de escrever algo para aqui]

####Vantagens
- Familiaridade a utilizadores de Chrome OS.
- Interface minimalista
- ?

####Desvantagens
- Uma única implementação default
- Fraca personalização (?)
- ?

####Onde encontrar:
- SolusOS
- Repositórios e PPA's.

Qualquer duvida disponham.
Contribuições e edições são bem vindas.