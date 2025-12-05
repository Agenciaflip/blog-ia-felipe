---
title: "Chatbot WhatsApp Grátis: Guia Completo 2025"
description: "Crie chatbot WhatsApp grátis com Evolution API + N8N: atenda clientes 24/7, automatize vendas e economize R$ 3-8k/mês vs plataformas pagas."
publishDate: 2025-01-14
author: "Felipe Zanoni"
category: "WhatsApp"
tags: ["chatbot whatsapp", "evolution api", "whatsapp grátis", "automação whatsapp"]
draft: false
---

> **📚 Série:** WhatsApp Business Automation
> → [WhatsApp Business API](/blog/whatsapp-business-api-guia-completo-2025/) | [N8N](/blog/n8n-automacao-guia-completo-2025/) | [IA para Vendas](/blog/ia-para-vendas-2025/)

## O que é Chatbot WhatsApp Grátis?

Chatbot WhatsApp grátis usa Evolution API (open-source) + N8N/Make + ChatGPT para automatizar atendimento WhatsApp Business sem mensalidades ($0 vs R$ 300-800/mês plataformas pagas). Stack self-hosted processa mensagens, detecta intenção (vendas/suporte/FAQ) e responde automaticamente 24/7 com taxa resposta <1 minuto vs 2-6h humano. Empresas economizam R$ 3-8k/mês em atendentes e aumentam conversão 40-80% com disponibilidade total.

Diferença vs WhatsApp API Oficial: Evolution API = não-oficial (grátis, sem aprovação Meta) vs API Oficial = $40-200/mês + aprovação rigorosa + limites por tier.

---

## Stack Chatbot Grátis (Custo Total: R$ 50/mês)

### Arquitetura

```
Cliente WhatsApp
       ↓
Evolution API (VPS $20/mês) ← Webhook
       ↓
N8N ($0 self-hosted) ← Lógica/Rotas
       ↓
ChatGPT API ($10-30/mês) ← IA conversacional
       ↓
Database (PostgreSQL/Supabase free)
```

**vs Plataformas Pagas:**
- Manychat: $15-145/mês
- MobileMonkey: $19-199/mês
- Chatfuel: $15-300/mês

**Economia anual:** R$ 3.600 - R$ 10.800

---

## Componentes Stack Grátis

### 1. Evolution API - Servidor WhatsApp

**O que é:** API open-source conecta WhatsApp Web

**Setup VPS (Hostinger/DigitalOcean):**
```bash
# Docker install Evolution API
git clone https://github.com/EvolutionAPI/evolution-api
cd evolution-api
docker-compose up -d

# Acessar: http://seu-vps:8080
```

**Custo:** VPS $20/mês (ilimitadas instâncias WhatsApp)

**Features:**
- Multi-device (5 números simultâneos)
- Webhook (receber/enviar msgs)
- Mídia (imagens, áudios, documentos)
- Grupos (auto-responder)

**Link:** https://github.com/EvolutionAPI/evolution-api

### 2. N8N - Lógica Chatbot

**Workflow exemplo:**
```
Webhook (nova mensagem)
↓
Parse JSON (extrair texto/número)
↓
IF detectar palavra-chave:
  "preço" → Enviar catálogo
  "horário" → Informar funcionamento
  "falar humano" → Criar ticket Zendesk
↓
Else: ChatGPT API (resposta IA)
↓
Send message (Evolution API)
↓
Log conversa (PostgreSQL)
```

**Custo:** $0 (self-hosted) ou $20/mês (n8n.cloud)

### 3. ChatGPT API - IA Conversacional

**Prompt exemplo:**
```python
prompt = f"""
Você é atendente virtual da Padaria Delícia.

Informações:
- Horário: Seg-Sáb 6h-20h, Dom 7h-13h
- Delivery: Grátis pedidos >R$ 30 (raio 5km)
- Produtos: Pães, bolos, salgados

Cliente perguntou: "{mensagem_cliente}"

Responda de forma amigável e objetiva (máximo 2 linhas).
"""

resposta = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
```

**Custo:** $0.002/1k tokens (≈ R$ 10-30/mês para 5k msgs)

### 4. Database - Histórico Conversas

**Opções grátis:**
- **Supabase:** 500MB PostgreSQL (free tier)
- **MongoDB Atlas:** 512MB (free)
- **Google Sheets:** Simples (via API)

