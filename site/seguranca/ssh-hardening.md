# Hardening do SSH (Secure Shell)

O SSH é a principal porta de entrada para administração remota de servidores Linux. Por isso, é um alvo frequente de ataques.

## Boas Práticas

### 1. Desabilitar Login de Root

Edite `/etc/ssh/sshd_config`:

```bash
PermitRootLogin no
```

### 2. Usar Chaves SSH e Desabilitar Senhas

O uso de chaves criptográficas é muito mais seguro que senhas.

```bash
PubkeyAuthentication yes
PasswordAuthentication no
```

### 3. Alterar a Porta Padrão

Mudar a porta 22 para uma porta alta (ex: 2222) reduz o ruído de scanners automáticos.

```bash
Port 2222
```

### 4. Limitar Usuários Permitidos

```bash
AllowUsers usuario1 usuario2
```

### 5. Reiniciar o Serviço

Sempre reinicie o serviço após alterações:

```bash
sudo systemctl restart sshd
```
