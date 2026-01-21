# Monitores (Displays)

Monitores são os dispositivos de saída visual. O Linux interage com monitores através dos drivers de GPU (como DRM/KMS).

## Configuração e Resolução

O comando `xrandr` (para X11) é a ferramenta clássica para listar monitores conectados e suas capacidades.

```bash
xrandr --listmonitors
```

Para ver todas as resoluções e taxas de atualização suportadas:

```bash
xrandr -q
```

Em ambientes Wayland, ferramentas específicas do compositor (como `wlr-randr` ou configurações do GNOME/KDE) são utilizadas.

## Informações de Hardware (EDID)

O monitor envia dados de identificação (EDID) para o computador. É possível ler esses dados brutos em `/sys/class/drm/*/edid` ou decodificá-los com ferramentas como `edid-decode`.

Isso informa ao sistema o tamanho físico da tela, espaço de cor suportado e timings preferidos.
