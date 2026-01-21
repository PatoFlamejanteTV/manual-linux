# Refrigeração (Cooling)

O sistema de refrigeração é vital para manter a temperatura dos componentes (CPU, GPU, VRMs) dentro de limites seguros. Pode ser a ar (Air Cooler) ou líquido (Water Cooler).

## Monitoramento de Temperaturas e Fans

No Linux, o pacote `lm-sensors` é essencial para ler os sensores de temperatura e velocidade das ventoinhas (RPM).

1. Detecte os sensores:

```bash
sudo sensors-detect
```

1. Verifique os dados:

```bash
sensors
```

## Controle de Ventoinhas

Ferramentas como `fancontrol` (parte do lm-sensors) permitem criar curvas de ventoinha personalizadas baseadas na temperatura.

```bash
sudo pwmconfig
```

Isso ajuda a configurar um sistema mais silencioso ou com maior performance térmica.
