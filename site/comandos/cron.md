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

## Exemplos comuns

Agendar para rodar todo dia à meia-noite (00:00):
```text
0 0 * * * /home/usuario/backup.sh
```

A cada 5 minutos:
```text
*/5 * * * * /home/usuario/script.sh
```

## Variáveis de Ambiente

No topo do arquivo crontab, você pode definir variáveis:

```text
PATH=/usr/sbin:/usr/bin:/sbin:/bin
MAILTO=meuemail@exemplo.com
```

**Dica**: É comum o cron falhar porque o PATH é diferente do seu terminal. Sempre use caminhos absolutos (`/usr/bin/python3`) nos seus comandos.

