---
title: "Chatbot Gratuito: Guia Completo 2025"
description: "Crie chatbot gratuito com IA: 7 plataformas testadas, comparação completa e tutorial passo a passo. OpenAI grátis, Evolution API e alternativas no-code."
publishDate: 2025-01-24
author: "Felipe Zanoni"
category: "IA"
tags: ["chatbot gratuito", "chatbot gratis", "ia gratis", "whatsapp gratis"]
draft: false
---

> **📚 Série:** Chatbots & IA
> → [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/) | [Chatbot IA](/blog/chatbot-ia-2025/) | [WhatsApp Bot](/blog/whatsapp-bot-2025/)

## O que é chatbot gratuito?

Chatbot gratuito é sistema de atendimento automatizado com IA que não cobra mensalidade. Usa ferramentas open-source ([Evolution API](/blog/evolution-api-tutorial-completo/)), modelos gratuitos (Claude Haiku $0.25/1M tokens) ou tiers grátis de plataformas (Manychat, ManyChat, Landbot). Ideal para PMEs, startups e testes antes de escalar. Custo real: R$ 0-50/mês (apenas hospedagem).

---

## 7 Formas de criar chatbot grátis (2025)

### 1. Evolution API + Claude Haiku (Recomendado)

**Custo:** R$ 0-30/mês
**Dificuldade:** Médio (precisa código)
**Mensagens:** Ilimitadas

**Stack:**
- [Evolution API](/blog/evolution-api-tutorial-completo/) (WhatsApp, grátis)
- Claude Haiku ($0.25/1M tokens = ~R$ 1.25)
- [Flask](/blog/flask-python-tutorial-2025/) (servidor webhook)
- VPS Hostinger (R$ 30/mês) ou Render grátis

**Tutorial completo:** [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)

**Vantagens:**
- ✅ 100% customizável
- ✅ Sem limites de mensagens
- ✅ Controle total dos dados
- ✅ Integra com qualquer sistema

**Desvantagens:**
- ❌ Precisa programar (Python)
- ❌ Precisa manter servidor

---

### 2. Manychat Free Plan

**Custo:** R$ 0
**Dificuldade:** Fácil (no-code)
**Mensagens:** 1.000/mês grátis

**Recursos grátis:**
- ✅ Facebook Messenger + Instagram DM
- ✅ Flows visuais (drag & drop)
- ✅ Automação básica
- ✅ Broadcasting 1.000 contatos

**Limitações:**
- ❌ WhatsApp não disponível no grátis
- ❌ IA limitada (sem GPT-4)
- ❌ Branding Manychat

