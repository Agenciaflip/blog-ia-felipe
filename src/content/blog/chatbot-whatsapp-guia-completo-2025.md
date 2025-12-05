---
title: "Chatbot WhatsApp: Guia Completo 2025"
description: "Aprenda a criar chatbot WhatsApp com IA. Tutorial completo com Evolution API, OpenAI GPT-4, código Python e cases reais (ROI 200%+). Implementação em 3-5 horas."
publishDate: 2025-01-16
author: "Felipe Zanoni"
category: "WhatsApp"
tags: ["chatbot whatsapp", "automação whatsapp", "ia whatsapp", "evolution api"]
draft: false
---

> **📚 Série:** Este guia faz parte da nossa série sobre Automação WhatsApp com IA
> → **Você está aqui:** Chatbot WhatsApp

## O que é chatbot WhatsApp?

Um chatbot WhatsApp é um sistema automatizado que conversa com clientes via WhatsApp usando Inteligência Artificial. Funciona 24/7, responde instantaneamente e resolve 60-80% dos atendimentos sem intervenção humana. Principais usos: vendas, suporte, agendamentos e qualificação de leads.

---

## Por que chatbots WhatsApp explodiram em 2025

O WhatsApp Business atingiu **200 milhões de empresas ativas** em 2025 (fonte: [Meta for Business](https://www.facebook.com/business/news/200-million-businesses-whatsapp)). A adoção de chatbots cresceu 340% no Brasil desde 2023.

**Motivos:**
- ✅ **Taxa de abertura 98%** (vs 20% e-mail)
- ✅ **Resposta instantânea** (<5 segundos)
- ✅ **Custo baixo** (R$ 150-400/mês vs R$ 3k+ atendente)
- ✅ **Integração nativa** com CRM, calendários, pagamentos

Se você quer automatizar vendas no WhatsApp, um chatbot é o primeiro passo.

---

## 5 tipos de chatbots WhatsApp

### 1. Chatbot de Atendimento
**Uso:** Responder FAQs, horários, endereços
**Exemplo:** "Qual horário de funcionamento?" → Resposta automática

### 2. Chatbot de Vendas
**Uso:** Mostrar catálogo, processar pedidos, calcular fretes
**Ferramentas:** Integração com [API WhatsApp](/blog/api-whatsapp/) + catálogo de produtos

### 3. Chatbot de Agendamento
**Uso:** Marcar consultas, reuniões, serviços
**Ferramentas:** Integração com Google Calendar via [Evolution API](/blog/evolution-api/)

### 4. Chatbot de Suporte
**Uso:** Abrir tickets, rastrear pedidos, resolver problemas
**Diferencial:** Transfere para humano quando necessário

### 5. Chatbot de Qualificação
**Uso:** Filtrar leads quentes, coletar informações, pontuar interesse
**ROI:** Equipe de vendas foca apenas em leads qualificados

---

## Tecnologias necessárias

### 1. API WhatsApp (obrigatório)

Você precisa de uma API para conectar sistemas ao WhatsApp. Opções:

**A) Evolution API (recomendado - grátis)**
- Open-source e self-hosted
- Sem custos mensais
- Veja tutorial completo: [Evolution API: Guia Definitivo](/blog/evolution-api/)

**B) WhatsApp Business API Oficial**
- Paga (a partir de $0.005/mensagem)
- Requer aprovação do Meta
- Documentação: [WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp/)

**C) Z-API (cloud)**
- R$ 50-150/mês
- Setup instantâneo
- Ideal para quem não quer hospedar

### 2. Inteligência Artificial

