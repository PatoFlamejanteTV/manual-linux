# Gentoo

Gentoo é uma distribuição Linux conhecida por sua extrema configurabilidade e performance. Diferente da maioria das distros que fornecem pacotes binários pré-compilados (como Debian ou Fedora), no Gentoo você [compila](../conceitos/compilation.md) quase tudo a partir do código-fonte na sua própria máquina.

Isso permite que o sistema seja otimizado especificamente para o seu hardware (CPU, instruções) e para as suas necessidades exatas. O mascote do Gentoo é o Larry the Cow (Larry, a Vaca).

## Características Principais

### Portage e o comando `emerge`

O coração do Gentoo é o **Portage**, seu [gerenciador de pacotes](../conceitos/package_manager.md). Ele é inspirado no sistema de ports do BSD e é escrito em Python. Diferente do `apt` ou `dnf` que baixam um `.deb` ou `.rpm`, o Portage baixa o código-fonte, aplica patches necessários e compila o software.

O comando principal é o `emerge`. Exemplo de instalação do Firefox:

```bash
emerge --ask www-client/firefox
```

### USE Flags

As **USE flags** são a característica mais poderosa do Gentoo. Elas permitem que você defina globalmente (no arquivo `/etc/portage/make.conf`) ou por pacote, quais funcionalidades você quer habilitar ou desabilitar na hora da compilação.

Por exemplo, se você não usa KDE no seu sistema, você pode adicionar `-kde` nas suas USE flags. Isso fará com que qualquer programa que você instale seja compilado *sem* suporte ao KDE, economizando espaço, reduzindo dependências e deixando o programa mais leve.

Exemplo de configuração:

```bash
USE="pulseaudio -systemd -gnome X alsa"
```

Neste exemplo, estamos habilitando suporte a PulseAudio, X11 e ALSA, mas desabilitando explicitamente systemd e GNOME.

### Escolha de Init System

Enquanto a maioria das distros padronizou no [systemd](../conceitos/systemd.md), o Gentoo oferece liberdade de escolha. O padrão oficial é o **OpenRC**, um sistema de init clássico, simples e rápido, baseado em scripts de shell. No entanto, é perfeitamente possível instalar e usar o systemd se o usuário preferir.

## Instalação: O "Handbook"

A instalação do Gentoo é famosa por ser complexa e longa. Não existe um instalador gráfico oficial "Next, Next, Finish". O usuário deve seguir o **Gentoo Handbook**, um manual detalhado que guia o processo de particionamento, descompactação do "stage3" (sistema base), configuração do [Kernel](../conceitos/kernel.md), compilação do sistema e instalação do bootloader.

Instalar o Gentoo é considerado um rito de passagem e uma das melhores formas de aprender como o Linux funciona "por baixo do capô".

## Prós (Vantagens)

1. **Otimização e Performance:** Todo o software é compilado para a sua arquitetura específica (`-march=native`), aproveitando todas as instruções do seu processador.
2. **Customização Extrema:** Você escolhe cada biblioteca instalada. Nada entra no sistema sem sua permissão (ou sem ser uma dependência estrita).
3. **Rolling Release:** O Gentoo está sempre atualizado.
4. **Aprendizado:** Você aprende sobre dependências, compilação, kernel e estrutura do sistema Linux.

## Contras (Desvantagens)

1. **Tempo de Compilação:** Compilar grandes softwares como navegadores (Chromium, Firefox) ou suítes de escritório (LibreOffice) pode levar horas, dependendo do processador.
2. **Complexidade:** A curva de aprendizado é íngreme. Erros de compilação podem ocorrer e exigem leitura de logs para resolver.
3. **Manutenção:** Atualizar o sistema ("world update") pode demorar e ocasionalmente requer intervenção manual para resolver conflitos de configuração.

## Para quem é?

Gentoo é voltado para **usuários avançados** (power users), desenvolvedores e entusiastas que querem controle total e absoluto, e que não se importam em trocar tempo de CPU (compilação) por um sistema feito sob medida.