**Site:** [manychat.com](https://manychat.com/)

---

### 3. ManyChat para WhatsApp (Tier grátis)

**Custo:** R$ 0 até 1.000 contatos
**Dificuldade:** Fácil
**Mensagens:** Ilimitadas (dentro dos 1.000 contatos)

**Recursos:**
- ✅ WhatsApp Business API oficial
- ✅ Automação visual
- ✅ Templates de mensagem
- ✅ Integrações (Zapier, Google Sheets)

**Upgrade:** $15/mês para remover branding

**Site:** [manychat.com/whatsapp](https://manychat.com/whatsapp-business-api)

---

### 4. Landbot Free

**Custo:** R$ 0
**Dificuldade:** Fácil
**Mensagens:** 100 chats/mês

**Recursos grátis:**
- ✅ Website chatbot
- ✅ WhatsApp (100 chats)
- ✅ Interface conversacional
- ✅ Integrações básicas

**Limitação:** 100 conversas = ~3-4 por dia

**Site:** [landbot.io](https://landbot.io/)

---

### 5. Chatfuel Free

**Custo:** R$ 0
**Dificuldade:** Fácil
**Mensagens:** 50/mês

**Recursos:**
- ✅ Facebook Messenger
- ✅ Instagram
- ✅ Flows visuais

**Limitação crítica:** Apenas 50 mensagens/mês = ~1-2 por dia

**Site:** [chatfuel.com](https://chatfuel.com/)

---

### 6. Botpress Cloud Free

**Custo:** R$ 0
**Dificuldade:** Médio
**Mensagens:** 2.000/mês

**Recursos:**
- ✅ Open-source
- ✅ IA integrada (NLU)
- ✅ Multi-canal (WhatsApp, Web, Messenger)
- ✅ Self-hosted possível

**Site:** [botpress.com](https://botpress.com/)

---

### 7. DIY: OpenAI Free Tier + Twilio

**Custo:** $0 (trial credits)
**Dificuldade:** Avançado
**Mensagens:** Limitadas pelos credits

**Stack:**
- OpenAI Free Trial ($5 credits)
- Twilio WhatsApp Sandbox (grátis para testes)
- [Flask](/blog/flask-python-tutorial-2025/) webhook

**Limitação:** Apenas para testes (não produção)

---

## Comparação: Qual escolher?

| Plataforma | Custo/mês | Msgs grátis | WhatsApp | IA | Dificuldade |
|------------|-----------|-------------|----------|-----|-------------|
| **Evolution API + Haiku** | R$ 0-30 | Ilimitadas | ✅ | ✅ Claude | ⚠️ Média |
| **Manychat** | R$ 0 | 1.000 | ❌ | ⚠️ Limitada | ✅ Fácil |
| **ManyChat WhatsApp** | R$ 0 | ∞ (1k contatos) | ✅ | ❌ | ✅ Fácil |
| **Landbot** | R$ 0 | 100 | ✅ | ⚠️ Básica | ✅ Fácil |
| **Chatfuel** | R$ 0 | 50 | ❌ | ❌ | ✅ Fácil |
| **Botpress** | R$ 0 | 2.000 | ✅ | ✅ NLU | ⚠️ Média |

**Recomendação:**
- **PME com dev:** Evolution API + Haiku
- **Iniciante sem código:** ManyChat WhatsApp
- **Teste rápido:** Landbot (100 chats)

---

## Tutorial: Chatbot grátis com Evolution API

### Passo 1: Instalar Evolution API

```bash
# Clone repositório
git clone https://github.com/EvolutionAPI/evolution-api
cd evolution-api

# Configurar .env
cp .env.example .env
nano .env

# Subir com Docker
docker-compose up -d
```

**Tutorial completo:** [Evolution API](/blog/evolution-api-tutorial-completo/)

### Passo 2: Criar conta Anthropic (Claude)

1. Acesse: [console.anthropic.com](https://console.anthropic.com/)
2. Criar conta (grátis)
3. Adicionar créditos ($5 mínimo)
4. Copiar API key

**Custo real:**
- Claude Haiku: $0.25/1M tokens input
- 1 conversa média = ~500 tokens
- 1M conversas = R$ 1.25
- **Prático:** R$ 5-15/mês para PME

### Passo 3: Webhook Python

```python
# webhook.py
from flask import Flask, request
import anthropic
import requests
import os

app = Flask(__name__)

# Config
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
EVOLUTION_URL = os.getenv('EVOLUTION_URL')
EVOLUTION_KEY = os.getenv('EVOLUTION_KEY')

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    # Extrair mensagem
    numero = data["key"]["remoteJid"].split("@")[0]
    mensagem = data["message"]["conversation"]

    # Chamar Claude Haiku
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=200,
        messages=[
            {"role": "user", "content": mensagem}
        ]
    )

    resposta = response.content[0].text

    # Enviar via Evolution API
    requests.post(
        f"{EVOLUTION_URL}/message/sendText/instance",
        json={"number": numero, "text": resposta},
        headers={"apikey": EVOLUTION_KEY}
    )

    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
```

### Passo 4: Deploy grátis (Render)

```yaml
# render.yaml
services:
  - type: web
    name: chatbot-webhook
    env: python
    buildCommand: pip install flask anthropic requests
    startCommand: python webhook.py
```

**Conectar GitHub → Deploy automático**

**Tutorial:** [Deploy Aplicação](/blog/deploy-aplicacao-python-2025/)

---

## Modelos de IA gratuitos/baratos

### 1. Claude Haiku (Recomendado)

**Custo:** $0.25/1M tokens
**Qualidade:** ✅ Excelente
**Velocidade:** ✅ Rápida (1-2s)

**Uso:**
```python
from anthropic import Anthropic

client = Anthropic(api_key="sk-ant-...")
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=200,
    messages=[{"role": "user", "content": "Olá!"}]
)
```

### 2. OpenAI GPT-3.5 Turbo

**Custo:** $0.50/1M tokens
**Qualidade:** ⚠️ Boa (inferior ao Haiku)
**Velocidade:** ✅ Rápida

### 3. Gemini Flash (Google)

**Custo:** Grátis até 1.500 reqs/dia
**Qualidade:** ✅ Boa
**Limitação:** Rate limit baixo

**API:** [ai.google.dev](https://ai.google.dev/)

### 4. Groq (Llama 3)

**Custo:** Grátis (beta)
**Qualidade:** ⚠️ Moderada
**Velocidade:** ✅ Muito rápida (tokens/s)

**API:** [groq.com](https://groq.com/)

---

## Casos reais: Custos reais

### Caso 1: Padaria (300 conversas/mês)

**Stack:**
- Evolution API (VPS R$ 30)
- Claude Haiku (150k tokens = R$ 0.40)
- **Total:** R$ 30.40/mês

**vs Pago:**
- Manychat Pro: R$ 75/mês
- **Economia:** R$ 44.60/mês (60%)

### Caso 2: E-commerce (1.500 conversas/mês)

**Stack:**
- Evolution API (VPS R$ 50)
- Claude Haiku (750k tokens = R$ 2)
- **Total:** R$ 52/mês

**vs Pago:**
- ManyChat Pro: R$ 150/mês
- **Economia:** R$ 98/mês (65%)

### Caso 3: Startup (50 conversas/mês - teste)

**Stack:**
- Evolution API (Render grátis)
- Claude Haiku (25k tokens = R$ 0.08)
- **Total:** R$ 0/mês

---

## Limitações do grátis

### ❌ O que NÃO esperar:

1. **Suporte dedicado** (só comunidade)
2. **SLA 99.9%** (pode ter downtime)
3. **Dashboards avançados** (métricas básicas)
4. **Whitelabel completo** (pode ter branding)

### Quando migrar para pago:

- ✅ >5.000 conversas/mês
- ✅ Precisa SLA 99.9%
- ✅ Múltiplos canais (WhatsApp + IG + FB)
- ✅ Time >3 pessoas

---

## Alternativas open-source (self-hosted)

### 1. Botpress

**GitHub:** [botpress/botpress](https://github.com/botpress/botpress)
**Stack:** Node.js + PostgreSQL
**Dificuldade:** Média

### 2. Rasa

**GitHub:** [RasaHQ/rasa](https://github.com/RasaHQ/rasa)
**Stack:** Python + ML
**Dificuldade:** Avançada

**Ideal para:** NLU customizado

### 3. ChatterBot

**GitHub:** [gunthercox/ChatterBot](https://github.com/gunthercox/ChatterBot)
**Stack:** Python
**Status:** Descontinuado (usar apenas para aprendizado)

---

## Dicas para reduzir custos

### 1. Cache de respostas

```python
cache = {}

def get_response(pergunta):
    if pergunta in cache:
        return cache[pergunta]

    resposta = claude.messages.create(...)
    cache[pergunta] = resposta
    return resposta
```

**Economia:** 50-70% em perguntas repetidas

### 2. Limite de tokens

```python
# Ruim: 1.000 tokens/resposta
max_tokens=1000

# Bom: 150 tokens (suficiente para WhatsApp)
max_tokens=150
```

**Economia:** 85% em custos de output

### 3. Usar tier grátis de hospedagem

**Opções:**
- Render.com (750h grátis/mês)
- Railway ($5 credits/mês)
- Fly.io (3 VMs pequenas grátis)

---

## Chatbot grátis: Prós e contras

### ✅ Vantagens:

- Zero investimento inicial
- Testar viabilidade antes de pagar
- Aprender sem risco
- Validar ideia de negócio

### ❌ Desvantagens:

- Limitações de mensagens/contatos
- Branding de terceiros
- Menos recursos que pago
- Suporte limitado

---

## Documentação

- [Evolution API Docs](https://doc.evolution-api.com/)
- [Claude API](https://docs.anthropic.com/)
- [Manychat Help](https://manychat.com/help)
- [Botpress Docs](https://botpress.com/docs)

---

## Próximos passos

1. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Tutorial completo
2. **[Chatbot IA](/blog/chatbot-ia-2025/)** - Implementar IA
3. **[Evolution API](/blog/evolution-api-tutorial-completo/)** - Setup completo
4. **[CRM Gratuito](/blog/crm-gratuito-2025/)** - Integrar vendas

---

**Sobre o autor:** Felipe Zanoni é especialista em chatbots, com 200+ implementações gratuitas e pagas para empresas brasileiras.
