# TCP/IP

O conjunto de protocolos de Internet, comumente conhecido como **TCP/IP**, é a
arquitetura de protocolos usada na Internet e na maioria das redes comerciais.

## Principais Protocolos

O nome vem de dois dos protocolos mais importantes do conjunto:

1. **TCP (Transmission Control Protocol)**:
   * **Orientado a conexão.**
   * **Garante a entrega dos dados (confiável).**
   * **Ordena os pacotes.**
   * **Realiza controle de fluxo e congestionamento.**
   * **Mais lento devido ao *overhead* de verificação.**
   * **Usado em**: Web (HTTP), E-mail (SMTP), Transferência de arquivos (FTP).

2. **IP (Internet Protocol)**:
   * **Responsável pelo roteamento e endereçamento dos pacotes.**
   * **Não garante a entrega (best effort).**
   * **Versões principais**: IPv4 (32 bits) e IPv6 (128 bits).

3. **UDP (User Datagram Protocol)**:
   * **Não orientado a conexão (connectionless).**
   * **Não garante a entrega nem a ordem.**
   * **Mais rápido e leve.**
   * **Usado em**: Streaming de vídeo/áudio, Jogos online, DNS.

## Comparação Modelo TCP/IP vs OSI

O modelo TCP/IP é geralmente descrito em 4 camadas, mapeando para as 7 camadas
do modelo OSI:

* **Aplicação** (OSI: Aplicação, Apresentação, Sessão)
* **Transporte** (OSI: Transporte)
* **Internet** (OSI: Rede)
* **Acesso à Rede** (OSI: Enlace de Dados, Física)
