# nohup

Executa um comando imune a hangup (sinal HUP), permitindo que ele continue rodando mesmo após você sair do terminal. A saída é normalmente redirecionada para `nohup.out`.

```
╭─quack @ termux in ~
╰─❯ nohup python3 script_longo.py &
[1] 12350
nohup: ignorando entrada e acrescentando saída a 'nohup.out'
```
