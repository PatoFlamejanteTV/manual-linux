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

Rodar:
```bash
cargo run
```
