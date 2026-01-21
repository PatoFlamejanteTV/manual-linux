# Fonte de Alimentação (PSU)

A Fonte de Alimentação (PSU) converte a corrente alternada da tomada em corrente contínua para os componentes do PC. Diferente de outros componentes, a PSU raramente comunica dados diretamente ao sistema operacional, a menos que seja uma fonte "inteligente" (digital) conectada via USB ou barramento de dados.

## Monitoramento de Voltagem

Embora não possamos ver o modelo da fonte via software na maioria dos casos, podemos monitorar as voltagens entregues à placa-mãe para verificar a estabilidade.

```bash
sensors
```

Procure por linhas como `+12V`, `+5V` e `+3.3V`.

## Fontes Digitais

Algumas fontes de alto desempenho (como modelos Corsair AXi) podem ser monitoradas via USB usando ferramentas como o `liquidctl` ou drivers específicos do kernel, permitindo ver eficiência, consumo em tempo real e temperatura da unidade.
