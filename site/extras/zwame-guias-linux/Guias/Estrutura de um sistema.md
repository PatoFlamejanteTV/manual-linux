---
layout: default
---

## Estrutura de um sistema GNU/Linux
Com este guia pretendo explicar como é um sistema GNU/Linux, ao nível dos componentes.

Um sistema operativo pode ser pensado como um enorme lego, cheio de peças que interagem as restantes de forma a que o hardware (parte física do dispositivo eletrónico).
Cada peça tem a sua função.
Existe uma peça que indica ao hardware como iniciar, executando o núcleo.
O núcleo opera o processador e indica o que é executado.
As drivers são instrutores, que indicam ao núcleo como utilizar componentes de hardware. Agarram-se ao núcleo como módulos do mesmo.
Os processos (alguns deles comummente chamados de aplicações) são tarefas que estão carregadas na memória do computador, podendo ocupar o processador de x em x tempo para o que necessitarem (des de que autorizadas pelo núcleo).
Os daemons (ou serviços), são tipos de processos que operam(geralmente) sem serem diretamente visíveis ao utilizador. Eles gerem funcionalidades, dês da ligação à rede, som, até uma outra infinidade de coisas.

Isto falando genericamente. Agora no que toca a sistemas GNU/Linux.

![Gráfico sistema operativo](https://upload.wikimedia.org/wikipedia/commons/7/7b/Free_and_open-source-software_display_servers_and_UI_toolkits.svg)
`Um gráfico das principais peças de um sistema (algumas redundantes).`

Os bootloaders são a peça que inicia o sistema operativo, imediatamente de seguida á BIOS/UEFI.
Entre os genéricos mais comuns de encontrar estão o GNU GRUB(GNU GRand Unified Bootloader), e o SYSLINUX
![](https://upload.wikimedia.org/wikipedia/commons/1/12/GRUB_screenshot.png)
Entretanto tambem há uma nova géração de bootloaders, apenas para UEFI, como o Gummyboot, o rEFInd e o Clover.

O ideal de um bootloader é não ser visível ao utilizador durante mais que breves momentos antes de o sistema operativo arrancar.
No caso de haverem vários sistemas operativos, ou de os parâmetros de arranque de um sistema operativo terem que ser ajustados, é também através desta peça de software.

O bootloader carrega para a memória o kernel, e o mesmo inicia um sistema de init.
O kernel referido é que é o tal Linux. Apenas a peça de software que é carregada na memoria durante os primeiros segundos (ou nem isso no caso de o computador têr um SSD). Essa peça é o componente do sistema com maior importancia. Tudo depende dele, dês de velocidade até segurança.

Altura de tornar a coisa mais gráfica:
![Systemd graph](https://i.imgur.com/edvIhZY.png)
`A minha torre a demonstrar a idade`

Esta imagem é a lista dos daemons que iniciam com o sistema ao longo do tempo.
O primeiro de todos de seguida ao carregamento do kernel é o sistema de Init, ou seja, o daemon que monitoriza e ajuda o kernel a isolar todos os restantes daemons.
Nos sistemas anteriores a 2012 havia um sistema (a mostrar a sua idade) de nome SysVinit, que foi substituído mais recentemente em praticamente todas as distribuições[link para o artigo] pelo SystemD que é o atual sistema de init standard.

Dentro do SystemD há um componente chamado udev que verifica quais os dispositivos de hardware que estão no sistema, e encarrega-se de carregar as drivers como modulos anexados ao kernel.

O mínimo absoluto de um sistema acaba por aqui.
Claramente quer desktops como servidores tem muito mais.

Em um servidor o SystemD continua a carregar daemons com os serviços a disponibilizar, variando com os serviços em questão.

Em um desktop é diferente. Normalmente não há tantos daemons a iniciar. Há no entanto um daemon que é o servidor gráfico.

O servidor gráfico é o serviço que se encarrega de utilizar a gráfica para desenhar um ambiente gráfico no ecrã.
Existem três servidores gráficos de momento. O Xorg (também chamado de X11), que é o mais antigo, o Wayland, e o Mir, estes últimos dois com a ambição de substituir o primeiro.

Existem planos para que o Wayland venha a substituir o Xorg durante o próximo ano estando os portes dos principais ambientes gráficos já praticamente completos no suporte ao mesmo e funcionais.
Do Mir pouco se sabe[que eu saiba] visto que é o esforço maioritariamente de uma só empresa (Canonical, empresa por traz do Ubuntu).

###Ambientes gráficos:
Vêr guia[inserir link]

###Lista de daemons
Os principais daemons de momento que são prováveis de estar no sistema são:

####Pulseaudio:
O servidor de som. Liga-se a um modulo do kernel chamado de ALSA(Advanced Linux Sound Architecture) que por sua vez se liga os dispositivos de hardware atravez da driver adequada.

####NetworkManager:
Um daemon que cria uma abstração sob as ligações de rede e controla-as. Tem também um widget nos principais ambientes gráficos para manipulação das mesmas.

####NTP:
O daemon que implementa o Network Time Protocol, ou seja, um mecanismo de sincronização de tempo que funciona através da Internet. Garante que o tempo no computador está certo.


####DBUS:
Sistema de comunicação entre processos.
Há planos para ser substituído pelo kdbus, com a mesma função mas parte do kernel.


###Outros:

####Bash:
Shell por defeito na maioria do sistemas GNU/Linux. É o interpretador que atua como linha de comandos.

####Glibc:
A livraria (mais utilizada) que implementa as funções standard da linguagem C utilizada a fundo no sistema.
Sem esta livraria o sistema é deixado completamente inutilizável. Sério, experiência própria! :p

#### Tar / Bz / Xz / Gz / Lrz
As ferramentas mais comuns de compressão de ficheiros. A primeira aglomera vários ficheiros em um só preservando a informação, e as restantes são algoritmos de compressão.

####SELinux / AppArmor / Tomoyo:
Sistema de controlos de	acesso. Restringe o que os processos podem fazer para finalidades de segurança. Raramente utilizados em um desktops.

#### GTK / QT / TK / EFL:
Toolkits e livrarias gráficas, que servem principalmente para a criação de widgets gráficos.

### vi / vim / nano / ed
Editores de texto

É garantido que me esqueci de alguma informação. Façam o favor de sugerir edições.