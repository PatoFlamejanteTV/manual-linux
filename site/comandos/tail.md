# tail

O comando `tail` (do inglês, "cauda") é o oposto do comando `head`. Ele serve para exibir as **últimas partes** de um arquivo de texto.

Por padrão, ele mostra as últimas 10 linhas, o que o torna extremamente útil para verificar rapidamente o final de arquivos de log, onde as mensagens mais recentes costumam estar.

## Exemplo Básico

Se você executar o `tail` em um arquivo, ele mostrará as 10 últimas linhas.

```bash
$ tail /var/log/syslog
Dec 10 11:30:01 pc systemd[1]: Started Session 123 of user jules.
Dec 10 11:30:15 pc pulseaudio[1234]: Server connection successful.
Dec 10 11:31:00 pc CRON[5678]: (root) CMD (command -v debian-sa1 > /dev/null...)
... (mais 7 linhas)
```

## Especificando o número de linhas com `-n`

Você pode alterar o número de linhas a serem exibidas com a opção `-n`.

```bash
# Para ver as últimas 5 linhas do arquivo
$ tail -n 5 /var/log/syslog

# Uma sintaxe alternativa e mais curta para o mesmo comando
$ tail -5 /var/log/syslog
```

## Monitorando arquivos em tempo real com `-f`

A funcionalidade mais poderosa do `tail` é a opção `-f` (**f**ollow). Ela permite que você "siga" um arquivo em tempo real.

O `tail` exibirá as últimas linhas e ficará ativo, mostrando qualquer nova linha que for adicionada ao arquivo. Isso é indispensável para monitorar logs de aplicações ou do sistema.

```bash
$ tail -f /var/log/nginx/access.log
192.168.1.10 - - [10/Dec/2023:11:35:00 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0"
192.168.1.12 - - [10/Dec/2023:11:35:05 +0000] "GET /styles.css HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
# O cursor ficará piscando aqui, esperando por novas linhas...
```
Para parar de seguir o arquivo e voltar ao terminal, pressione `Ctrl+C`.
