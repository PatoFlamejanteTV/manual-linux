# netstat

O **netstat** exibe conexões de rede, tabelas de roteamento e estatísticas de interfaces. Embora depreciado em favor do `ss`, ainda é muito comum.

## Listar todas as portas e conexões

```bash
netstat -a
```

## Listar apenas portas ouvindo (listening)

```bash
netstat -l
```

## Mostrar programa/PID associado

```bash
sudo netstat -lnp
```
