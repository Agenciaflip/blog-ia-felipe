---
title: "WhatsApp Bot: Guia Completo 2025"
description: "Criar WhatsApp bot: Python, Node.js, Evolution API e automações. Tutorial completo com código, deploy e casos reais. ROI 300%+ comprovado."
publishDate: 2025-01-25
author: "Felipe Zanoni"
category: "WhatsApp"
tags: ["whatsapp bot", "bot whatsapp", "automação whatsapp", "python whatsapp"]
draft: false
---

> **📚 Série:** Automação WhatsApp
> → [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/) | [Automação WhatsApp](/blog/automacao-whatsapp-2025/) | [API WhatsApp](/blog/api-whatsapp-guia-completo/)

## O que é WhatsApp bot?

WhatsApp bot é programa automatizado que envia/recebe mensagens WhatsApp via API, sem intervenção humana. Bots executam tarefas como: responder FAQs, enviar lembretes, qualificar leads, processar pedidos e integrar com sistemas ([CRM](/blog/crm-vendas-guia-completo-2025/), e-commerce). Empresas economizam 70% do tempo de atendimento e aumentam conversões em 40-60% com bots WhatsApp.

---

## Tipos de WhatsApp bots

### 1. Bot de respostas automáticas

**Função:** Responde mensagens com regras fixas

**Exemplo:**
```
Cliente: "Horário"
Bot: "Funcionamos seg-sex 9h-18h"
```

**Complexidade:** ✅ Baixa
**Uso:** FAQs, informações básicas

### 2. Bot com IA ([Chatbot](/blog/chatbot-whatsapp-guia-completo-2025/))

**Função:** Entende contexto e responde inteligentemente

**Exemplo:**
```
Cliente: "Quanto custa o produto X?"
Bot: [busca no banco] "O produto X custa R$ 49,90. Quer adicionar ao carrinho?"
```

**Complexidade:** ⚠️ Média
**Uso:** Atendimento, vendas, suporte

### 3. Bot de notificações

**Função:** Envia mensagens proativas

**Exemplo:**
- Lembrete de consulta (24h antes)
- Status de pedido
- Boleto vencendo

**Complexidade:** ✅ Baixa
**Uso:** Alertas, campanhas

### 4. Bot transacional

**Função:** Processa ações (pagamentos, pedidos)

**Exemplo:**
```
Cliente: "Pedir 2 pizzas calabresa"
Bot: [cria pedido] "Pedido #123 criado. Total: R$ 78. PIX ou cartão?"
```

**Complexidade:** ❌ Alta
**Uso:** E-commerce, delivery

---

## 3 formas de criar WhatsApp bot

### Opção 1: [Evolution API](/blog/evolution-api-tutorial-completo/) + Python (Recomendado)

**Vantagens:**
- ✅ Grátis e open-source
- ✅ Controle total
- ✅ Ilimitado

**Desvantagens:**
- ❌ Precisa programar
- ❌ Precisa VPS

**Stack:**
- Evolution API (WhatsApp)
- [Flask](/blog/flask-python-tutorial-2025/) (webhook)
- OpenAI/Claude (IA opcional)

**Tutorial completo:** [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)

### Opção 2: WhatsApp Business API Oficial

**Vantagens:**
- ✅ Oficial do Meta
- ✅ Confiável
- ✅ Recursos avançados

**Desvantagens:**
- ❌ Pago ($0.005-0.02/msg)
- ❌ Aprovação demorada (7-14 dias)
- ❌ Limites por tier

**Documentação:** [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/)

### Opção 3: Plataformas no-code

**Opções:**
- Manychat ($15-145/mês)
- MobileMonkey ($19-299/mês)
- Landbot ($40-400/mês)

**Vantagens:**
- ✅ Sem código
- ✅ Interface visual

**Desvantagens:**
- ❌ Custo mensal alto
- ❌ Vendor lock-in

---

## Tutorial: Bot Python com Evolution API

### Passo 1: Setup Evolution API

```bash
# Instalar Docker
curl -fsSL https://get.docker.com | sh

# Clonar Evolution API
git clone https://github.com/EvolutionAPI/evolution-api
cd evolution-api

# Configurar
cp .env.example .env
nano .env  # Adicionar API_KEY

# Subir
docker-compose up -d
```

**Docs:** [Evolution API Tutorial](/blog/evolution-api-tutorial-completo/)

### Passo 2: Criar bot Python

