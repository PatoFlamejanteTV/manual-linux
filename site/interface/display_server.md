# Servidor de Exibição (Display Server)

O servidor de exibição é a camada fundamental que coordena a entrada e saída
dos seus dispositivos (teclado, mouse, monitor) com o sistema operacional e os
aplicativos gráficos.

## X11 (X Window System)

O padrão histórico do Linux e Unix.

* **Vantagens:** Extremamente maduro, estável, funciona em praticamente
  qualquer lugar, permite encaminhamento de rede (rodar app numa máquina e
  ver noutra).
* **Desvantagens:** Código antigo e complexo, não foi projetado para o
  hardware moderno, possui problemas de segurança (qualquer app pode ver o
  que os outros estão fazendo, como keylogging).

## Wayland

O protocolo moderno destinado a substituir o X11.

* **Vantagens:** Mais seguro (isolamento entre aplicativos), mais leve,
  projetado para hardware moderno, elimina problemas como screen tearing.
* **Desvantagens:** Ainda em adoção, algumas aplicações antigas podem não
  funcionar perfeitamente sem camadas de compatibilidade (XWayland), e
  algumas ferramentas de gravação de tela ou acesso remoto exigem adaptações.
