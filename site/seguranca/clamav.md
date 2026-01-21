# Antivírus ClamAV

Embora vírus sejam raros no Linux, servidores de arquivos e e-mail precisam verificar arquivos que passarão para clientes Windows. O ClamAV é a solução open-source padrão.

## Instalação

```bash
sudo apt install clamav clamav-daemon
```

## Atualizando Assinaturas

Pare o serviço e use o `freshclam`:

```bash
sudo systemctl stop clamav-freshclam
sudo freshclam
sudo systemctl start clamav-freshclam
```

## Escaneando

Escanear um diretório recursivamente e tocar um sinal sonoro se encontrar algo:

```bash
clamscan -r --bell -i /home
```

- `-r`: Recursivo.
- `-i`: Mostrar apenas arquivos infectados.