```python
# bot.py
from flask import Flask, request
import requests
import os

app = Flask(__name__)

EVOLUTION_URL = os.getenv('EVOLUTION_URL', 'http://localhost:8080')
API_KEY = os.getenv('API_KEY')
INSTANCE = os.getenv('INSTANCE', 'minha-instancia')

def enviar_mensagem(numero, texto):
    """Envia mensagem via Evolution API"""
    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE}"

    payload = {
        "number": numero,
        "text": texto
    }

    headers = {"apikey": API_KEY}

    return requests.post(url, json=payload, headers=headers).json()

@app.route('/webhook', methods=['POST'])
def webhook():
    """Recebe mensagens do WhatsApp"""
    data = request.json

    # Extrair dados
    numero = data["key"]["remoteJid"].split("@")[0]
    mensagem = data["message"]["conversation"].lower()

    # Lógica de respostas
    if "horário" in mensagem or "horario" in mensagem:
        resposta = "Funcionamos seg-sex 9h-18h, sáb 9h-13h"

    elif "preço" in mensagem or "preco" in mensagem:
        resposta = "Nossos preços variam de R$ 50 a R$ 500. Qual produto te interessa?"

    elif "endereço" in mensagem or "endereco" in mensagem:
        resposta = "Rua Exemplo, 123 - São Paulo/SP"

    else:
        resposta = "Olá! Como posso ajudar? Digite: horário, preço ou endereço"

    # Enviar resposta
    enviar_mensagem(numero, resposta)

    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
```

### Passo 3: Configurar webhook

```bash
# Configurar webhook na Evolution API
curl -X POST http://localhost:8080/webhook/set/minha-instancia \
  -H "apikey: SUA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://seu-servidor.com/webhook",
    "events": ["messages.upsert"]
  }'
```

### Passo 4: Deploy

**Opção A: VPS**

```bash
# Copiar bot para servidor
scp bot.py user@servidor:/home/user/

# SSH no servidor
ssh user@servidor

# Instalar dependências
pip install flask requests

# Rodar com PM2
pm2 start bot.py --name whatsapp-bot
pm2 save
```

**Opção B: Render.com (grátis)**

```yaml
# render.yaml
services:
  - type: web
    name: whatsapp-bot
    env: python
    buildCommand: pip install flask requests
    startCommand: python bot.py
```

---

## Bot com IA (GPT-4)

```python
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/webhook', methods=['POST'])
def webhook_ia():
    data = request.json

    numero = data["key"]["remoteJid"].split("@")[0]
    mensagem = data["message"]["conversation"]

    # Chamar GPT-4
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é assistente da Empresa X. Seja breve (max 2 linhas)."},
            {"role": "user", "content": mensagem}
        ],
        max_tokens=100
    )

    resposta = response.choices[0].message.content

    # Enviar
    enviar_mensagem(numero, resposta)

    return '', 200
```

**Custo:** GPT-4o-mini = $0.15/1M tokens (R$ 0.75)

**Tutorial:** [API OpenAI](/blog/api-openai-python-2025/)

---

## Bot Node.js (alternativa)

```javascript
// bot.js
const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

const EVOLUTION_URL = process.env.EVOLUTION_URL;
const API_KEY = process.env.API_KEY;
const INSTANCE = process.env.INSTANCE;

async function enviarMensagem(numero, texto) {
    await axios.post(
        `${EVOLUTION_URL}/message/sendText/${INSTANCE}`,
        { number: numero, text: texto },
        { headers: { apikey: API_KEY } }
    );
}

app.post('/webhook', async (req, res) => {
    const data = req.body;

    const numero = data.key.remoteJid.split('@')[0];
    const mensagem = data.message.conversation.toLowerCase();

    let resposta;

    if (mensagem.includes('horário')) {
        resposta = 'Funcionamos seg-sex 9h-18h';
    } else {
        resposta = 'Como posso ajudar?';
    }

    await enviarMensagem(numero, resposta);

    res.sendStatus(200);
});

app.listen(5000, () => console.log('Bot rodando na porta 5000'));
```

---

## Recursos avançados

### 1. Enviar mídias

```python
# Enviar imagem
def enviar_imagem(numero, url_imagem, legenda):
    payload = {
        "number": numero,
        "mediaMessage": {
            "mediatype": "image",
            "media": url_imagem,
            "caption": legenda
        }
    }

    requests.post(
        f"{EVOLUTION_URL}/message/sendMedia/{INSTANCE}",
        json=payload,
        headers={"apikey": API_KEY}
    )

# Uso
enviar_imagem("5511999999999", "https://exemplo.com/foto.jpg", "Veja nossa promoção!")
```

### 2. Botões interativos

```python
payload = {
    "number": "5511999999999",
    "buttonMessage": {
        "text": "Escolha uma opção:",
        "buttons": [
            {"buttonId": "1", "buttonText": {"displayText": "✅ Sim"}},
            {"buttonId": "2", "buttonText": {"displayText": "❌ Não"}}
        ]
    }
}
```

### 3. Listas (menu)

```python
payload = {
    "number": "5511999999999",
    "listMessage": {
        "title": "Nossos produtos",
        "buttonText": "Ver opções",
        "sections": [
            {
                "title": "Categoria A",
                "rows": [
                    {"title": "Produto 1", "description": "R$ 50"},
                    {"title": "Produto 2", "description": "R$ 80"}
                ]
            }
        ]
    }
}
```

