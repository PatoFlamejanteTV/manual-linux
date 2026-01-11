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

## Expondo Aplicações (Services)

Para acessar o pod externamente (via NodePort ou LoadBalancer):

```bash
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
```

## Abordagem Declarativa (Arquivos YAML)

A forma profissional de gerenciar k8s é via arquivos.

Crie `deployment.yaml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

Aplicar:
```bash
kubectl apply -f deployment.yaml
```

## Namespaces

Para organizar o cluster em ambientes virtuais:

```bash
kubectl get namespaces
kubectl create namespace dev
```

## Rodando Localmente

Para testar no seu próprio computador, instale:
- **Minikube**: Cria uma VM com o cluster.
- **Kind**: Roda o cluster dentro de containers Docker.