**Schema exemplo:**
```sql
CREATE TABLE conversas (
  id SERIAL PRIMARY KEY,
  numero_cliente VARCHAR(20),
  mensagem TEXT,
  resposta_bot TEXT,
  timestamp TIMESTAMP DEFAULT NOW()
);
```

---

## Setup Passo a Passo (1h)

### Passo 1: VPS + Evolution API (20 min)

**1.1 Criar VPS:**
- Hostinger: $20/mês (4GB RAM)
- DigitalOcean: $24/mês (droplet básico)

**1.2 Instalar Docker:**
```bash
curl -fsSL https://get.docker.com | sh
```

**1.3 Clonar Evolution API:**
```bash
git clone https://github.com/EvolutionAPI/evolution-api
cd evolution-api
cp .env.example .env

# Editar .env (API key, database)
nano .env
```

**1.4 Subir serviço:**
```bash
docker-compose up -d
```

**1.5 Conectar WhatsApp:**
- Acessar http://seu-vps-ip:8080
- Escanear QR Code (WhatsApp app)

### Passo 2: N8N Workflow (25 min)

**2.1 Instalar N8N:**
```bash
docker run -d --restart unless-stopped \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

**2.2 Criar workflow:**
1. Webhook node (receber msgs Evolution)
2. IF node (detectar keywords)
3. HTTP Request (ChatGPT API)
4. HTTP Request (Evolution send message)

**2.3 Configurar webhook Evolution:**
```bash
# POST http://evolution-api:8080/webhook/set
{
  "url": "http://n8n-ip:5678/webhook/whatsapp",
  "events": ["messages.upsert"]
}
```

### Passo 3: ChatGPT Integration (10 min)

**3.1 Obter API key:**
- https://platform.openai.com/api-keys
- Criar key (copy)

**3.2 N8N HTTP Request node:**
```json
{
  "url": "https://api.openai.com/v1/chat/completions",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer sk-..."
  },
  "body": {
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "system", "content": "Você é atendente..."},
      {"role": "user", "content": "{{$json.message}}"}
    ]
  }
}
```

### Passo 4: Database Logs (5 min)

**Supabase setup:**
1. Criar projeto: https://supabase.com
2. Criar tabela `conversas`
3. N8N Postgres node: Insert row (cada msg)

---

## 10 Casos de Uso Chatbot Grátis

### 1. E-commerce - Catálogo Automático

**Trigger:** Cliente pergunta "produtos" ou "preço"

**Bot:**
```
Olá! 👋 Temos 3 categorias:

1️⃣ Eletrônicos
2️⃣ Moda
3️⃣ Casa

Qual te interessa? (digite número)
```

**ROI:** Consultoria produto 24/7 (vs horário comercial)

### 2. Agendamento Serviços

**Workflow:**
```
Cliente: "Quero agendar corte"
Bot: "Que dia prefere? (ex: 15/01)"
Cliente: "15/01"
Bot: "Horários disponíveis: 10h, 14h, 16h"
Cliente: "14h"
Bot: ✅ "Agendado! 15/01 14h com João"

→ Salvar Google Calendar (API)
→ Confirmar 1 dia antes (automático)
```

**Conversão:** Salão beleza - Agendamentos +65%

### 3. Rastreio Pedidos

**Integração:**
```
Cliente: "Cadê meu pedido #1234?"
↓
N8N: Query database pedidos
↓
Bot: "Pedido #1234 saiu para entrega! 
Previsão: hoje 18h
Rastreio: BR123456789"
```

**Redução tickets:** -40% suporte

### 4. Qualificação Leads

**Perguntas automáticas:**
```
Bot: "Olá! Para te ajudar melhor:"
1. Seu nome?
Cliente: "João Silva"

2. Empresa?
Cliente: "Acme Corp"

3. Quantos funcionários?
Cliente: "50"

→ If >20 funcionários:
  "Ótimo! Vou te passar pro vendedor especialista"
  → Criar deal CRM + atribuir vendedor

→ If <20:
  "Envio trial grátis no email?"
```

**Leads qualificados:** +180%

### 5. Suporte FAQ Automático

**Base conhecimento:**
```
Perguntas frequentes (match keywords):
- "horário" → "Seg-Sex 9h-18h"
- "delivery" → "Grátis acima R$ 50"
- "pagamento" → "Pix, cartão, boleto"
- "troca" → "Até 7 dias (nota fiscal)"

