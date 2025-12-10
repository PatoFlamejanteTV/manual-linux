# Cron

O **cron** é um *daemon* utilizado em sistemas operacionais do tipo Unix para executar tarefas agendadas em segundo plano. Essas tarefas, conhecidas como **cron jobs**, são executadas em horários ou intervalos específicos.

O cron é ideal para automatizar tarefas repetitivas, como backups, atualizações de sistema, envio de e-mails e execução de scripts de manutenção.

## O arquivo crontab

A configuração dos cron jobs é feita através de um arquivo chamado **crontab**. Cada usuário do sistema pode ter seu próprio crontab, além de um crontab de sistema.

Para editar o seu crontab, utilize o comando:

```bash
$ crontab -e
```

### Sintaxe do crontab

Cada linha em um arquivo crontab representa um job e segue a seguinte sintaxe:

`minuto hora dia_do_mês mês dia_da_semana comando`

| Campo | Valores | Descrição |
|---|---|---|
| minuto | 0-59 | O minuto em que o comando será executado. |
| hora | 0-23 | A hora em que o comando será executado. |
| dia_do_mês | 1-31 | O dia do mês em que o comando será executado. |
| mês | 1-12 | O mês em que o comando será executado. |
| dia_da_semana | 0-7 | O dia da semana em que o comando será executado (0 e 7 representam Domingo). |

Você pode usar um asterisco (`*`) em qualquer um desses campos para indicar "todos".

## Exemplos

Aqui estão alguns exemplos de cron jobs:

```bash
# Executa um script de backup todos os dias à 1h da manhã
0 1 * * * /home/user/scripts/backup.sh

# Executa um script de limpeza a cada 15 minutos
*/15 * * * * /home/user/scripts/limpeza.sh

# Executa um comando no primeiro dia de cada mês
0 0 1 * * /usr/bin/echo "Feliz mês novo!"

# Executa um script toda segunda-feira às 9h
0 9 * * 1 /home/user/scripts/relatorio_semanal.sh
```

## Dicas

* Use o caminho completo para os comandos e scripts para evitar problemas com a variável de ambiente `PATH`.
* Redirecione a saída dos seus scripts para um arquivo de log para poder depurar problemas: `* * * * * /path/to/command > /path/to/logfile.log 2>&1`
* Verifique os logs do sistema (geralmente em `/var/log/cron` ou `/var/log/syslog`) para ver se seus cron jobs estão sendo executados corretamente.
