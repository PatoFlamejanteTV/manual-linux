# NixOS

O NixOS é uma distribuição única, construída sobre o gerenciador de pacotes **Nix**. Ela aborda o gerenciamento do sistema de uma forma completamente diferente, focando em **reprodutibilidade** e **configuração declarativa**.

## O Conceito Declarativo

Em distros tradicionais, você instala pacotes e edita arquivos em `/etc` manualmente. Se formatar o PC, precisa lembrar de tudo o que fez.

No NixOS, todo o estado do sistema é descrito em um único arquivo de configuração (`/etc/nixos/configuration.nix`). Você declara:

* "Quero o Firefox instalado."
* "Quero o usuário 'joao'."
* "Quero o serviço SSH ativado na porta 22."

Ao aplicar a configuração (`nixos-rebuild switch`), o sistema cria exatamente esse estado. Se você copiar esse arquivo para outro PC, terá um clone exato do sistema.

## Imutabilidade e Rollbacks

O NixOS é imutável. Quando você atualiza o sistema, ele não sobrescreve os arquivos antigos. Ele cria uma nova "geração" do sistema e aponta os links para ela.
Se a atualização quebrar o PC, você pode reiniciar e escolher a "geração anterior" no menu de boot. O sistema volta exatamente como estava antes, garantido.

## Prós (Vantagens)

1. **Indestrutível:** Atualizações nunca deixam o sistema num estado inconsistente. Rollback é trivial.
2. **Reprodutibilidade:** Perfeito para ambientes de desenvolvimento e servidores. "Funciona na minha máquina" torna-se verdade global se a config for a mesma.
3. **Nixpkgs:** Um repositório gigantesco de software, comparável ou maior que o AUR/Debian.

## Contras (Desvantagens)

1. **Curva de Aprendizado:** Você precisa aprender a linguagem Nix. Não dá para seguir tutoriais genéricos de Linux (ex: "edite o /etc/fstab") porque o NixOS sobrescreve arquivos manuais.
2. **Binários Externos:** Baixar e rodar um binário qualquer da internet muitas vezes não funciona porque os caminhos das bibliotecas no NixOS são diferentes (não ficam em `/lib`, mas em `/nix/store/...`). É preciso usar ferramentas como `steam-run` ou empacotar o software.
3. **Complexidade Inicial:** Configurar coisas simples pode exigir leitura de documentação.

## Para Quem é?

* Desenvolvedores de software e DevOps.
* Pessoas que amam "Infrastructure as Code" (Infraestrutura como Código).
* Quem gosta de experimentar tecnologias de ponta e conceitos novos de sistemas operacionais.
