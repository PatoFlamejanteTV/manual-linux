# Apache

O **Apache HTTP Server**, ou só "Apache" pros íntimos, é um dos servidores web
mais antigos e confiáveis que existem. Ele é aquele tiozão que manja de tudo e
tá aí firme e forte há décadas.

Se você quer hospedar um site, ele é uma escolha clássica e muito robusta.

## Instalação

No Debian, Ubuntu e derivados, é molezinha:

```bash
sudo apt update
sudo apt install apache2
```

Se tiver usando Fedora ou CentOS, o nome muda um pouco (é `httpd`):

```bash
sudo dnf install httpd
```

## Configuração

A mágica acontece na pasta `/etc/apache2/` (ou `/etc/httpd/`).

- **`/etc/apache2/apache2.conf`**: O arquivo principal de configuração.
- **`/etc/apache2/sites-available/`**: Onde você cria os arquivos de config
  dos seus sites (vhosts).
- **`/var/www/html/`**: Onde os arquivos do site ficam por padrão.

Pra ver se tá rodando, é só abrir o navegador e digitar `localhost` ou o IP
da máquina. Se aparecer a página "It works!", sucesso!
