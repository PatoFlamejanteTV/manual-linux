# GitLab CI/CD

GitLab CI/CD é uma ferramenta construída no GitLab para integração e entrega contínua.

## Arquivo .gitlab-ci.yml

A configuração reside na raiz do repositório.

Exemplo básico:

```yaml
build-job:
  stage: build
  script:
    - echo "Compilando..."
    - make

test-job:
  stage: test
  script:
    - echo "Testando..."
    - make test
```

## Runners

Os jobs são executados por GitLab Runners, que podem ser instalados em servidores locais.
