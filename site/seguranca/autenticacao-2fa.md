# Autenticação de Dois Fatores (2FA)

Adicionar uma camada extra de segurança ao login (SSH ou local) usando Google Authenticator ou tokens TOTP.

## Instalação

No Debian/Ubuntu:

```bash
sudo apt install libpam-google-authenticator
```

## Configuração por Usuário

Execute no terminal:

```bash
google-authenticator
```

Siga as instruções para gerar o QR code e configurar o app.

## Configuração do PAM

Edite `/etc/pam.d/sshd` (para SSH) e adicione:

```bash
auth required pam_google_authenticator.so
```

## Configuração do SSH

Edite `/etc/ssh/sshd_config`:

```bash
ChallengeResponseAuthentication yes
KbdInteractiveAuthentication yes
```

Reinicie o SSH. Agora será solicitado o código do token após a senha ou chave.
