# GPG (GNU Privacy Guard)

O GPG é uma implementação livre do padrão OpenPGP, utilizado para criptografar
e assinar dados e comunicações. Ele é fundamental para garantir a privacidade e
a autenticidade de arquivos no ecossistema Linux.

## Para que serve?

* **Criptografia**: Codificar arquivos para que apenas o destinatário com a
  chave correta possa lê-los.
* **Assinatura Digital**: Garantir que um arquivo (como uma ISO de uma
  distribuição Linux) não foi alterado e realmente veio do autor original.

## Chaves Públicas e Privadas

O GPG funciona com um par de chaves:

* **Chave Pública**: Pode ser compartilhada com qualquer pessoa. Usada para
  criptografar mensagens para você ou verificar suas assinaturas.
* **Chave Privada**: Deve ser mantida em segredo absoluto. Usada para
  descriptografar mensagens enviadas para você ou assinar arquivos.

## Exemplo de Uso: Verificando um Arquivo

Muitos projetos Linux fornecem um arquivo de assinatura (`.asc` ou `.sig`) junto
com o download.

1. Importe a chave pública do desenvolvedor (geralmente disponível no site
   deles).

   ```bash
   $ gpg --import chave_do_desenvolvedor.asc
   gpg: key 12345678: public key "Developer <dev@example.com>" imported
   ```

2. Verifique a assinatura do arquivo baixado.

   ```bash
   $ gpg --verify arquivo.iso.sig arquivo.iso
   gpg: Good signature from "Developer <dev@example.com>"
   ```

Se a saída mostrar "Good signature", significa que o arquivo é autêntico e não
foi corrompido ou modificado.
