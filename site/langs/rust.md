# Rust no Linux

Rust é uma linguagem de sistemas focada em segurança e performance.

## Instalação (Rustup)

A maneira recomendada é usar o rustup:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Isso instala `rustc`, `cargo` e `rustup`.

## Atualizar

```bash
rustup update
```

## Compilar um arquivo

```bash
rustc main.rs
```

## Usando Cargo

Criar projeto:
```bash
cargo new meu_projeto
```

cargo run
```

## Ferramentas de Qualidade

Rust tem ferramentas de formatação e análise estática integradas.

### Formatar código
```bash
cargo fmt
```

### Linter (Clippy)
Sugere melhorias idiomáticas e de performance:
```bash
cargo clippy
```

## Compilando para Produção

Por padrão, `cargo build` e `cargo run` usam modo debug (mais lento). Para release:

```bash
cargo build --release
```
O binário otimizado estará em `target/release/`.

## Gerenciamento de Dependências

Para adicionar bibliotecas (crates), edite o arquivo `Cargo.toml`.

```toml
[dependencies]
serde = "1.0"
tokio = { version = "1", features = ["full"] }
```
Depois rode `cargo build` para baixar e compilar.

