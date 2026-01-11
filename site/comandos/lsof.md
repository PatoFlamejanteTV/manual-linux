# lsof

O **lsof** (List Open Files) lista informações sobre arquivos abertos por processos.

## Arquivos abertos por um usuário

```bash
lsof -u usuario
```

## Quem está usando uma porta?

```bash
lsof -i :80
```

## Quem está usando um arquivo/diretório?

```bash
lsof /var/log/syslog
```
