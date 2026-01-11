# wget

O **wget** é uma ferramenta de linha de comando para baixar arquivos da web. Ele suporta protocolos HTTP, HTTPS e FTP.

## Uso Básico

Baixar um arquivo:

```bash
wget http://exemplo.com/arquivo.iso
```

Salvar com um nome diferente:

```bash
wget -O novo_nome.iso http://exemplo.com/arquivo.iso
```

## Resumo de downloads

Continuar um download interrompido:

```bash
wget -c http://exemplo.com/arquivo_grande.iso
```

## Baixar em segundo plano

Use a opção `-b` para baixar em background:

```bash
wget -b http://exemplo.com/distro.iso
```
