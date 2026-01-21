# Slackware

O Slackware é a distribuição Linux mais antiga que ainda está sendo mantida (lançada em 1993). Ela tem uma filosofia muito distinta: **KISS (Keep It Simple, Stupid)**. No entanto, "simples" para o Slackware significa "simples do ponto de vista da arquitetura do sistema", e não necessariamente "fácil de usar" para o usuário final.

O Slackware tenta ser o mais próximo possível do Unix, modificando o software original (upstream) o mínimo possível.

## Filosofia e Gerenciamento de Pacotes

Diferente de Debian ou Fedora, o gerenciador de pacotes do Slackware (`pkgtool` / `slackpkg`) **não resolve dependências automaticamente**. Se você instalar o programa A, e ele precisar da biblioteca B, o Slackware não vai baixar a biblioteca B para você. Você deve saber disso e instalar a biblioteca B manualmente.

Isso dá ao administrador controle total sobre o que está instalado, mas exige conhecimento.

## Inicialização (Init System)

O Slackware é famoso por **não** usar o systemd, que se tornou padrão na maioria das distros modernas. Ele usa um sistema de scripts de inicialização estilo **BSD** (`/etc/rc.d`), que são simples scripts de shell fáceis de ler e editar.

## Prós (Vantagens)

1. **Aprendizado:** Dizem que "se você usa Ubuntu, aprende Ubuntu; se usa Slackware, aprende Linux". Você entende como o sistema funciona por baixo do capô.
2. **Estabilidade (Rocha Sólida):** O sistema é extremamente testado e conservador.
3. **Sem Surpresas:** O sistema não faz nada que você não tenha mandado explicitamente.
4. **Simplicidade Arquitetural:** Scripts legíveis, configurações em texto plano onde você espera que estejam.

## Contras (Desvantagens)

1. **Gerenciamento de Dependências:** Manual. Pode ser um pesadelo ("Dependency Hell") para usuários novos que querem instalar softwares complexos.
2. **Software Antigo:** As versões estáveis podem demorar anos para serem lançadas.
3. **Curva de Aprendizado Vertical:** Exige uso constante do terminal e edição de arquivos de config.

## Para Quem é?

* Administradores de sistemas "Old School".
* Estudantes que querem entender profundamente como o Linux funciona.
* Pessoas que detestam o systemd e preferem scripts de init simples.
* Servidores que precisam de estabilidade extrema e manutenção manual controlada.
