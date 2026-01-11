# systemctl

O **systemctl** é o comando central para controlar o sistema systemd e gerenciador de serviços.

## Iniciar um serviço

```bash
sudo systemctl start nginx
```

## Habilitar no boot

```bash
sudo systemctl enable nginx
```

## Checar status

```bash
systemctl status nginx
```

## Outros Comandos Importantes

### Restart vs Reload
- **Restart**: Para e inicia o processo (derruba conexões).
- **Reload**: Apenas recarrega arquivos de configuração (não derruba conexões).

```bash
sudo systemctl reload nginx
```

### Listar serviços com falha
Útil para diagnóstico rápido.

```bash
systemctl --failed
```

### Desabilitar completamente (Mask)
Impede que o serviço seja iniciado, mesmo manualmente.

```bash
sudo systemctl mask servico
```

### Editar Service Unit
A maneira correta de alterar configurações de um serviço sem sobrescrever o arquivo do pacote.

```bash
sudo systemctl edit nginx
```
Isso abre um editor para você adicionar overrides.