---

## Casos reais

### Caso 1: Padaria automatizou pedidos

**Empresa:** Padaria artesanal (2 atendentes)

**Antes:**
- Atendentes passavam 5h/dia no WhatsApp
- Pedidos perdidos (esqueciam de responder)

**Bot implementado:**
- Cardápio automatizado (lista interativa)
- Pedidos registrados automaticamente
- Confirmação via WhatsApp

**Resultados:**
- ✅ Tempo atendimento: 5h → 1h/dia
- ✅ Pedidos aumentaram 35%
- ✅ 0% pedidos perdidos
- ✅ Custo bot: R$ 40/mês (VPS)

### Caso 2: Clínica reduziu no-show 60%

**Empresa:** Clínica odontológica (3 dentistas)

**Bot:**
- Lembrete automático 24h antes
- Confirmação via botão (Sim/Não)
- Se não confirma → liga pra reagendar

**Resultados:**
- ✅ No-show: 25% → 10%
- ✅ 15% mais consultas/mês
- ✅ R$ 12k receita adicional/mês

### Caso 3: E-commerce recuperou carrinhos

**Bot:**
- Detecta carrinho abandonado
- Após 1h: "Olá! Vi que você deixou produtos..."
- Após 24h: Cupom 10% desconto

**Resultados:**
- ✅ 18% carrinhos recuperados
- ✅ R$ 47k receita adicional/mês
- ✅ ROI: 12.300%

**Tutorial:** [Automação WhatsApp](/blog/automacao-whatsapp-2025/)

---

## Boas práticas

### ✅ FAÇA:

1. **Sempre se identifique como bot**
```python
resposta = "🤖 Olá! Sou um assistente automático. Como posso ajudar?"
```

2. **Respeite horários**
```python
from datetime import datetime

hora_atual = datetime.now().hour

if 9 <= hora_atual <= 18:
    enviar_mensagem(numero, resposta)
else:
    # Não enviar notificações à noite
    pass
```

3. **Ofereça opção de humano**
```python
if "atendente" in mensagem or "humano" in mensagem:
    enviar_mensagem(numero, "Transferindo para atendente humano...")
    # Notificar equipe
```

4. **Limite de mensagens**
```python
# Máximo 1 mensagem/dia por contato (LGPD)
```

### ❌ NÃO FAÇA:

1. ❌ Enviar spam (múltiplas mensagens não solicitadas)
2. ❌ Comprar listas de contatos
3. ❌ Usar número pessoal (use WhatsApp Business)
4. ❌ Responder infinitamente (limitar loops)

---

## Integrações úteis

### 1. [CRM](/blog/crm-vendas-guia-completo-2025/) (HubSpot, Pipedrive)

```python
# Criar contato no HubSpot após mensagem
import requests

def criar_contato_hubspot(nome, numero):
    requests.post(
        "https://api.hubapi.com/crm/v3/objects/contacts",
        json={
            "properties": {
                "firstname": nome,
                "phone": numero,
                "lifecyclestage": "lead"
            }
        },
        headers={"Authorization": f"Bearer {HUBSPOT_TOKEN}"}
    )
```

### 2. Pagamentos (Stripe, Mercado Pago)

```python
# Gerar link de pagamento
def gerar_link_pagamento(valor, descricao):
    response = requests.post(
        "https://api.mercadopago.com/checkout/preferences",
        json={
            "items": [{"title": descricao, "unit_price": valor, "quantity": 1}]
        },
        headers={"Authorization": f"Bearer {MP_TOKEN}"}
    )

    return response.json()["init_point"]

# Enviar link
link = gerar_link_pagamento(50.00, "Produto X")
enviar_mensagem(numero, f"Pague aqui: {link}")
```

### 3. Google Calendar (agendamentos)

```python
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Criar evento
service = build('calendar', 'v3', credentials=creds)

event = {
    'summary': 'Consulta - Cliente X',
    'start': {'dateTime': '2025-01-30T10:00:00-03:00'},
    'end': {'dateTime': '2025-01-30T11:00:00-03:00'},
}

service.events().insert(calendarId='primary', body=event).execute()
```

---

## Documentação

- [Evolution API](https://doc.evolution-api.com/)
- [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp/)
- [OpenAI API](https://platform.openai.com/docs)

---

## Próximos passos

1. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Bot com IA
2. **[Automação WhatsApp](/blog/automacao-whatsapp-2025/)** - Workflows
3. **[Evolution API](/blog/evolution-api-tutorial-completo/)** - Setup completo
4. **[API OpenAI](/blog/api-openai-python-2025/)** - Integrar IA

---

**Sobre o autor:** Felipe Zanoni é especialista em WhatsApp bots, com 300+ implementações para empresas brasileiras.
