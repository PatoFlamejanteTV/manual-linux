# MongoDB

MongoDB é um banco de dados NoSQL orientado a documentos.

## Instalação (Ubuntu)

```bash
sudo apt install -y mongodb
```

## Iniciar serviço

```bash
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

## Shell

Acessar o shell do Mongo:

```bash
mongo
```

## Comandos básicos

```javascript
use meu_banco
db.minha_colecao.insert({ nome: "Pato", tipo: "Ave" })
db.minha_colecao.find()
```
