# kill

O comando `kill` é usado para "matar" (encerrar) um processo que está rodando no sistema.

Para usá-lo, você precisa saber o **ID do Processo** (também chamado de **PID**). Pense no PID como se fosse o CPF de um programa em execução: um número único que o identifica.

## Como encontrar o PID?

Você pode usar o comando `ps` junto com o `grep` para encontrar o PID de um programa específico. Por exemplo, para achar o PID de um processo chamado `gedit` (um editor de texto), você faria:

```bash
$ ps aux | grep gedit
jules     1234  0.4  1.2 654321 98765 ?        Sl   10:30   0:01 gedit
```
O número logo depois do nome de usuário (neste caso, `1234`) é o PID.

## Exemplo de uso

Depois de encontrar o PID, você pode usar o `kill` para encerrá-lo.

```bash
$ kill 1234
```

Isso envia um sinal de terminação padrão (`SIGTERM`), que pede educadamente para o processo fechar.

### Forçando a parada com `-9`

Às vezes, um processo pode travar e não responder ao `kill` normal. Nesses casos, você pode usar a força bruta com o sinal `SIGKILL`, representado pelo número `-9`.

```bash
$ kill -9 1234
```

Isso força o sistema a encerrar o processo imediatamente, sem dar a ele a chance de salvar ou limpar o que estava fazendo. É o último recurso!
