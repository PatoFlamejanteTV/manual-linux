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

## Artifacts e Cache

### Artifacts (Persistir arquivos)
Para passar arquivos de um estágio para outro (ex: binário compilado):

```yaml
build-job:
  script: make build
  artifacts:
    paths:
      - bin/app
    expire_in: 1 week
```

### Cache (Otimizar performance)
Para não baixar dependências toda vez (ex: node_modules):

```yaml
cache:
  paths:
    - node_modules/
```

## Regras de Execução

Rodar apenas na branch main:

```yaml
deploy-job:
  stage: deploy
  script: ./deploy.sh
  only:
    - main
```

