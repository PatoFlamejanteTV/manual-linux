# BIOS e UEFI

O Firmware da placa-mãe é responsável por inicializar o hardware antes de carregar o Sistema Operacional.

## Legacy BIOS vs UEFI

- **BIOS (Legacy):** Método antigo. Usa MBR.
- **UEFI:** Padrão moderno, interface gráfica, suporta Secure Boot e discos GPT maiores que 2TB.

Para verificar se você está rodando em modo UEFI:

```bash
ls /sys/firmware/efi
```

Se o diretório existir, o sistema bootou em modo UEFI.

## Manipulação de Variáveis UEFI

No Linux, é possível ler e (com cuidado) escrever variáveis UEFI e a ordem de boot usando `efibootmgr`.

```bash
sudo efibootmgr
```

Isso listará a ordem de boot atual e as entradas disponíveis (ex: "Linux Boot Manager", "Windows Boot Manager").
