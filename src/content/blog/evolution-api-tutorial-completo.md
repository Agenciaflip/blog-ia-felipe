---
title: "Evolution API: Tutorial Completo 2025"
description: "Evolution API: instalação, configuração, webhooks e integração com IA. Open-source, grátis e ilimitado. Tutorial Docker, QR Code e código Python/Node.js."
publishDate: 2025-01-20
author: "Felipe Zanoni"
category: "WhatsApp"
tags: ["evolution api", "whatsapp api", "open source", "docker"]
draft: false
---

> **📚 Série:** Automação WhatsApp com IA
> → [API WhatsApp](/blog/api-whatsapp-guia-completo/) | [Chatbot](/blog/chatbot-whatsapp-guia-completo-2025/) | [Automação](/blog/automacao-whatsapp-2025/)

## O que é Evolution API?

Evolution API é uma solução **open-source** que conecta sistemas ao WhatsApp Business **gratuitamente**. Substitui a [API oficial paga](/blog/api-whatsapp-guia-completo/) do Meta. Permite criar [chatbots](/blog/chatbot-whatsapp-guia-completo-2025/), [automatizar vendas](/blog/crm-vendas-guia-completo-2025/) e [integrar WhatsApp](/blog/automacao-whatsapp-2025/) com qualquer sistema.

