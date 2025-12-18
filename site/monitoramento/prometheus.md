# Prometheus

O **Prometheus** é um sistema de monitoramento e banco de dados de séries
temporais _open-source_. Ele é muito popular no ecossistema _cloud native_.

## Como funciona

O Prometheus coleta métricas de seus alvos (serviços instrumentados) raspando
endpoints HTTP (geralmente `/metrics`).

```bash
# Exemplo de configuração simples (prometheus.yml)
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
```

Ele usa uma linguagem de consulta chamada **PromQL** para selecionar e agregar
dados em tempo real.
