# API de Gerenciamento de Tarefas — Curso de Extensão DevOps (PUCPR)

Projeto desenvolvido para o Curso de Extensão em DevOps, promovido pela PUCPR em parceria com a Sescoop. O objetivo é colocar em prática, de ponta a ponta, um fluxo real de desenvolvimento: da escrita da API até a implantação em um cluster Kubernetes, passando por conteinerização e uma pipeline automatizada de CI/CD.

## 📋 Sobre o Projeto

A aplicação é uma API REST construída com **FastAPI** para gerenciar tarefas (criação, consulta, atualização e remoção). O projeto vai além da API em si e reproduz um ambiente próximo do que se encontra em produção, incluindo:

- Serviço de notificações rodando em container separado;
- Gateway com Nginx na frente da aplicação;
- Orquestração local com Docker Compose;
- Pipeline de CI/CD automatizada no GitHub Actions;
- Manifests de implantação para Kubernetes.

## 🚀 Stack

- **Linguagem:** Python 3.12
- **Framework:** FastAPI + Uvicorn
- **Containers:** Docker / Docker Compose
- **Orquestração:** Kubernetes
- **Gateway:** Nginx
- **CI/CD:** GitHub Actions
- **Qualidade e testes:** Pytest, Bandit, Pylint

## 📁 Estrutura

```
.
├── .github/
│   └── workflows/
│       └── ci_cd.yaml
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── notificacao.py
├── tests/
├── Dockerfile
├── Dockerfile.nginx
├── docker-compose.yaml
├── deployment.yaml
├── service-devops.yaml
├── nginx.conf
├── requirements.txt
└── README.md
```

## ⚙️ Funcionalidades

- Criar, listar, consultar, atualizar e excluir tarefas
- Health check da aplicação
- Exposição de métricas

## 📌 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Mensagem inicial |
| GET | `/tarefas` | Lista todas as tarefas |
| GET | `/tarefas/{id}` | Busca uma tarefa pelo ID |
| POST | `/tarefas/criar` | Cria uma nova tarefa |
| PUT | `/tarefas/atualizar/{id}` | Atualiza uma tarefa existente |
| DELETE | `/tarefas/deletar/{id}` | Remove uma tarefa |
| GET | `/health` | Health check |
| GET | `/metricas` | Métricas da aplicação |

## 🐳 Rodando com Docker

Construir as imagens:

```bash
docker compose build
```

Subir os containers:

```bash
docker compose up
```

Ou em background:

```bash
docker compose up -d
```

## ☸️ Implantação no Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service-devops.yaml
```

Verificar o estado do cluster:

```bash
kubectl get pods
kubectl get services
```

## 🔄 Pipeline de CI/CD

A pipeline roda automaticamente em Pull Requests para a branch `main` e também pode ser disparada manualmente. Ela é dividida em três grandes etapas:

**Integração Contínua**
- Instalação de dependências
- Testes unitários com Pytest
- Cobertura mínima de código de 65%
- Análise estática de segurança com Bandit
- Análise de qualidade de código com Pylint
- Checagem de dependências com FOSSA

**Entrega Contínua**
- Build da imagem Docker
- Publicação da imagem no Docker Hub

**Implantação**
- Aplicação automática do deployment no Kubernetes

## 🧪 Testes

Instalar dependências:

```bash
pip install -r requirements.txt
```

Rodar os testes:

```bash
pytest
```

Rodar com cobertura:

```bash
pytest --cov
```

## 📊 Health Check

```
GET /health
```

Resposta esperada:

```json
{
  "status": "ok, retorno esperado"
}
```

## 📦 Containers da aplicação

- API principal
- Serviço de notificações
- Nginx (gateway)

## 🔒 Qualidade de código

Ferramentas usadas para manter o código testado e seguro: Pytest, Coverage, Bandit e Pylint.

## 👨‍💻 Autor

Projeto desenvolvido para o Curso de Extensão em DevOps — PUCPR / Sescoop 

Repositório: https://github.com/felipe1cruz/devops
