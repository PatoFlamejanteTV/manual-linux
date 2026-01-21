# Tails

O Tails (The Amnesic Incognito Live System) é uma distribuição focada obsessivamente em **privacidade e anonimato**. É o sistema operacional recomendado por Edward Snowden.

Ele é baseado no Debian e projetado para ser usado como um "Live System" (rodar de um pen drive/DVD) sem nunca ser instalado no disco rígido do computador.

## Amnésia e Tor

1. **Amnésico:** O Tails não escreve nada no disco rígido. Quando você desliga o computador, a memória RAM é sobrescrita e tudo o que você fez desaparece. Nenhum histórico, senha ou arquivo sobra para contar história (a menos que você configure explicitamente uma partição criptografada persistente no pen drive).
2. **Tor:** Todo o tráfego de internet é forçado a passar pela rede **Tor**. Conexões que tentam burlar o Tor são bloqueadas. Isso esconde seu IP e localização.

## Prós (Vantagens)

1. **Anonimato Máximo:** Configuração pronta para evitar vigilância, censura e rastreamento.
2. **Portabilidade e Segurança:** Pode ser usado em computadores não confiáveis (lan house, hotel) com risco reduzido (embora keyloggers de hardware ainda sejam um risco).
3. **Ferramentas:** Já vem com carteiras de criptomoedas, ferramentas de criptografia (PGP, KeePassXC) e limpeza de metadados.

## Contras (Desvantagens)

1. **Uso Diário:** Não serve para ser seu sistema principal. É lento (devido ao Tor) e inconveniente (perde tudo ao reiniciar).
2. **Restrições:** Muitos sites bloqueiam nós de saída do Tor, tornando a navegação frustrante (muitos CAPTCHAs).
3. **Hardware:** Pode ter problemas com drivers de Wi-Fi proprietários muito novos, pois foca em drivers livres.

## Para Quem é?

* Jornalistas e ativistas em regimes opressivos.
* Whistleblowers (denunciantes).
* Qualquer pessoa que precise realizar uma tarefa sensível com anonimato total e depois desaparecer sem deixar rastros.
