---
layout: default
---

## Guia dos guias:
### **Os guias são:**
- Imparciais, não ambicionando criar qualquer disputa entre comunidades, sendo que normalmente (consoante o bom senso) apenas deverão de ter um teor comparativo quando o tema do guia o pressupor.
- Genéricos, a não ser que seja explicito o contrario. Um guia para "fazer A" não pode funcionar só em B, mas um guia para "Fazer A em B" não tem qualquer problema.
- Simples. A ambição dos guias é facilitar a utilização aos novos utilizadores, não assustar os mesmos com matérias avançadas e muitos termos técnicos. Um guia que não seja destinado a utilizadores inexperientes deve de ser explicito quanto a isso.
- [Opcional] Agrupados em um [repositório de GIT](https://github.com/SirOfTheRepo/zwame-guias-linux/), para que a comunidade os possa alterar após o autor os ter criado(mediante pedido à moderação no caso de o autor não manifestar atividade). Quem não souber utilizar o GIT pode contribuir com alterações diretamente neste tópico, e tal é o recomendado visto que assim alterações podem ser aprovadas pela comunidade e não apenas pelo dono do repositório.
- Escritos em markdown (se de acordo com a alínea anterior). Trata-se de uma linguagem similar ao BBcode que o fórum utiliza, com vários editores gráficos, e sem qualquer barreira de adoção dada a simplicidade da sintaxe.

### **Ferramentas para escrever guias em markdown**
Existem varias ferramentas para escrever markdown, duas que valem a menção são:
#### [Haroopad](http://pad.haroopress.com/)
<img src="https://i.stack.imgur.com/wu5gF.png"/>
Editor cross-platform, com uma interface muito simples.
Existe (aquando da altura da escrita deste guia) um quadrado azul no canto inferior esquerdo, que quando premido faz com que apareça uma barra lateral com as formatações comuns de utilizar.
O Haroopad não tem uma forma embutida de inserir imagens. Em markdown as mesmas tem que ser inseridas com código HTML. Para quem não saiba HTML, o código para inserir uma imagem é `<img src="http://link.para.a.imagem">`, tudo o resto não deve de haver qualquer problema com as ferramentas que o Haroopad traz embutidas.

#### [StackEdit](https://stackedit.io/)
<img src="https://stackedit-beta.herokuapp.com/res-min/img/logo-promo-128.png">
Um editor que não instalação pois porque funciona no browser através da própria página.
Bastante intuitivo de utilizar, e até com um mini-guia. Não deverá de haver qualquer duvida.

### **Porquê o GIT?:**
O GIT é um sistema de versionamento que (sobre-simplificando) cria um repositório que ordena as contribuições(commits), se pode mover no tempo para qualquer contribuição feita, e possibilita ver as diferenças que cada contribuição insere sobre a anterior.
A comunidade de Power Users de GNU/Linux frequentemente conhece o funcionamento do mesmo, de modos que se trata da escolha mais adequada, até porque possibilita a qualquer interessado o download do repositório com os guias todos para visualização offline.
Utilizando um sistema destes permite que os tópicos não fiquem presos no tempo, o que pode fazer com que um guia deixe de funcionar para um utilizador inexperiente que não será capaz de determinar o porquê.

### **Como ver os guias offline:**
[Inserir img download github]
A forma mais simples é utilizar o botão de download que se encontra na barra lateral (direita) do repositorio no GitHub[URL], mas o comando `git clone https://github.com/maintainer/repo.git` tambem funcionará para fazer download para a pasta actual caso o git esteja instalado no sistema.
Descomprimindo o ZIP que será descarregado deverá de haver uma pasta dentro do mesmo chamada "Guias", a qual terá ficheiros de markup, que terão que ser abertos com um visualizador como o Haroopad (visto que o utilizador se encontra offline).

Boas contribuições