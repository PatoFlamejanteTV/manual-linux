# Go

Go (ou Golang) é uma linguagem de programação moderna desenvolvida pelo Google.
Ela é conhecida por sua simplicidade e eficiência, sendo muito utilizada no
desenvolvimento de ferramentas de infraestrutura, como Docker e Kubernetes.

## Exemplo de Código

Um arquivo `main.go`:

```go
package main

import "fmt"

func main() {
    fmt.Println("Olá, Go no Linux!")
}
```

## Executando

Você pode executar diretamente sem compilar um binário separado:

```bash
$ go run main.go
Olá, Go no Linux!
```

Ou compilar para um executável:

```bash
$ go build main.go
$ ./main
Olá, Go no Linux!
```
