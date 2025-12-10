---
layout: default
---

## Como instalar software e utilizar gestores de pacotes?
Um dos pontos fortes dos sistemas GNU/Linux, que também é uma novidade aos utilizadores de Windows e Mac OS X é a forma de instalar software (e não só).

###Solução do Windows:
Os utilizadores utilizam ficheiros executáveis que podem ser encontrados em qualquer fonte. Esses mesmos ficheiros (que sendo executáveis fazem o que quiserem), têm dentro de si (ou vão buscar á Internet) os ficheiros que constituem um programa, os quais vão colocar numa localização á sua escolha, e eventualmente criam atalhos no menu e no ambiente de trabalho para esses programas.

#### Vantagens:
- Versatilidade
- Flexibilidade

#### Desvantagens:
- Um enorme buraco de segurança
- O executável faz o que quiser, dês de colocar os ficheiros legítimos no local adequado até estragar o sistema
- Dificuldade em determinar a versão de um executável
- Impossibilidade de saber(por parte de um utilizador) exatamente quais os ficheiros que um executável traz.
- Incapacidade de distinguir um executável legitimo de um clone. Existem assinaturas criptográficas que podem ser embutidas nos executáveis, no entanto bastantes executáveis legítimos não as têm, e larga parte dos utilizadores ignora a janela que informa da assinatura e confirma se é realmente desejável continuar a execução.
- Inconsistências na colocação de ficheiros. Tanto podem ir parar a `C:\Programas`, como a `C:\Programas\Jogos`, como apenas a `C:\`, ou até mesmo a `C:\Utilizadores\Utilizador\Programa` e não há nada que a Microsoft possa fazer(de momento) para resolver esse problema.
- Não existe uma forma linear de encontrar o instalador de um programa. Tanto pode estar no site da empresa que desenvolve, numa pagina feita propositadamente para o programa, num arquivo como o SourceForge, o CNET, etc; ou dentro de uma loja de aplicações.
- Quase impossibilidade de remover a totalidade (até á ultima peça) de uma aplicação. Muitas deixam partes consideráveis para traz ou poluem os registos do sistema mesmo depois de desinstaladas pelos métodos oficiais.
- Falta de uniformização, há lugar a perguntas como "Quer instalar a toolbar do XYZ"
- Não há uma forma consistente de atualizar as aplicações.
- Não há uma forma de lidar com dependências. Muitas vezes instala-se n vezes o a mesma dependência para garantir que tudo funciona (Ex: Múltiplas instalações do Microsoft Net Framework, DirectX, Visual Runtime, etc...)

#####Nota:
Dependências são softwares do qual outros softwares dependem para funcionar.
Se um jogo utilizar DirectX, o DirectX é uma dependência do jogo.

- - -
###Solução do Mac OS X:
Os utilizadores procuram no que querem na App Store, e pedem para instalar. É feito o download de um formato de arquivo que tem uma hierarquia de ficheiros nas localizações destino, e os mesmos são extraídos para os locais certos.
Aquando da desinstalação o inverso é feito deixando o sistema limpo.

####Vantagens:
- Uma certa garantia de segurança, visto que há processos de aprovação na App Store e um custo envolvido
- Uniformização.
- Simplicidade de utilização.
- Desinstalações completas
- Lida com dependências (Alguém confirma?)

####Desvantagens:
- Aplicações sujeitas ás vontades e termos da Apple.
- Centralização.
- Instalação de aplicações de fora da App Store, visto que envolve retirar uma check box que muitos entendem como "deixar-me por minha conta e privar-me da segurança".
- Custos de desenvolvimento.

#### Nota:
Algum utilizador de OS X que retifique, porque não sou um, e falo com duas horas de experiencia.
- - -
###Solução em sistemas GNU/Linux:
Cada distribuição tem repositórios oficiais com pacotes (que são como os arquivos do OS X), dentro dos repositórios oficiais estão vários milhares de pacotes, entre eles os que constituem o sistema, mas também bastantes aplicações que servirão para a maior parte das necessidades dos utilizadores.
Dependendo das políticas de cada distribuição e da mão de obra que a mesma tem disponível é que se determina quais os pacotes disponíveis nos repositórios oficiais. Por exemplo uma distribuição com uma boa quantidade de mão de obra e sem uma política de exclusividade a software opensource, terá nos repositórios softwares como o Opera, a Steam, o Skype, etc...; enquanto que uma que tenha exclusividade a opensource não terá essas aplicações nos repositórios oficiais.
No entanto a flexibilidade está na capacidade do utilizador adicionar os repositórios que bem entender.
Se uma empresa de software providenciar um repositório para os seus programas, o utilizador pode adicionar o repositório, e instala os programas dessa empresa como se qualquer outro software se tratasse.
E o melhor é que quando o sistema verificar por atualizações, também vai verificar os repositórios não oficiais, sendo mesmo uma atualização completa ao sistema.

####Vantagens:
- Se todos os repositórios tiverem chave, há uma garantia de segurança de onde o software vem. Que foi mesmo feito por determinada entidade ou comunidade.
- Facilidade de instalação de software.
- Capacidade para atualizar o sistema integralmente
- Desinstalações completas
- Uniformização`*`
- Sistema descentralizado
- Lida com dependências

####Desvantagens:
- Pode ser difícil encontrar repositórios para todos os software em uma das distribuições não principais
- Discórdia entre as distribuições em qual o formato correto de pacote a utilizar.`*`
- Como não há nada que impeça uma instalação similar ao Windows, há alguns poucos softwares que vem 'entalados' dentro de scripts. Nas distros com mão de obra para tal, o que é feito pelos desenvolvedores é extrair a aplicação do script, converte-la a um pacote, e coloca-la num repositório, mas há empresas que não dão autorização para que isso seja feito(teimosia?).

#####Nota:
`*` - Supondo que um formato de pacote standard venha a ser aceite por parte de todas as distribuições. Por agora existem dois principais; o `.deb`(distribuições baseadas em Debian) e o `.rpm`(distribuições baseadas em Red Hat ou SUSE), mas ainda há mais dentro de formatos genéricos de arquivos.
O problema passa por ser que um pacote para Debian pode não funcionar em Ubuntu(que é baseado em Debian), ou um para Red Hat não funcionar em SUSE; e vice versa, porque os sistemas tem diferenças, mesmo que utilizem o mesmo formato de pacote.
Decidir um formato standard é um trabalho em desenvolvimento, que é por muitos considerado vital para dar alguma consistência ao mundo GNU/Linux, mas ainda há muitas disputas onde deveria de haver colaboração.
Até lá a norma é empacotar para Ubuntu, e as restantes comunidades adaptam os pacotes do Ubuntu aos seus.

![Popup download Google Chrome](https://i.imgur.com/wLJ4tpI.png)
`Exemplo de uma entidade que fornece pacotes genéricos no formato .deb e .rpm`
`Popup download do Google Chrome`

- - -

###Ok ok, teoria suficiente, eu quero instalar coisas, como faço?

Cada distribuição tem o seu gestor de pacotes, que é um programa que se encarrega de encontrar pacotes nos repositórios, fazer download de pacotes, instalar pacotes, atualiza-los e desinstala-los.

Há varios gestores de pacotes, mas os mais comuns são o apt(Ubuntu, Debian, Mint), o yum que será substituido pelo DNF em breve(Red Hat, Fedora), o zypper(SUSE, OpenSUSE), o Pacman(Arch, Manjaro, Antergos) e o Portage(Gentoo).

Cada distribuição tem a sua interface gráfica para utilizar o gestor de pacotes (são poucas as que não tem), no entanto variam muito de distribuição para distribuição e teria que fazer um guia por cada uma, por isso a forma genérica é utilizar comandos.

Os comandos são introduzidos num terminal(linha de comandos), e todos os que envolverem ações administrativas tem que ser executados como administrador.
Para executar um comando como administrador, prefixe `sudo` em uma distribuição que tenha a ferramenta "sudo" instalada (maior parte vem com ela por defeito), e ai escreve a password(não é visível) e prime `Enter`.
Se a distribuição não tiver a ferramenta instalada, para fazer login como administrador escreve `su` e a password de administrador, e depois o comando que quer executar.
==Tomar ações que não as estritamente necessárias como administrador é perigoso. Não faça do Linux um Windows!==

![Package managers roseta](https://i.imgur.com/lzXoeT2.png)
A) Instalar o pacote.
B) Desinstalar o pacote.
C) Procurar pelo pacote nos repositórios.
D) Atualizar os repositórios locais e atualizar o sistema
E) Atualizar a versão do sistema (Ex: Ubuntu 14.10 para 15.04)
F) Reinstalar o pacote.
G) Instalar o pacote local (seguido do caminho do ficheiro)
H) Verificar por problemas nas bases de dados dos pacotes.
I) Desinstalar dependências(pacotes) que ficaram órfãs.(sem nenhum outro pacote que necessite delas)
J) Limpar as caches. (É deixada uma copia de todos os pacotes na cache. Este comando apaga as copias)

Esta tabela é uma adaptação [desta](https://wiki.archlinux.org/index.php/Pacman_Rosetta) que é muito mais completa (e complicada). Um gestor de pacotes pode ser algo muito poderoso caso o utilizador o deseje, mas para uma utilização básica isto chega.

####Nota:
- Os comandos executados como administrador assumem que tem mais que dois palmos de inteligência e sabe o que faz. Não experimente desinstalar componentes críticos ao sistema, porque vai funcionar!


###Mas, eu fiz o download de um programa e veio um ficheiro `tar.gz`/`tar.bz`. O que faço?
Quando faz o download de programas pelos sites, pode ás vezes vir um ficheiro `tar.***`.
Esses ficheiros são meros arquivos(como um ficheiro `zip`, um `7z` ou um `rar`), não pacotes, e apesar de muitos deles terem uma hierarquia bem definida e uma forma de instalar, não é recomendado que o faça.

Lá dentro pode tanto estar binário(executáveis) como apenas o código fonte para os fazer, e não vão instalar qualquer dependência.

Se tiver forçosamente que utilizar um software num arquivo(por não o ter em nenhum repositório), não o instale.
No explorador de ficheiros, vá ás propriedades do ficheiro que julgue ser o binário principal(caso tenha executáveis), marque-o como executável(é uma prevenção de segurança) e execute-o com um click duplo (pode variar).
![Exemplo](https://i.imgur.com/WZWT2kN.png)
`Exemplo com os ficheiros do Firefox no GNOME, explorador de ficheiros Nautilus`

Alternativamente os comandos são `chmod +x firefox` para mudar as permições e `./firefox` para executar.

**PS:** É um mero exemplo, poupem a vossa sanidade e não executem o Firefox a partir de um arquivo a não ser que tenham mesmo que o fazer. Se por algum motivo obscuro a vossa distribuição não o tiver instalado por defeito, ele estará nos repositórios.

###De futuro:
Um guia mais especifico ás principais distribuições, para que se faça o mesmo sem recurso à linha de comandos.