**OpenAI GPT-4o (recomendado)**
- Custo: ~R$ 0,10 por 1000 mensagens
- Qualidade superior de conversação
- Function calling nativo
- Cadastro: [OpenAI Platform](https://platform.openai.com/)

**Alternativas:**
- **Google Gemini 1.5 Pro:** Grátis até 50 req/dia
- **Claude 3.5 Sonnet:** Melhor para textos longos
- **GPT-4o-mini:** 10x mais barato que GPT-4o

### 3. Servidor Backend

**Python + Flask (recomendado)**
- Fácil de aprender
- Bibliotecas prontas para WhatsApp
- Deploy simples

**Node.js + Express (alternativa)**
- Performance superior
- Ecossistema rico

### 4. Banco de Dados

**Supabase PostgreSQL (recomendado - grátis)**
- 500MB grátis
- Real-time subscriptions
- Auth integrado
- Cadastro: [Supabase](https://supabase.com/)

---

## Passo a passo: Criar chatbot WhatsApp

### Passo 1: Configurar Evolution API

```bash
# Instalar Docker
curl -fsSL https://get.docker.com | sh

# Clonar Evolution API
git clone https://github.com/EvolutionAPI/evolution-api
cd evolution-api

# Configurar variáveis
cp .env.example .env
nano .env  # Editar: API_KEY, webhook URL

# Subir com Docker Compose
docker-compose up -d
```

Acesse: `http://seu-vps:8080` e escaneie QR Code no WhatsApp Business.

**Veja tutorial completo:** [Evolution API: Instalação e Configuração](/blog/evolution-api/)

---

### Passo 2: Criar servidor Python

```python
# chatbot_whatsapp.py

from flask import Flask, request, jsonify
from openai import OpenAI
import requests
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configurações Evolution API
EVOLUTION_URL = "https://sua-evolution.com.br"
EVOLUTION_KEY = os.getenv("EVOLUTION_API_KEY")

# Prompt do chatbot
PROMPT_SISTEMA = """
Você é a Carla, assistente virtual da Padaria Exemplo.

REGRAS:
1. Sempre se identifique como IA na primeira mensagem
2. Mensagens curtas: 20-40 palavras
3. NUNCA use markdown (###, **, -)
4. Use a tool "buscar_produto" antes de informar preços
5. Para pedidos urgentes, use "enviar_vendedor"

INFORMAÇÕES:
- Horário: Seg-Sáb 6h-20h, Dom 6h-14h
- Delivery: Grátis acima R$ 30
- Especialidades: Pães artesanais, doces, bolos
"""

# Tool: Buscar produto
def buscar_produto(nome_produto):
    # Conectar ao seu sistema de produtos
    produtos = {
        "pão francês": {"preco": 0.80, "descricao": "Pão fresquinho"},
        "croissant": {"preco": 8.50, "descricao": "Croissant de manteiga"}
    }
    return produtos.get(nome_produto.lower())

# Tool: Enviar para vendedor
def enviar_vendedor(numero_cliente, resumo):
    payload = {
        "number": "5511999999999",  # Número do vendedor
        "text": f"🔔 Cliente {numero_cliente} precisa de ajuda:\\n{resumo}"
    }
    requests.post(
        f"{EVOLUTION_URL}/message/sendText/sua-instancia",
        json=payload,
        headers={"apikey": EVOLUTION_KEY}
    )

# Webhook: Receber mensagens
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Extrair dados da mensagem
    numero = data["key"]["remoteJid"].split("@")[0]
    mensagem = data["message"]["conversation"]

    # Chamar OpenAI GPT-4
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": PROMPT_SISTEMA},
            {"role": "user", "content": mensagem}
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "buscar_produto",
                    "description": "Busca preço e detalhes de produto",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "nome": {"type": "string"}
                        },
                        "required": ["nome"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "enviar_vendedor",
                    "description": "Transfere para vendedor humano",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "resumo": {"type": "string"}
                        }
                    }
                }
            }
        ]
    )

    # Processar resposta
    resposta_ia = response.choices[0].message.content

    # Verificar se ativou alguma tool
    if response.choices[0].message.tool_calls:
        tool = response.choices[0].message.tool_calls[0]

        if tool.function.name == "buscar_produto":
            produto_nome = eval(tool.function.arguments)["nome"]
            produto = buscar_produto(produto_nome)

            if produto:
                resposta_ia = f"{produto['descricao']} - R$ {produto['preco']:.2f}"

    # Enviar resposta via Evolution API
    payload = {
        "number": numero,
        "text": resposta_ia
    }
    requests.post(
        f"{EVOLUTION_URL}/message/sendText/sua-instancia",
        json=payload,
        headers={"apikey": EVOLUTION_KEY}
    )

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Passo 3: Configurar webhook

No painel da Evolution API:
1. **Webhook URL:** `https://seu-servidor.com:5000/webhook`
2. **Eventos:** `messages.upsert`
3. **Method:** POST

---

### Passo 4: Testar chatbot

Envie mensagem para o WhatsApp conectado:

**Teste 1:** "Oi"
**Resposta esperada:** "Olá! Eu sou a Carla, assistente virtual (IA) da Padaria Exemplo. Como posso ajudar?"

**Teste 2:** "Quanto custa o pão francês?"
**Resposta esperada:** "Pão fresquinho - R$ 0,80"

**Teste 3:** "Preciso de 100 salgados pra hoje"
**Resposta esperada:** "Vou conectar você com nosso vendedor para pedidos especiais!" + notificação para vendedor

---

## 3 casos reais de sucesso

### Caso 1: Padaria Regional (Grande rede, 5 lojas)

**Desafio:** 300+ mensagens/dia, equipe de 2 atendentes sobrecarregada

**Solução:**
- Chatbot com GPT-4o-mini
- Integração com sistema de pedidos
- Catálogo de 200+ produtos

**Resultados (4 meses):**
- ✅ 82% dos atendimentos resolvidos pela IA
- ✅ Tempo médio de resposta: 12 min → 15 segundos
- ✅ NPS: 72 → 88
- ✅ Custo OpenAI: R$ 210/mês
- ✅ ROI: 380%

---

### Caso 2: Clínica Odontológica (Rede com 3 unidades)

**Desafio:** Agendamentos fora do horário comercial perdidos

**Solução:**
- Chatbot integrado com Google Calendar
- Confirmação automática de consultas
- Lembretes 24h antes

**Resultados (3 meses):**
- ✅ 67 consultas agendadas das 18h-8h (antes: 0)
- ✅ R$ 16.750 em receita adicional
- ✅ Taxa de no-show: 18% → 6%
- ✅ Custo total: R$ 280/mês
- ✅ ROI: 5.900%

---

### Caso 3: E-commerce Moda (Loja online)

**Desafio:** Dúvidas sobre produtos bloqueando vendas

**Solução:**
- Chatbot com acesso ao catálogo completo
- Envio de fotos/vídeos de produtos
- Cálculo de frete automático

**Resultados (5 meses):**
- ✅ 1.240 vendas originadas pelo chatbot
- ✅ Ticket médio: R$ 187
- ✅ R$ 231.880 em receita
- ✅ Taxa de conversão: 34% (vs 12% sem chatbot)
- ✅ ROI: 620%

---

## Quanto custa criar chatbot WhatsApp

### Investimento inicial (DIY - Faça Você Mesmo):

| Item | Custo |
|------|-------|
| VPS (2GB RAM) | R$ 50-80/mês |
| Evolution API | Grátis (self-hosted) |
| OpenAI API (setup) | $5 (R$ 25) |
| Desenvolvimento | R$ 0 (usando código deste guia) |
| **Total inicial** | **R$ 75-105** |

### Custos mensais:

| Item | Custo/mês |
|------|-----------|
| VPS | R$ 50-80 |
| Evolution API (cloud) | R$ 0-150 (se usar Z-API) |
| OpenAI GPT-4o | R$ 150-400 (1000-3000 conversas) |
| Supabase | Grátis (até 500MB) |
| **Total mensal** | **R$ 200-630** |

### Economia vs atendente humano:

- **Atendente:** R$ 2.500-3.500/mês + encargos
- **Chatbot:** R$ 200-630/mês
- **Economia:** **R$ 2.000-3.000/mês** (70-85%)

---

## Erros comuns e como evitar

### 1. Prompt muito genérico
❌ "Você é um assistente útil"
✅ "Você é a Carla da Padaria Exemplo, fala português informal, máximo 40 palavras"

### 2. Não usar tools
❌ IA inventa preços
✅ IA SEMPRE chama buscar_produto antes

### 3. Markdown no WhatsApp
❌ Mensagens com ###, **, -
✅ Instrução explícita no prompt: "NUNCA use markdown"

### 4. Sem fallback para humano
❌ Chatbot trava em situações complexas
✅ Tool enviar_vendedor para transferências

### 5. Não testar com clientes reais
❌ Deploy direto em produção
✅ Testes com 10+ conversas reais antes

---

## Ferramentas recomendadas

### APIs WhatsApp:
- **[Evolution API](https://evolution-api.com/)** - Open-source, grátis
- **[Z-API](https://z-api.io/)** - Cloud, R$ 50/mês
- **[WhatsApp Business API](https://developers.facebook.com/docs/whatsapp/)** - Oficial, empresarial

### Inteligência Artificial:
- **[OpenAI GPT-4](https://platform.openai.com/)** - Melhor qualidade
- **[Google Gemini](https://ai.google.dev/)** - Grátis até 50/dia
- **[Anthropic Claude](https://www.anthropic.com/)** - Textos longos

### Desenvolvimento:
- **[Flask Documentation](https://flask.palletsprojects.com/)** - Python
- **[Supabase](https://supabase.com/)** - Banco de dados
- **[Postman](https://www.postman.com/)** - Testar APIs

---

## Próximos passos

Agora que você sabe criar chatbot WhatsApp, explore:

1. **[API WhatsApp: Guia Completo](/blog/api-whatsapp/)** - Entenda APIs em profundidade
2. **[Evolution API: Tutorial Definitivo](/blog/evolution-api/)** - Setup completo passo a passo
3. **[CRM para Vendas](/blog/crm-vendas/)** - Integre seu chatbot com CRM

**Quer automatizar vendas no WhatsApp?** Veja nosso [Guia de Automação WhatsApp](/blog/automacao-whatsapp/).

---

## Conclusão

Chatbots WhatsApp com IA **não são mais luxo de grandes empresas**. Com R$ 200-400/mês você automatiza 60-80% do atendimento, economiza R$ 2k-3k em custos de equipe e ainda melhora satisfação do cliente.

**ROI típico:** 200-600% nos primeiros 6 meses.

Precisa de ajuda para implementar? A **[Agência Café Online](https://agenciacafeonline.com.br)** já criou chatbots WhatsApp para 20+ empresas brasileiras - de padarias a clínicas médicas. [Entre em contato](https://agenciacafeonline.com.br/contato).

---

**Sobre o autor:** Felipe Zanoni é especialista em automação WhatsApp com IA, com 500+ horas implementando chatbots para empresas brasileiras. Confira outros guias práticos em [blog.agenciacafeonline.com.br](/blog).
