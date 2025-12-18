# Modelo OSI

O **Modelo OSI** (Open Systems Interconnection) é um modelo conceitual que
caracteriza e padroniza as funções de comunicação de um sistema de
telecomunicações ou de computação sem levar em conta a estrutura interna e a
tecnologia subjacente.

## As 7 Camadas

O modelo é dividido em 7 camadas, da mais baixa (física) para a mais alta
(aplicação):

1. **Física (Physical)**: Transmissão e recepção dos dados brutos não
   estruturados através de um meio físico (cabos, fibra, ondas de rádio).
   Trata de bits, voltagens e frequências.
2. **Enlace de Dados (Data Link)**: Transfere dados entre nós adjacentes na
   rede (WAN ou LAN). Trata de quadros (frames) e endereços MAC. (Ex:
   Ethernet, Wi-Fi).
3. **Rede (Network)**: Estrutura e gerencia uma rede com múltiplos nós,
   incluindo endereçamento, roteamento e controle de tráfego. Trata de pacotes
   e endereços IP. (Ex: IP, ICMP).
4. **Transporte (Transport)**: Transferência confiável de dados entre pontos,
   controle de fluxo e correção de erros. Trata de segmentos. (Ex: TCP, UDP).
5. **Sessão (Session)**: Gerencia sessões de comunicação (diálogos) entre
   computadores. Estabelece, gerencia e termina conexões.
6. **Apresentação (Presentation)**: Tradução de dados entre o serviço de rede
   e a aplicação (codificação, criptografia, compressão). (Ex: SSL/TLS).
7. **Aplicação (Application)**: Camada mais próxima do usuário final. Fornece
   interfaces para aplicações acessarem serviços de rede. (Ex: HTTP, FTP,
   SMTP).

## Mnemônico

Uma frase comum para lembrar a ordem (de baixo para cima) é:
**F**ui **E**m **R**oma **T**entar **S**alvar **A**lguém.
