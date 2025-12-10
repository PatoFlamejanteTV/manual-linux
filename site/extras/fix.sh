#!/bin/bash

echo "🔍 Detectando submódulos faltantes…"

# Lista de paths reconhecidos pelo Git como submódulos
KNOWN=$(git submodule status | awk '{print $2}')

# Transforma lista em array para facilitar comparação
KNOWN_ARRAY=($KNOWN)

is_known() {
    local candidate="$1"
    for k in "${KNOWN_ARRAY[@]}"; do
        if [[ "$candidate" == "$k" ]]; then
            return 0
        fi
    done
    return 1
}

# Varrer diretórios da raiz (nível 1)
find . -maxdepth 2 -mindepth 1 -type d -name .git | while read -r gitdir; do
    repo_dir=$(dirname "$gitdir")
    repo_dir_clean=${repo_dir#./}

    if is_known "$repo_dir_clean"; then
        echo "✔ Já registrado: $repo_dir_clean"
        continue
    fi

    echo "⚠ Faltando no .gitmodules: $repo_dir_clean"

    remote_url=$(git -C "$repo_dir" remote get-url origin 2>/dev/null)

    if [[ -z "$remote_url" ]]; then
        echo "❌ Sem remote origin → ignorando: $repo_dir_clean"
        continue
    fi

    echo "→ Registrando submódulo: $repo_dir_clean"
    echo "→ URL: $remote_url"

    # Registrar como submódulo mantendo tudo intacto
    git submodule add --force "$remote_url" "$repo_dir_clean"
done

echo "🔄 Sincronizando…"
git submodule sync
git submodule update --init --recursive

echo "🎉 Finalizado: todos os submódulos faltantes foram corrigidos!"

