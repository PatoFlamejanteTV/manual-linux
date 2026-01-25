# Wine

**Wine** (Wine Is Not an Emulator) é uma camada de compatibilidade capaz de
executar aplicativos Windows em vários sistemas operacionais compatíveis com
POSIX, como Linux, macOS e BSD. Ao contrário de uma máquina virtual ou emulador,
o Wine traduz chamadas de API do Windows em chamadas POSIX em tempo real,
eliminando as penalidades de desempenho e memória de outros métodos.

## Como funciona

Em vez de simular a lógica interna do Windows como uma máquina virtual ou
emulador, o Wine traduz as chamadas de API do Windows para chamadas POSIX em
tempo real, eliminando as penalidades de desempenho e memória de outros métodos
e permitindo que você integre de forma limpa aplicativos Windows em sua área de
trabalho.

## Instalação básica

Geralmente, você pode instalar o Wine através do gerenciador de pacotes da sua
distribuição.

```bash
# Debian/Ubuntu
sudo apt install wine

# Fedora
sudo dnf install wine

# Arch Linux
sudo pacman -S wine
```

### Notas

Pelo menos para mim, todas as vezes que eu tentei usar o WINE/instalar ele na minha máquina eu tive que fazer uma preparação antes, no caso desinstalar todos os pacotes com o nome `wine` (`wine*`) para fazer uma "_instalação limpa_" antes de atualizar ele.

Eu recomendo pesquisar antes de instalar ele, já que é muito fácil acabar com um "_inferno de dependências_" tentando baixar múltiplas versões dele.

## Uso

Para rodar um executável do Windows (.exe):

```bash
wine programa.exe
```

## Winetricks

Uma ferramenta útil para acompanhar o Wine é o `winetricks`, um script auxiliar
para baixar e instalar várias bibliotecas de tempo de execução redistribuíveis
necessárias para rodar alguns programas no Wine.
