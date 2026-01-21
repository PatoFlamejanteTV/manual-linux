# Detecção de Intrusão (IDS)

Sistemas de Detecção de Intrusão (IDS) monitoram o tráfego de rede ou a integridade de arquivos para identificar atividades suspeitas.

## Network IDS (NIDS)

Exemplos: **Snort**, **Suricata**.
Eles analisam pacotes em tempo real comparando com assinaturas de ataques conhecidos.

## Host IDS (HIDS)

Exemplos: **AIDE**, **Tripwire**, **OSSEC**.
Monitoram alterações nos arquivos do sistema. Se `/bin/ls` mudar de tamanho ou hash, o HIDS alerta.

### Exemplo com AIDE

1. **Inicializar banco de dados**:

```bash
sudo aideinit
```

1. **Verificar integridade**:

```bash
sudo aide --check
```

Manter o banco de dados de integridade em um local seguro (offline ou somente leitura) é crucial.
