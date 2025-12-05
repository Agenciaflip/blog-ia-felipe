---
title: "Flask Python: Tutorial Completo 2025"
description: "Flask Python: criar API REST, deploy, autenticação JWT e integração banco de dados. Tutorial do zero ao deploy em produção. Código completo incluído."
publishDate: 2025-01-22
author: "Felipe Zanoni"
category: "Desenvolvimento"
tags: ["flask python", "api rest", "python web", "backend python"]
draft: false
---

> **📚 Série:** Desenvolvimento Python
> → [API OpenAI](/blog/api-openai-python-2025/) | [Docker Tutorial](/blog/docker-tutorial-completo-2025/) | [Deploy Aplicação](/blog/deploy-aplicacao-python-2025/)

## O que é Flask Python?

Flask é um micro-framework Python para criar aplicações web e APIs REST. Criado por Armin Ronacher em 2010, Flask é usado por empresas como Netflix, Uber e Airbnb. É ideal para criar [APIs WhatsApp](/blog/api-whatsapp-guia-completo/), [chatbots](/blog/chatbot-whatsapp-guia-completo-2025/) e backends de aplicações modernas. Flask tem 65.000+ estrelas no GitHub e 2M+ downloads/mês.

**Site oficial:** [flask.palletsprojects.com](https://flask.palletsprojects.com/)
**GitHub:** [pallets/flask](https://github.com/pallets/flask)

---

## Por que Flask vs Django/FastAPI

### Comparação frameworks Python:

| Recurso | Flask | Django | FastAPI |
|---------|-------|--------|---------|
| **Tipo** | Micro-framework | Full-stack | Async framework |
| **Curva aprendizado** | ✅ 1 dia | ❌ 1 semana | ⚠️ 2-3 dias |
| **Performance** | Boa | Boa | ✅ Excelente |
| **Admin painel** | ❌ Não | ✅ Sim | ❌ Não |
| **ORM nativo** | ❌ Não (usar SQLAlchemy) | ✅ Sim | ❌ Não |
| **Async/await** | ❌ Limitado | ❌ Limitado | ✅ Nativo |
| **Documentação auto** | ❌ Não | ❌ Não | ✅ Swagger |
| **Ideal para** | APIs, microservices | Sites completos | APIs high-performance |

**Veredito:** Flask vence em **simplicidade + flexibilidade**.

**Quando usar Flask:**
- ✅ APIs REST simples/médias
- ✅ Microservices
- ✅ Webhooks (ex: [Evolution API](/blog/evolution-api-tutorial-completo/))
- ✅ MVPs rápidos

**Quando NÃO usar Flask:**
- ❌ Sites complexos com admin (usar Django)
- ❌ APIs com tráfego massivo (usar FastAPI)

---

## Instalação e setup

### Passo 1: Criar ambiente virtual

```bash
# Criar projeto
mkdir meu-projeto-flask
cd meu-projeto-flask

# Criar virtualenv
python3 -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate
```

### Passo 2: Instalar Flask

```bash
pip install flask

# Verificar instalação
flask --version
# Flask 3.0.0 (Python 3.11)
```

### Passo 3: Hello World

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Hello World!'}

if __name__ == '__main__':
    app.run(debug=True)
```

**Executar:**
```bash
python app.py
# Running on http://127.0.0.1:5000
```

**Testar:**
```bash
curl http://localhost:5000
# {"message":"Hello World!"}
```

---

## Criar API REST completa

### Estrutura do projeto:

```
meu-projeto-flask/
├── app.py              # Aplicação principal
├── models.py           # Modelos do banco
├── routes/
│   ├── __init__.py
│   ├── users.py        # Rotas /users
│   └── products.py     # Rotas /products
├── config.py           # Configurações
├── requirements.txt    # Dependências
└── .env                # Variáveis ambiente
```

### app.py (principal):

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Permitir CORS

# Configurações
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Banco de dados
db = SQLAlchemy(app)

# Importar rotas
from routes import users, products

# Registrar blueprints
app.register_blueprint(users.bp, url_prefix='/api/users')
app.register_blueprint(products.bp, url_prefix='/api/products')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Criar tabelas
    app.run(debug=True)
```

### models.py (modelos):

```python
from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'created_at': self.created_at.isoformat()
        }
```

### routes/users.py (CRUD usuários):

```python
from flask import Blueprint, request, jsonify
from app import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('users', __name__)

# CREATE
@bp.route('/', methods=['POST'])
def create_user():
    data = request.json

    # Validação
    if not data.get('email') or not data.get('password'):
        return {'error': 'Email e password obrigatórios'}, 400

    # Verificar se já existe
    if User.query.filter_by(email=data['email']).first():
        return {'error': 'Email já cadastrado'}, 409

    # Criar usuário
    user = User(
        name=data.get('name'),
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )

    db.session.add(user)
    db.session.commit()

    return user.to_dict(), 201

# READ (listar todos)
@bp.route('/', methods=['GET'])
def list_users():
    users = User.query.all()
    return {'users': [u.to_dict() for u in users]}

# READ (por ID)
@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user.to_dict()

# UPDATE
@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json

    if data.get('name'):
        user.name = data['name']
    if data.get('email'):
        user.email = data['email']

    db.session.commit()
    return user.to_dict()

# DELETE
@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204
```

---

## Autenticação JWT

### Instalar dependências:

```bash
pip install flask-jwt-extended
```

### Configurar JWT:

```python
# app.py
from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET', 'super-secret-key')
jwt = JWTManager(app)
```

### Login endpoint:

```python
# routes/auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from models import User

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.json

    # Buscar usuário
    user = User.query.filter_by(email=data.get('email')).first()

    # Verificar senha
    if not user or not check_password_hash(user.password_hash, data.get('password')):
        return {'error': 'Email ou senha inválidos'}, 401

    # Gerar token
    access_token = create_access_token(identity=user.id)

    return {
        'access_token': access_token,
        'user': user.to_dict()
    }

# Rota protegida
@bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return user.to_dict()
```

**Uso:**

```bash
# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"senha123"}'

# Resposta:
# {"access_token":"eyJ0eXAi..."}

# Usar token
curl http://localhost:5000/api/auth/me \
  -H "Authorization: Bearer eyJ0eXAi..."
```

---

## Integração com banco de dados

### PostgreSQL (produção):

```bash
pip install psycopg2-binary
```

```python
# .env
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
```

### SQLite (desenvolvimento):

```python
# app.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
```

### Migrations (Alembic):

```bash
pip install flask-migrate

# Inicializar
flask db init

# Criar migration
flask db migrate -m "Initial migration"

# Aplicar
flask db upgrade
```

---

## Integrar com OpenAI GPT-4

**Criar [chatbot](/blog/chatbot-whatsapp-guia-completo-2025/) com Flask:**

```python
# routes/chatbot.py
from flask import Blueprint, request
from openai import OpenAI

bp = Blueprint('chatbot', __name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensagem = data.get('message')

    # Chamar GPT-4
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": mensagem}
        ]
    )

    resposta = response.choices[0].message.content

    return {'response': resposta}
```

**Integrar com [WhatsApp via Evolution API](/blog/evolution-api-tutorial-completo/):**

```python
@bp.route('/webhook-whatsapp', methods=['POST'])
def webhook_whatsapp():
    data = request.json

    numero = data["key"]["remoteJid"].split("@")[0]
    mensagem = data["message"]["conversation"]

    # Chamar GPT-4
    resposta_ia = chat_gpt4(mensagem)

    # Enviar via Evolution API
    requests.post(
        "https://evolution.com/message/sendText/instance",
        json={"number": numero, "text": resposta_ia},
        headers={"apikey": "KEY"}
    )

    return '', 200
```

**Tutorial completo:** [API OpenAI Python](/blog/api-openai-python-2025/)

---

## Deploy em produção

### Opção 1: Docker ([Tutorial completo](/blog/docker-tutorial-completo-2025/))

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

```bash
# Build
docker build -t meu-flask-app .

# Run
docker run -p 8000:8000 meu-flask-app
```

### Opção 2: Render.com (grátis)

1. Criar `render.yaml`:

```yaml
services:
  - type: web
    name: meu-flask-app
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
```

2. Conectar GitHub
3. Deploy automático

**Docs:** [Render Python Apps](https://render.com/docs/deploy-flask)

### Opção 3: Heroku

```bash
# Criar Procfile
web: gunicorn app:app

# Deploy
git push heroku main
```

---

## Boas práticas

### 1. Usar Blueprints

**Errado:**
```python
# Tudo em app.py (300+ linhas)
@app.route('/users')
def users():
    ...
```

**Correto:**
```python
# routes/users.py
bp = Blueprint('users', __name__)

@bp.route('/')
def list_users():
    ...
```

### 2. Validação de dados

```bash
pip install marshmallow
```

```python
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))

@bp.route('/', methods=['POST'])
def create_user():
    schema = UserSchema()
    errors = schema.validate(request.json)

    if errors:
        return {'errors': errors}, 400

    # Criar usuário...
```

### 3. Error handling

```python
@app.errorhandler(404)
def not_found(error):
    return {'error': 'Recurso não encontrado'}, 404

@app.errorhandler(500)
def internal_error(error):
    return {'error': 'Erro interno do servidor'}, 500
```

### 4. CORS configurado

```python
from flask_cors import CORS

CORS(app, origins=['https://meu-frontend.com'])
```

---

## Testing (Pytest)

```bash
pip install pytest flask-testing
```

```python
# test_app.py
import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_user(client):
    response = client.post('/api/users/', json={
        'name': 'João',
        'email': 'joao@example.com',
        'password': 'senha123'
    })

    assert response.status_code == 201
    assert response.json['email'] == 'joao@example.com'
```

**Executar:**
```bash
pytest
```

---

## Caso Real: Startup criou MVP em 2 semanas

**Empresa:** SaaS de agendamentos (3 devs)

**Solução:**
- Flask + PostgreSQL
- Autenticação JWT
- Deploy Render (grátis)
- Frontend React consumindo API

**Tempo desenvolvimento:** 80h (2 semanas)

**Stack:**
- Backend: Flask + SQLAlchemy
- Banco: PostgreSQL (Render)
- Deploy: Render.com (grátis)

**Resultado:**
- ✅ MVP funcional em 14 dias
- ✅ 500 usuários no primeiro mês
- ✅ 99.9% uptime (Render)
- ✅ Custo: R$ 0 (tier grátis)

---

## Documentação oficial

- [Flask Docs](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [Marshmallow](https://marshmallow.readthedocs.io/)

---

## Próximos passos

1. **[Criar API OpenAI](/blog/api-openai-python-2025/)** - Integrar IA
2. **[Docker Tutorial](/blog/docker-tutorial-completo-2025/)** - Containerizar app
3. **[Deploy aplicação](/blog/deploy-aplicacao-python-2025/)** - Produção
4. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Usar Flask

---

**Sobre o autor:** Felipe Zanoni é desenvolvedor Python especializado em Flask, com 400+ APIs criadas em produção.
