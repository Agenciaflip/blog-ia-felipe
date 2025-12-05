---
title: "Docker Tutorial: Guia Completo 2025"
description: "Docker tutorial do zero: instalação, Dockerfile, Docker Compose, deploy containers em produção. Aprenda containerização em 1 hora. Código completo incluído."
publishDate: 2025-01-23
author: "Felipe Zanoni"
category: "DevOps"
tags: ["docker", "containers", "devops", "docker compose"]
draft: false
---

> **📚 Série:** DevOps & Deploy
> → [Flask Python](/blog/flask-python-tutorial-2025/) | [Deploy Aplicação](/blog/deploy-aplicacao-python-2025/) | [VPS Servidor](/blog/servidor-vps-2025/)

## O que é Docker?

Docker é uma plataforma open-source para criar, distribuir e executar aplicações em containers. Containers empacotam código + dependências, garantindo que aplicações rodem identicamente em qualquer ambiente (dev, staging, produção). Docker é usado por 85% das empresas Fortune 500, incluindo Netflix, Spotify e Uber. Criado em 2013, Docker revolucionou deploy de aplicações.

**Site oficial:** [docker.com](https://www.docker.com/)
**GitHub:** [docker/docker-ce](https://github.com/docker/docker-ce)

---

## Por que usar Docker em 2025

### Problemas que Docker resolve:

**Sem Docker:**
- ❌ "Funciona na minha máquina" (diferenças de ambiente)
- ❌ Conflitos de dependências (Python 3.10 vs 3.11)
- ❌ Setup complexo (instalar 10+ dependências manualmente)
- ❌ Deploy manual demorado (30-60 min)

**Com Docker:**
- ✅ Ambiente idêntico (dev = produção)
- ✅ Isolamento total (sem conflitos)
- ✅ Setup em 1 comando (`docker run`)
- ✅ Deploy em segundos

### Docker vs Máquinas Virtuais:

| Característica | Docker | VM (VirtualBox) |
|----------------|--------|-----------------|
| **Tamanho** | 50-200 MB | 2-10 GB |
| **Startup** | <1 segundo | 30-60 segundos |
| **Performance** | ✅ Nativa | ⚠️ Overhead 10-15% |
| **Isolamento** | ✅ Processo | ✅ Sistema completo |
| **Uso de recursos** | ✅ Baixo | ❌ Alto |
| **Portabilidade** | ✅ Total | ⚠️ Limitada |

---

## Instalação Docker

### Linux (Ubuntu/Debian):

```bash
# Remover versões antigas
sudo apt remove docker docker-engine docker.io containerd runc

# Atualizar
sudo apt update
sudo apt install ca-certificates curl gnupg

# Adicionar chave GPG
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Adicionar repositório
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER
newgrp docker

# Verificar
docker --version
# Docker version 24.0.7
```

### macOS:

1. Baixar: [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
2. Instalar (drag & drop)
3. Abrir Docker Desktop
4. Verificar:
```bash
docker --version
```

### Windows:

1. Habilitar WSL 2: [Docs Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install)
2. Baixar: [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)
3. Instalar
4. Verificar no PowerShell:
```powershell
docker --version
```

---

## Conceitos fundamentais

### 1. Image (Imagem)

Template imutável com código + dependências.

**Exemplo:** `python:3.11-slim` (imagem oficial Python)

### 2. Container

Instância executável de uma imagem.

**Analogia:** Imagem = receita de bolo | Container = bolo assado

### 3. Dockerfile

Arquivo texto com instruções para criar imagem.

```dockerfile
FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### 4. Docker Compose

Ferramenta para rodar múltiplos containers (ex: app + banco).

---

## Primeiro container: Hello World

```bash
# Baixar e executar imagem hello-world
docker run hello-world

# Saída:
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
```

**O que aconteceu:**
1. Docker procurou imagem `hello-world` localmente
2. Não encontrou, baixou do Docker Hub
3. Criou container a partir da imagem
4. Executou comando padrão
5. Mostrou mensagem
6. Container parou

---

## Criar Dockerfile (aplicação Python)

### Projeto exemplo: [API Flask](/blog/flask-python-tutorial-2025/)

**Estrutura:**
```
meu-projeto/
├── app.py
├── requirements.txt
└── Dockerfile
```

### app.py:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Hello from Docker!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
```

### requirements.txt:

```
flask==3.0.0
```

### Dockerfile:

```dockerfile
# Imagem base (Python 3.11 slim = menor tamanho)
FROM python:3.11-slim

# Metadados
LABEL maintainer="seu@email.com"

# Diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro (cache layer)
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Expor porta
EXPOSE 8000

# Comando padrão
CMD ["python", "app.py"]
```

### Build e run:

```bash
# Build imagem
docker build -t minha-api:v1 .

# Listar imagens
docker images
# REPOSITORY   TAG   IMAGE ID      SIZE
# minha-api    v1    abc123def456  150MB

# Executar container
docker run -d -p 8000:8000 --name minha-api-container minha-api:v1

# Testar
curl http://localhost:8000
# {"message":"Hello from Docker!"}
```

**Flags explicadas:**
- `-d`: detached (background)
- `-p 8000:8000`: mapear porta host:container
- `--name`: nome do container

---

## Comandos essenciais

### Containers:

```bash
# Listar containers rodando
docker ps

# Listar todos (incluindo parados)
docker ps -a

# Parar container
docker stop minha-api-container

# Iniciar container parado
docker start minha-api-container

# Remover container
docker rm minha-api-container

# Logs
docker logs minha-api-container

# Logs em tempo real
docker logs -f minha-api-container

# Executar comando em container rodando
docker exec -it minha-api-container bash

# Inspecionar container
docker inspect minha-api-container
```

### Images:

```bash
# Listar imagens
docker images

# Baixar imagem
docker pull python:3.11

# Remover imagem
docker rmi minha-api:v1

# Fazer push (Docker Hub)
docker push usuario/minha-api:v1
```

---

## Docker Compose (múltiplos containers)

### Caso de uso: [Flask](/blog/flask-python-tutorial-2025/) + PostgreSQL

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  # Banco de dados
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: senha123
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  # API Flask
  api:
    build: .
    command: python app.py
    environment:
      DATABASE_URL: postgresql://admin:senha123@db:5432/mydb
    ports:
      - "8000:8000"
    depends_on:
      - db
    volumes:
      - .:/app

volumes:
  postgres_data:
```

### Comandos Docker Compose:

```bash
# Subir todos containers
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar todos
docker-compose down

# Rebuild e subir
docker-compose up --build

# Ver containers rodando
docker-compose ps
```

---

## Volumes (persistência de dados)

**Sem volume:** Dados deletados quando container para.

**Com volume:** Dados persistem.

```bash
# Criar volume
docker volume create meu-volume

# Usar volume
docker run -d -v meu-volume:/data alpine

# Listar volumes
docker volume ls

# Inspecionar
docker volume inspect meu-volume
```

**No Dockerfile:**
```dockerfile
VOLUME ["/data"]
```

**No docker-compose.yml:**
```yaml
volumes:
  - ./local-folder:/container-folder
```

---

## Caso Real: Deploy [Evolution API](/blog/evolution-api-tutorial-completo/)

### docker-compose.yml:

```yaml
version: '3.8'

services:
  evolution-api:
    image: atendai/evolution-api:latest
    environment:
      AUTHENTICATION_API_KEY: minha_chave_secreta
      DATABASE_ENABLED: true
      DATABASE_PROVIDER: postgresql
      DATABASE_CONNECTION_URI: postgresql://user:pass@db:5432/evolution
    ports:
      - "8080:8080"
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: evolution
      POSTGRES_PASSWORD: senha123
      POSTGRES_DB: evolution
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Subir:**
```bash
docker-compose up -d

# Acessar: http://localhost:8080
```

---

## Boas práticas Dockerfile

### 1. Use imagens oficiais e slim

❌ **Ruim:**
```dockerfile
FROM ubuntu:latest  # 77 MB
RUN apt install python3
```

✅ **Bom:**
```dockerfile
FROM python:3.11-slim  # 45 MB
```

### 2. Multi-stage builds (reduzir tamanho)

```dockerfile
# Stage 1: Build
FROM python:3.11 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
CMD ["python", "app.py"]
```

**Resultado:** Imagem 60% menor (não inclui ferramentas de build).

### 3. Order layers (cache inteligente)

❌ **Ruim (rebuild tudo sempre):**
```dockerfile
COPY . .
RUN pip install -r requirements.txt
```

✅ **Bom (cache se requirements não muda):**
```dockerfile
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### 4. .dockerignore

```
# .dockerignore
__pycache__/
*.pyc
.git/
.env
node_modules/
venv/
```

---

## Deploy em produção

### Opção 1: [VPS com Docker](/blog/servidor-vps-2025/)

```bash
# SSH no servidor
ssh user@meu-servidor.com

# Clonar repo
git clone https://github.com/user/projeto.git
cd projeto

# Subir com Docker Compose
docker-compose up -d

# Configurar Traefik (reverse proxy)
# Ver tutorial completo: https://doc.traefik.io/traefik/
```

### Opção 2: Render.com

1. Criar `Dockerfile` no projeto
2. Conectar GitHub ao Render
3. Deploy automático a cada push

**Docs:** [Render Docker](https://render.com/docs/docker)

### Opção 3: AWS ECS/Fargate

```bash
# Push imagem para ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789.dkr.ecr.us-east-1.amazonaws.com

docker tag minha-api:v1 123456789.dkr.ecr.us-east-1.amazonaws.com/minha-api:v1
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/minha-api:v1
```

---

## Troubleshooting

### Container não inicia:

```bash
# Ver logs
docker logs container-name

# Ver detalhes
docker inspect container-name
```

### Porta já em uso:

```bash
# Matar processo na porta 8000
lsof -ti:8000 | xargs kill -9

# Ou usar porta diferente
docker run -p 8001:8000 minha-api
```

### Disco cheio (imagens antigas):

```bash
# Limpar containers parados
docker container prune

# Limpar imagens não usadas
docker image prune

# Limpar TUDO (cuidado!)
docker system prune -a
```

---

## Docker Hub (registry público)

### Fazer push:

```bash
# Login
docker login

# Tag com username
docker tag minha-api:v1 meuusername/minha-api:v1

# Push
docker push meuusername/minha-api:v1
```

### Usar imagem pública:

```bash
docker pull meuusername/minha-api:v1
docker run -p 8000:8000 meuusername/minha-api:v1
```

**Imagens populares:**
- `nginx:latest` - Web server
- `postgres:15` - Banco de dados
- `redis:latest` - Cache
- `python:3.11` - Python runtime

---

## Caso Real: Startup reduziu custos 70%

**Empresa:** SaaS B2B (10 microservices)

**Antes do Docker:**
- 10 VPS separados ($50/cada = $500/mês)
- Deploy manual (30 min por service)
- Downtime frequente (inconsistências de ambiente)

**Depois do Docker:**
- 2 VPS com Docker Swarm ($150/mês total)
- Deploy automático (< 1 min)
- Zero downtime (rolling updates)

**Resultados:**
- ✅ Custo: $500 → $150/mês (70% economia)
- ✅ Deploy time: 30 min → 1 min
- ✅ Uptime: 95% → 99.9%
- ✅ Produtividade dev: +40%

---

## Documentação oficial

- [Docker Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

---

## Próximos passos

1. **[Deploy aplicação](/blog/deploy-aplicacao-python-2025/)** - Produção completa
2. **[VPS Servidor](/blog/servidor-vps-2025/)** - Configurar VPS
3. **[Flask Python](/blog/flask-python-tutorial-2025/)** - Criar API
4. **[Evolution API](/blog/evolution-api-tutorial-completo/)** - Deploy com Docker

---

**Sobre o autor:** Felipe Zanoni é especialista em DevOps e Docker, com 300+ deploys em containers para produção.