Não matchou → ChatGPT responde
```

**Resolução 1º nível:** 70% sem humano

### 6. Abandoned Cart WhatsApp

**E-commerce integration:**
```
Cliente abandona carrinho
↓
Aguardar 2h
↓
WhatsApp: "Oi {nome}! Vi que você deixou 
{produto} no carrinho. Finalize agora com 
10% OFF: {link_checkout_desconto}"
```

**Taxa recuperação:** 12-28%

### 7. Feedback Pós-Compra

**3 dias após entrega:**
```
Bot: "Oi {nome}! Como foi sua experiência 
com {produto}? (1-5 estrelas)"

Cliente: "5"
Bot: "🌟 Que ótimo! Deixa avaliação no Google? 
{link_review}"

Cliente: "2"
Bot: "Que pena 😔 O que aconteceu?"
→ Criar ticket urgente (gerente)
```

**NPS:** +35 pontos

### 8. Enquetes/Pesquisas

**Mensalmente:**
```
Bot: "Rápida pesquisa (30seg):
Qual produto quer que adicionemos?

A) Camisetas
B) Bonés  
C) Mochilas
D) Outro (descreva)"

→ Salvar respostas Google Sheets
→ Análise mensal (decidir estoque)
```

**Engajamento:** 40-60% respostas

### 9. Notificações Proativas

**Alertas úteis:**
```
Novo produto lançado:
"🚀 Chegou! iPhone 15 Pro Max
R$ 7.999 (12x sem juros)
{link_comprar}"

Promoção relâmpago:
"⚡ 2h APENAS: 50% OFF todos tênis
{link_loja}"
```

**Taxa clique:** 25-40% (vs 2-5% email)

### 10. Onboarding Clientes

**SaaS workflow:**
```
Novo cadastro → WhatsApp boas-vindas

Dia 1: "👋 Bem-vindo! Assista tutorial 2 min: 
{link_video}"

Dia 3: "Conseguiu fazer X? Precisa ajuda?"

Dia 7: "Dica pro: Use feature Y para 3x resultado"

Dia 14: "Que nota dá pro produto? (1-10)"
```

**Ativação:** +55%

---

## Evolution API vs WhatsApp Oficial

| Aspecto | Evolution API | WhatsApp API Oficial |
|---------|---------------|----------------------|
| **Custo** | Grátis | $40-200/mês |
| **Aprovação Meta** | Não precisa | Rigorosa (7-14 dias) |
| **Limite msgs** | Ilimitado* | 1k/dia (tier 1) |
| **Multi-device** | ✅ 5 números | ⚠️ 1-2 (pago extra) |
| **Setup** | 1 hora | 3-7 dias |
| **Risco ban** | ⚠️ Existe | ❌ Zero (oficial) |
| **Suporte** | Comunidade | Meta oficial |

***Observação:** Evolution não-oficial = risco ban se spam

**Quando Evolution:**
- Pequenas empresas (< 1k msgs/dia)
- Budget limitado
- Precisa agilidade setup

**Quando API Oficial:**
- Empresas grandes (>5k msgs/dia)
- Marca estabelecida (evitar risco)
- Compliance crítico

---

## Próximos passos

Aprofunde em WhatsApp automation:

1. **[WhatsApp Business API](/blog/whatsapp-business-api-guia-completo-2025/)** - API oficial
2. **[N8N](/blog/n8n-automacao-guia-completo-2025/)** - Workflows avançados
3. **[IA para Vendas](/blog/ia-para-vendas-2025/)** - ChatGPT + CRM
4. **[Automação Marketing](/blog/automacao-marketing-2025/)** - Multi-canal
5. **[Chatbot IA](/blog/chatbot-ia-guia-completo-2025/)** - IA conversacional

**Precisa chatbot WhatsApp profissional?** A Agência Café Online já criou 50+ bots para clientes (economia média R$ 6k/mês vs atendentes). [Consultoria grátis](https://agenciacafeonline.com.br).

---

**Sobre o autor:** Felipe Zanoni desenvolve chatbots WhatsApp há 4 anos, com 80+ bots ativos processando 50k+ mensagens/dia usando Evolution API + IA.
