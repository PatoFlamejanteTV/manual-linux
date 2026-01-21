# Detecção de Rootkits

Rootkits são softwares maliciosos projetados para esconder a existência de processos ou atividades no sistema. Ferramentas como `chkrootkit` e `rkhunter` ajudam a identificá-los.

## chkrootkit

Ferramenta simples que verifica binários do sistema em busca de assinaturas conhecidas.

Uso:

```bash
sudo chkrootkit
```

## rkhunter (Rootkit Hunter)

Mais avançado, verifica hashes de arquivos, permissões e arquivos ocultos.

1. **Atualizar base de dados**:

```bash
sudo rkhunter --update
```

1. **Fazer verificação**:

```bash
sudo rkhunter --check
```

Lembre-se: Se um sistema foi comprometido por um rootkit de kernel, a única solução 100% segura é reinstalar o sistema.
