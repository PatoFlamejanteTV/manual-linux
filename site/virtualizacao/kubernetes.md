# Kubernetes (K8s)

Kubernetes é um sistema de orquestração de containers.

## Componentes Principais

- **Pod**: A menor unidade, um ou mais containers.
- **Node**: Máquina (física ou virtual) onde o k8s roda.
- **Cluster**: Conjunto de nodes.

## Kubectl

Ferramenta de linha de comando para interagir com o cluster.

Verificar nodes:
```bash
kubectl get nodes
```

Implantar app:
```bash
kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
```
