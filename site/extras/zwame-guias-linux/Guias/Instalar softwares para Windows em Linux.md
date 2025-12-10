---
layout: default
---

##Como instalar softwares do Windows em GNU/Linux
Antes de mais nada saliento que não apoio que o façam.
É mau utilizar softwares não nativos por muitos motivos:
- Bugs.
- Mais bugs.
- Disparidade de performance em implementações incompletas.
- Passam por ser cota de mercado do Windows, porque provavelmente os autores do software não vão ser capazes de distinguir.
- Dão a entender que podem utilizar os softwares através de hacks, e como tal as empresas não se importam a portar.
- Perdem o direito a qualquer suporte.
- Em certos jogos podem ser ativadas proteções contra hacks, sem estar a ser utilizado qualquer hack.
- O Wine(software utilizado) tem muitas dependências, e se não tiverem mais nada de 32 bits no sistema, é possível que o mesmo praticamente duplique de tamanho.
- Regressões

Quando é que é aceitável fazê-lo?
- Não há alternativa e só necessito de um único programa (dois/três no máximo).
- Não tenho uma licença do Windows e quero-me manter 100% legal.

Ou seja:
- (**Mau**) Jogo Skyrim, WoW, Sims, FarCry e LoL e todos eles funcionam no Wine. Se quero utilizar Linux logo vou joga-los a todos no Wine.
- (**Péssimo**) Utilizo o Photoshop, o Illustrator, e mais 20 ferramentas gráficas para trabalhar, todas no Wine.
- (**Sem comentário**) A ferramenta super critica para o funcionamento da empresa parece trabalhar no Wine.
- (**Razoavel**) Jogo maioritariamente CS e DotA(jogos já portados), mas não consigo deixar o vicio do Skyrim.

**Ou seja**: Se querem utilizar Linux como se utilizassem o Windows, utilizem o Windows. Não há nada que impeça os dois de coexistir seja em dual-boot ou numa maquina virtual(que por sinal é um dos pontos fortes do Linux).

Se os programas forem leves e não requererem grande aceleração gráfica, uma maquina virtual pode ser uma solução.
Para isso o ideal é utilizar KVM com o virt-manager(interface gráfica) que fica com uma velocidade quase nativa (exceto placa gráfica).
Um tutorial nessa matéria pode vir a existir na eventualidade de se demonstrar interesse.

Vou tentar manter o artigo simples e intuitivo, por isso vou utilizar um wrapper (software que funciona em torno do Wine) chamado PlayOnLinux.
O Wine só por si pode ser uma peça de software muito complexa, que pode demorar horas ou mesmo dias a experimentar para se colocar certos softwares a funcionar, e há alguns que não funcionam de todo por necessitarem de algo ainda não implementado ou por bugs.

No entanto o PlayOnLinux tem uma lista de software suportado [aqui](https://www.playonlinux.com/en/supported_apps.html).

O que necessita não está nesta lista? Essa lista que indiquei são softwares com instruções de instalação para o POL(vou passar a abreviar o nome), não todos os softwares que são conhecidos por funcionar com o Wine ([para o Wine é esta](https://appdb.winehq.org/)) no entanto está fora do âmbito deste guia utilizar diretamente o Wine. Se instalar pelas instruções que encontram na segunda lista então boa sorte, porque não há guia possível porque cada caso é um caso.

**Nota para quem queira utilizar o Wine diretamente**: Se não houverem instruções por norma para executar utiliza-se o comando `wine /caminho/para/o/software.exe` e para instalar dependências (directx, flash, etc...) utiliza-se um utilitário que pode ou não vir com o wine chamado winetricks.(comando `winetricks`). Configurações do sistema é o comando `winecfg`. Uma sugestão é que criem explicitamente uma instância do Wine em 32 bits, e não a 64. Procurem por `32bit wineprefix` em um motor de busca e devem de encontrar como o fazer.
Isto também pode ser feito dentro da interface do POL se for uma instalação manual.


####De volta ao POL.
(Não tenho o POL instalado, por isso as imagens não são minhas; Alguém que faça o favor de trocar)
![Janela](https://www.playonlinux.com/images/playonlinux_screenshots/install_wizard.png)
`Interface principal`

Eis a interface que verão quando abrirem o POL. Deverá de ser vagamente intuitivo de utilizar; Um botão para executar, um para parar a execução(caso dê para o torto), um para instalar algo, um para apagar, e configurações.

Podem também executar programas instalados através do menu do sistema operativo ou por atalhos que o POL cria no ambiente de trabalho. Caso os atalhos não existam e os prefira, há uma forma de criar nas configurações. [Alguém que confirme]

Quando carregar no botão de instalação isto será o que vai ver:
![Instalação](https://www.playonlinux.com/images/playonlinux_screenshots/program.png)
Uma lista de aplicações. A lista que o link referido tinha.(Note que pode ter que marcar os check boxes no topo da lista para ver certas aplicações)

É agora uma questão de pesquisar e carregar em instalar. (Note o link em baixo para instalar software não listado)

Cada instalador é diferente, mas deverá de aparecer uma janela com instruções a guia-lo e a indicar o que deve de fazer. Tome atenção porque ás vezes a mesma tem informação importante.
![Janela de instalação](https://www.playonlinux.com/images/playonlinux_screenshots/install.png)


####Quando a coisa dá para o torto
Nos links na parte esquerda da primeira imagem, há um que diz debug(quando em inglês); carregue nesse link e o programa será executado e uma janela aberta à parte. Nessa janela estarão os erros gerados pelo programa. Terá que os interpretar e corrigir por si. Pode ser algo que falte no sistema, pode ser bug do Wine, pode ser bug do programa.

**Nota**:
O Wine só por si, sem problema algum, já larga muita informação na janela de debug do POL que passa por ser erros, mas não o é necessariamente. Podem ser coisas que o Wine ainda não tenha implementado, mas não sejam criticas ao programa.