**Site oficial:** [evolution-api.com](https://evolution-api.com/)
**GitHub:** [EvolutionAPI/evolution-api](https://github.com/EvolutionAPI/evolution-api)

---

## Por que Evolution API é a melhor escolha

### vs WhatsApp Business API Oficial:
- ✅ **Grátis** vs $0.005-0.02/mensagem
- ✅ **Sem aprovação** vs 7-14 dias de espera
- ✅ **Ilimitado** vs limites por tier
- ✅ **Self-hosted** vs dependência do Meta

### vs Alternativas pagas (Z-API, WPPConnect Cloud):
- ✅ **R$ 0/mês** vs R$ 50-300/mês
- ✅ **Controle total** vs vendor lock-in
- ✅ **Código aberto** vs caixa preta

**Único "custo":** VPS R$ 50-80/mês (hospedagem)

---

## Instalação passo a passo

### Requisitos:
- VPS com Ubuntu 20.04+ (2GB RAM, 20GB disco)
- Docker + Docker Compose instalado
- Domínio/IP público (para webhooks)

### Passo 1: Instalar Docker
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Docker
curl -fsSL https://get.docker.com | sh

# Adicionar usuário ao grupo docker
sudo usermod -aG docker $USER

# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verificar instalação
docker --version
docker-compose --version
```

### Passo 2: Clonar Evolution API
```bash
git clone https://github.com/EvolutionAPI/evolution-api
cd evolution-api
```

### Passo 3: Configurar variáveis
```bash
cp .env.example .env
nano .env
```

**Configurações essenciais:**
```env
# API
AUTHENTICATION_API_KEY=minha_chave_secreta_123

# Base de dados (PostgreSQL recomendado)
DATABASE_ENABLED=true
DATABASE_PROVIDER=postgresql
DATABASE_CONNECTION_URI=postgresql://user:pass@localhost:5432/evolution

# Webhook global (opcional)
WEBHOOK_GLOBAL_URL=https://meu-servidor.com/webhook

# Porta
PORT=8080
```

### Passo 4: Subir com Docker Compose
```bash
docker-compose up -d

# Verificar logs
docker-compose logs -f
```

**Acesso:** http://seu-vps-ip:8080

---

## Configurar instância WhatsApp

### Via Interface Web:
1. Acesse: http://seu-vps:8080
2. Criar nova instância: `minha-empresa`
3. Gerar QR Code
4. Escanear com WhatsApp Business (Aparelhos conectados)

### Via API (automatizado):
```python
import requests

EVOLUTION_URL = "http://localhost:8080"
API_KEY = "minha_chave_secreta_123"

# Criar instância
response = requests.post(
    f"{EVOLUTION_URL}/instance/create",
    headers={"apikey": API_KEY},
    json={
        "instanceName": "minha-empresa",
        "qrcode": True
    }
)

qr_code = response.json()["qrcode"]["base64"]
print(f"Escaneie: {qr_code}")
```

---

## Enviar mensagens (Código)

### Python:
```python
import requests

def enviar_mensagem(numero, texto):
    url = "http://localhost:8080/message/sendText/minha-empresa"
    
    payload = {
        "number": numero,  # 5511999999999
        "text": texto
    }
    
    headers = {"apikey": "minha_chave_secreta_123"}
    
    return requests.post(url, json=payload, headers=headers).json()

# Usar
enviar_mensagem("5511999999999", "Olá da Evolution API!")
```

### JavaScript (Node.js):
```javascript
const axios = require('axios');

async function enviarMensagem(numero, texto) {
    const response = await axios.post(
        'http://localhost:8080/message/sendText/minha-empresa',
        {
            number: numero,
            text: texto
        },
        {
            headers: {'apikey': 'minha_chave_secreta_123'}
        }
    );
    return response.data;
}

// Usar
enviarMensagem('5511999999999', 'Olá da Evolution API!');
```

---

## Webhooks (Receber mensagens)

### Configurar webhook:
```bash
curl -X POST http://localhost:8080/webhook/set/minha-empresa \
  -H "apikey: minha_chave_secreta_123" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://meu-servidor.com/webhook",
    "webhook_by_events": false,
    "events": ["messages.upsert"]
  }'
```

### Servidor webhook (Flask):
```python
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    
    # Extrair dados
    numero = data["key"]["remoteJid"].split("@")[0]
    mensagem = data["message"]["conversation"]
    
    print(f"📱 {numero}: {mensagem}")
    
    # Responder (integrar com [chatbot IA](/blog/chatbot-whatsapp-guia-completo-2025/))
    resposta = gpt4_responder(mensagem)
    
    requests.post(
        "http://localhost:8080/message/sendText/minha-empresa",
        headers={"apikey": "minha_chave_secreta_123"},
        json={"number": numero, "text": resposta}
    )
    
    return "ok"

if __name__ == "__main__":
    app.run(port=5000)
```

---

## Recursos avançados

### 1. Enviar mídias
```python
# Imagem
payload = {
    "number": "5511999999999",
    "mediaMessage": {
        "mediatype": "image",
        "media": "https://exemplo.com/foto.jpg",
        "caption": "Veja esta imagem!"
    }
}

# Documento
payload = {
    "number": "5511999999999",
    "mediaMessage": {
        "mediatype": "document",
        "media": "https://exemplo.com/pdf.pdf",
        "fileName": "catalogo.pdf"
    }
}
```

### 2. Grupos
```python
# Criar grupo
payload = {
    "subject": "Meu Grupo",
    "participants": ["5511999999999", "5511888888888"]
}
requests.post(f"{url}/group/create/minha-empresa", ...)

# Enviar mensagem em grupo
payload = {
    "number": "120363xxxxxx@g.us",  # ID do grupo
    "text": "Mensagem para o grupo"
}
```

### 3. Botões (WhatsApp Business)
```python
payload = {
    "number": "5511999999999",
    "buttonMessage": {
        "title": "Escolha uma opção",
        "buttons": [
            {"buttonId": "1", "buttonText": {"displayText": "Sim"}},
            {"buttonId": "2", "buttonText": {"displayText": "Não"}}
        ]
    }
}
```

---

## Integrar com IA ([Chatbot](/blog/chatbot-whatsapp-guia-completo-2025/))

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

def gpt4_responder(mensagem):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Você é assistente da Empresa X"},
            {"role": "user", "content": mensagem}
        ]
    )
    return response.choices[0].message.content

# Usar no webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    mensagem_cliente = data["message"]["conversation"]
    resposta_ia = gpt4_responder(mensagem_cliente)
    enviar_mensagem(numero, resposta_ia)
```

---

## Troubleshooting

### QR Code não aparece:
```bash
# Ver logs
docker-compose logs -f

# Reiniciar
docker-compose restart
```

### Webhook não recebe:
- Verificar URL pública acessível
- Testar com ngrok: `ngrok http 5000`
- Checar firewall VPS (liberar porta)

### Desconexão frequente:
- Usar WhatsApp Business (não pessoal)
- Evitar usar mesmo número em múltiplos lugares
- Manter Docker rodando com PM2/supervisor

---

## Documentação oficial

- **[Evolution API Docs](https://doc.evolution-api.com/)**
- **[GitHub](https://github.com/EvolutionAPI/evolution-api)**
- **[Comunidade Discord](https://discord.gg/evolution-api)**

---

## Próximos passos

1. **[Criar Chatbot IA](/blog/chatbot-whatsapp-guia-completo-2025/)** - Automatizar respostas
2. **[Automação WhatsApp](/blog/automacao-whatsapp-2025/)** - Workflows completos
3. **[Integrar CRM](/blog/crm-vendas-guia-completo-2025/)** - Centralizar leads

---

**Sobre o autor:** Felipe Zanoni é especialista em Evolution API, com 300+ implementações para empresas brasileiras.
