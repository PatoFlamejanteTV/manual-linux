# Steam

A **Steam** é a maior plataforma de distribuição digital de jogos para PC. A
Valve, empresa por trás da Steam, tem sido a maior impulsionadora dos jogos no
Linux nos últimos anos, especialmente com o desenvolvimento do Proton e o
lançamento do Steam Deck.

## Instalação

A maioria das distribuições Linux possui a Steam em seus repositórios oficiais.

```bash
# Debian/Ubuntu
sudo apt install steam

# Fedora (requer repositórios RPM Fusion habilitados)
sudo dnf install steam

# Arch Linux (habilite o repositório multilib)
sudo pacman -S steam
```

## Flatpak

A versão Flatpak da Steam também é muito popular e funciona bem em diversas
distribuições, isolando o cliente do resto do sistema.

```bash
flatpak install flathub com.valvesoftware.Steam
```

## Dicas

- **Drivers:** Certifique-se de estar usando os drivers de vídeo mais recentes
  para sua GPU (especialmente Nvidia) para garantir o melhor desempenho.
- **Vulkan:** A Steam no Linux depende muito da API Vulkan, então certifique-se
  de que sua placa de vídeo suporte e tenha as bibliotecas Vulkan instaladas.
