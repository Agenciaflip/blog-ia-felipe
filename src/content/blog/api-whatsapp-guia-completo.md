---
title: "API WhatsApp: Guia Completo 2025"
description: "Integre WhatsApp Business API: Evolution API grátis vs oficial paga. Tutorial Python/Node.js, webhooks, envio de mensagens e mídia. Cases reais."
publishDate: 2025-01-19
author: "Felipe Zanoni"
category: "WhatsApp"
tags: ["api whatsapp", "whatsapp business api", "evolution api", "integração whatsapp"]
draft: false
---

> **📚 Série:** Automação WhatsApp com IA
> → [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/) | [Automação WhatsApp](/blog/automacao-whatsapp-2025/) | [Evolution API](/blog/evolution-api-tutorial-completo/)

## O que é API WhatsApp?

API WhatsApp é uma interface que permite sistemas enviarem/receberem mensagens WhatsApp via código. Empresas usam para criar [chatbots](/blog/chatbot-whatsapp-guia-completo-2025/), integrar [CRMs](/blog/crm-vendas-guia-completo-2025/) e [automatizar atendimento](/blog/automacao-whatsapp-2025/). Existem 2 tipos: oficial (paga) e não-oficial como [Evolution API](/blog/evolution-api-tutorial-completo/) (grátis).

---

## WhatsApp Business API vs Evolution API

| Recurso | WhatsApp API Oficial | Evolution API (Open-source) |
|---------|----------------------|----------------------------|
| **Custo** | $0.005-0.02/mensagem | Grátis (VPS R$ 50/mês) |
| **Aprovação** | Exige aprovação Meta (7-14 dias) | Instantâneo |
| **Limites** | 1.000-100k msgs/dia (conforme tier) | Ilimitado |
| **Mídia** | Imagens, vídeos, docs, áudio | Todos suportados |
| **Webhooks** | Sim | Sim |
| **Suporte** | Meta oficial | Comunidade GitHub |
| **Ideal para** | Grandes empresas | PMEs, devs, startups |

**Recomendação:** Comece com [Evolution API](/blog/evolution-api-tutorial-completo/) (grátis), migre para oficial se crescer muito.

---

## Tutorial: Enviar mensagem via API (Python)

### Evolution API:
```python
import requests

EVOLUTION_URL = "https://sua-evolution.com.br"
API_KEY = "sua_api_key"
INSTANCE = "sua_instancia"

def enviar_mensagem(numero, texto):
    url = f"{EVOLUTION_URL}/message/sendText/{INSTANCE}"
    
    payload = {
        "number": numero,  # Ex: 5511999999999
        "text": texto
    }
    
    headers = {"apikey": API_KEY}
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Uso
enviar_mensagem("5511999999999", "Olá! Esta é uma mensagem via API")
```

### WhatsApp Business API Oficial:
```python
import requests

ACCESS_TOKEN = "seu_token"
PHONE_NUMBER_ID = "seu_phone_id"

def enviar_oficial(numero, texto):
    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
    
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": texto}
    }
    
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
```

**Documentação:** [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/)

---

## Recursos avançados

### 1. Enviar imagens
```python
payload = {
    "number": "5511999999999",
    "mediaMessage": {
        "mediatype": "image",
        "media": "https://exemplo.com/imagem.jpg",
        "caption": "Veja nossa promoção!"
    }
}
```

### 2. Webhooks (receber mensagens)
```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    
    numero = data["key"]["remoteJid"].split("@")[0]
    mensagem = data["message"]["conversation"]
    
    print(f"Mensagem de {numero}: {mensagem}")
    
    # Responder via [chatbot](/blog/chatbot-whatsapp-guia-completo-2025/)
    
    return "ok"
```

### 3. Botões interativos
```python
payload = {
    "number": "5511999999999",
    "options": [
        {"id": "1", "title": "Sim"},
        {"id": "2", "title": "Não"}
    ],
    "title": "Confirmar pedido?",
    "footer": "Responda com botão"
}
```

---

## Integrações populares

- **[CRM](/blog/crm-vendas-guia-completo-2025/):** HubSpot, Pipedrive, Salesforce
- **[Automação](/blog/automacao-whatsapp-2025/):** Zapier, N8N, Make
- **E-commerce:** WooCommerce, Shopify, Magento
- **Agendamento:** Google Calendar, Calendly
- **Pagamentos:** Stripe, Mercado Pago

---

## Caso Real: Suporte automatizado

**Empresa:** SaaS B2B (50 clientes)

**Solução:**
- Evolution API + GPT-4
- Integração com sistema de tickets
- Rastreamento de bugs em tempo real

**Resultados:**
- ✅ 73% tickets resolvidos pela IA
- ✅ Tempo resposta: 4h → 2min
- ✅ CSAT: 78 → 92
- ✅ Custo: R$ 280/mês
- ✅ Economia: R$ 4.200/mês vs +1 atendente

---

## Documentação oficial

- [Evolution API Docs](https://doc.evolution-api.com/)
- [WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp/)
- [WhatsApp Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/)

---

## Próximos passos

1. **[Tutorial Evolution API](/blog/evolution-api-tutorial-completo/)** - Setup completo
2. **[Criar Chatbot](/blog/chatbot-whatsapp-guia-completo-2025/)** - Automatizar respostas
3. **[Automação WhatsApp](/blog/automacao-whatsapp-2025/)** - Workflows avançados

---

**Sobre o autor:** Felipe Zanoni é desenvolvedor especializado em integrações WhatsApp, com 500+ horas de experiência.
