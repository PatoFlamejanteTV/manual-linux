# Usuários e Grupos

O Linux é, por natureza, um sistema **multiusuário**. Isso significa que múltiplos usuários podem ter contas no mesmo sistema, cada um com seus próprios diretórios, arquivos e permissões.

## Tipos de Usuário

Existem três tipos principais de usuários no Linux:

* **`root` (Superusuário):** O usuário `root` tem acesso total e irrestrito ao sistema. Ele pode ler, escrever e executar qualquer arquivo, bem como modificar qualquer configuração do sistema. É recomendado usar o `root` apenas para tarefas administrativas.
* **Usuário Padrão:** Um usuário padrão tem privilégios limitados. Ele pode executar programas e criar arquivos em seu diretório pessoal, mas não pode modificar arquivos de sistema ou de outros usuários, a menos que tenha permissão explícita.
* **Usuário de Serviço:** Muitos serviços e daemons do sistema rodam com suas próprias contas de usuário. Essas contas de serviço têm privilégios ainda mais limitados e são usadas por razões de segurança.

## Gerenciando Usuários

Aqui estão os comandos básicos para gerenciar usuários no Linux:

```bash
# Adicionar um novo usuário
$ sudo useradd -m nome_de_usuario

# Definir a senha para o novo usuário
$ sudo passwd nome_de_usuario

# Modificar um usuário existente (por exemplo, adicionar a um grupo)
$ sudo usermod -aG sudo nome_de_usuario

# Deletar um usuário
$ sudo userdel -r nome_de_usuario
```

## Grupos

Cada usuário no Linux pertence a um ou mais **grupos**. Os grupos são usados para organizar usuários e gerenciar permissões de forma mais eficiente.

### Gerenciando Grupos

Aqui estão os comandos básicos para gerenciar grupos:

```bash
# Adicionar um novo grupo
$ sudo groupadd nome_do_grupo

# Adicionar um usuário a um grupo
$ sudo usermod -aG nome_do_grupo nome_de_usuario

# Remover um usuário de um grupo
$ sudo gpasswd -d nome_de_usuario nome_do_grupo

# Deletar um grupo (não pode ser o grupo primário de nenhum usuário)
$ sudo groupdel nome_do_grupo
```

## Verificando Informações

Você pode ver informações sobre usuários e grupos nos seguintes arquivos:

* `/etc/passwd`: Lista de usuários do sistema.
* `/etc/shadow`: Contém as senhas criptografadas dos usuários.
* `/etc/group`: Lista de grupos do sistema.
