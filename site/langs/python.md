# Python no Linux

Python é uma linguagem de programação interpretada de alto nível, onipresente no ecossistema Linux. É a escolha padrão para scripts de automação, ciência de dados, backend web e ferramentas de sistema (como o `dnf` e `yum`).

## Verificando Instalação

A maioria das distros já traz o Python pré-instalado.

```bash
python3 --version
# Python 3.10.12
```

Se precisar instalar:

```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv
```

## Gerenciamento de Pacotes (Pip)

O `pip` é o gerenciador de pacotes padrão.

### Instalar um pacote

```bash
pip3 install requests
```

### Gerar lista de dependências

É boa prática salvar as versões dos pacotes usados:

```bash
pip3 freeze > requirements.txt
```

### Instalar a partir de lista

```bash
pip3 install -r requirements.txt
```

## Ambientes Virtuais (Venv)

Sempre use ambientes virtuais para isolar dependências de projetos e evitar poluir o sistema global.

1.  **Criar**:
    ```bash
    python3 -m venv venv
    ```

2.  **Ativar**:
    ```bash
    source venv/bin/activate
    ```
    (O terminal mudará para indicar `(venv)`).

3.  **Desativar**:
    ```bash
    deactivate
    ```

## Truques Úteis

### Servidor Web Instantâneo

Precisa compartilhar arquivos da pasta atual rapidamente?

```bash
python3 -m http.server 8000
```
Acesse `http://localhost:8000`.

### Pretty Print JSON

Formatar JSON de APIs direto no terminal:

```bash
cat dados.json | python3 -m json.tool
```

### Debugger

Para debugar um script linha a linha:

```bash
python3 -m pdb script.py
```
