# cron

O **cron** é um agendador de tarefas baseados em tempo. O comando para editar tarefas é o `crontab`.

## Editar o crontab do usuário

```bash
crontab -e
```

## Listar tarefas agendadas

```bash
crontab -l
```

## Sintaxe básica

```text
# m h  dom mon dow   command
* * * * * comando_a_rodar
```
