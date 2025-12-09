# ssh

O comando `ssh` (abreviação de **S**ecure **Sh**ell) é uma das ferramentas mais importantes para quem trabalha com servidores ou precisa acessar outro computador remotamente de forma **segura**.

Ele cria uma conexão criptografada entre a sua máquina (o cliente) e a máquina remota (o servidor), garantindo que os dados trocados, incluindo senhas e comandos, não possam ser facilmente interceptados.

Ao se conectar, você obtém um shell (linha de comando) no servidor, permitindo que você execute comandos como se estivesse sentado na frente dele.

## Exemplo de Conexão

A sintaxe básica para se conectar é `ssh usuario@host`, onde:
*   `usuario`: É o nome de usuário na máquina remota.
*   `host`: Pode ser o endereço IP (ex: `192.168.1.100`) ou o nome do domínio (ex: `servidor.empresa.com`).

```bash
# Conectando ao servidor 192.168.1.100 com o usuário "admin"
$ ssh admin@192.168.1.100
```

### O que acontece depois?

1.  **Verificação da Identidade (Primeira Vez)**: Na primeira vez que você se conecta a um novo servidor, o SSH perguntará se você confia nele, mostrando a "impressão digital" da chave do servidor. Você deve digitar `yes` para continuar.
    ```
    The authenticity of host '192.168.1.100 (192.168.1.100)' can't be established.
    ECDSA key fingerprint is SHA256:AbCdEfGhIjKlMnOpQrStUvWxYz.
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    ```
2.  **Senha**: Em seguida, ele pedirá a senha do usuário `admin` no servidor.
    ```
    Warning: Permanently added '192.168.1.100' (ECDSA) to the list of known hosts.
    admin@192.168.1.100's password:
    ```
3.  **Conexão Estabelecida**: Se a senha estiver correta, você verá a linha de comando do servidor, e a partir daí, todos os comandos que você digitar serão executados na máquina remota.
    ```
    Welcome to Ubuntu 22.04.1 LTS
    admin@servidor:~$ ls /home
    admin  outro_usuario
    admin@servidor:~$
    ```

Para fechar a conexão, basta digitar `exit` ou pressionar `Ctrl+D`.
