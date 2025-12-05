---
title: "Como Criar Chatbot WhatsApp: Guia 2025"
description: "Crie chatbot WhatsApp grátis: ManyChat, Typebot, Evolution API + ChatGPT. Tutorial passo a passo sem programar, 24/7 atendimento (510 buscas/mês)."
publishDate: 2025-01-26
author: "Felipe Zanoni"
category: "WhatsApp"
tags: ["como criar chatbot whatsapp", "chatbot whatsapp gratis", "manychat tutorial", "typebot whatsapp", "chatbot sem programar"]
draft: false
---

> **📚 Série:** Automação WhatsApp
> → [Chatbot WhatsApp IA](/blog/chatbot-whatsapp-guia-completo-2025/) | [WhatsApp Business](/blog/whatsapp-business-automacao-2025/) | [WhatsApp Bot Python](/blog/whatsapp-bot-python-guia-2025/) | [Evolution API](/blog/evolution-api-tutorial-completo/)

## O que é Chatbot WhatsApp?

Chatbot WhatsApp é robô conversacional que atende clientes 24/7 via WhatsApp Business API, responde perguntas frequentes (FAQ), qualifica leads, agenda consultas, envia catálogo produtos e transfere para humano quando necessário sem programar. Plataformas no-code (ManyChat, Typebot, Landbot) permitem criar chatbot drag-and-drop em 30 minutos vs 40h desenvolvimento custom. Empresas reportam 80% automação atendimento, 350%+ aumento conversão leads e economia R$ 15k/mês vs contratar 3 atendentes.

Diferença: Chatbot básico (respostas fixas "se X então Y") vs chatbot IA (ChatGPT entende contexto, linguagem natural).

---

## 5 Formas Criar Chatbot WhatsApp (Comparação)

| Método | Custo | Dificuldade | Tempo Setup | IA Integrada | Ideal Para |
|--------|-------|-------------|-------------|--------------|------------|
| **ManyChat** | $15-145/mês | ⭐ Fácil | 30 min | ✅ Sim | Pequenas empresas |
| **Typebot** | $0-39/mês | ⭐⭐ Média | 1h | ✅ Sim | Médias empresas |
| **Landbot** | $40-400/mês | ⭐ Fácil | 30 min | ⚠️ Limitada | Marketing |
| **Evolution + N8N** | $0 (self-host) | ⭐⭐⭐⭐ Difícil | 4h | ✅ ChatGPT full | Desenvolvedores |
| **Python Custom** | $0-50/mês | ⭐⭐⭐⭐⭐ Muito difícil | 8-40h | ✅ Ilimitada | Empresas grandes |

**Recomendação:**
- **Iniciante sem tech:** ManyChat (mais fácil)
- **Budget baixo:** Typebot (open-source)
- **Flexibilidade máxima:** Evolution API + N8N
- **Custom complexo:** Python (controle total)

---

## Método 1: Criar Chatbot com ManyChat (Mais Fácil)

### Passo 1: Criar Conta ManyChat

1. **Acesse:** https://manychat.com
2. **Criar conta** (grátis 1k contatos)
3. **Conectar WhatsApp:**
   - Settings → WhatsApp
   - Escolher provedor: **360Dialog** (recomendado)
   - Inserir API key 360Dialog

### Passo 2: Criar Fluxo Conversacional

**Exemplo: FAQ Loja Online**

**1. Criar Automation:**
- Automations → New Automation
- Trigger: **User sends message**
- Keyword: (qualquer mensagem)

**2. Adicionar blocos (drag-and-drop):**

```
[Trigger: Mensagem recebida]
   ↓
[Text Block]
"Olá! Sou assistente virtual 😊
Como posso ajudar?"

[Button Block]
1️⃣ Ver produtos
2️⃣ Status pedido
3️⃣ Falar com humano
   ↓ (se clicou 1)
[Show Products]
[Carousel com 5 produtos]
   ↓ (se clicou 2)
[User Input: Número pedido]
   ↓
[API Call: Buscar pedido sistema]
   ↓
[Text: Status pedido]
   ↓ (se clicou 3)
[Notify Team + Transfer to Agent]
```

**3. Configurar integrações:**
- ManyChat → Settings → Integrations
- Conectar: Shopify, WooCommerce, Google Sheets, Zapier

**Custo:**
- Free: 1k contatos
- Pro: $15/mês (até 500 contatos)
- Premium: $145/mês (até 25k contatos)

**Prós:**
- ✅ Setup 30 minutos
- ✅ Interface visual (sem código)
- ✅ Templates prontos (50+)
- ✅ Integrações nativas (Shopify, Stripe, Google Sheets)

**Contras:**
- ❌ Custo escala rápido (>1k contatos)
- ❌ Customização limitada
- ❌ Preso à plataforma (vendor lock-in)

---

## Método 2: Criar Chatbot com Typebot (Open-Source)

### Passo 1: Setup Typebot

**Opção A: Typebot Cloud (pago)**
```
1. Acesse: https://typebot.io
2. Criar conta
3. Plano: $0 (200 chats/mês) ou $39/mês (2k chats)
```

**Opção B: Self-hosted (grátis)**
```bash
# Docker Compose
git clone https://github.com/baptisteArno/typebot.io
cd typebot.io
docker-compose up -d

# Acessar: http://localhost:3000
```

### Passo 2: Criar Bot

**1. Novo Typebot:**
- Dashboard → Create Typebot
- Template: FAQ/Lead Qualification/E-commerce

**2. Adicionar blocos:**

```
[Start]
   ↓
[Text Bubble]
"Olá {{displayName}}! Como posso ajudar? 😊"
   ↓
[Buttons]
- Ver produtos 🛍️
- Suporte técnico 🔧
- Falar com vendedor 💬
   ↓ (se Ver produtos)
[Text Input: "O que você procura?"]
   ↓
[OpenAI Block]
Model: gpt-4o-mini
Prompt: "Recomende 3 produtos baseado em: {{answer}}"
   ↓
[Text: Exibir recomendações IA]
   ↓
[Button: "Quero comprar"]
   ↓
[Webhook: Criar pedido sistema]
```

**3. Integrar WhatsApp:**
```
Settings → Integrations → WhatsApp
   ↓
Escolher provedor:
- Evolution API (grátis, self-hosted)
- 360Dialog (oficial, pago)
- Twilio (oficial, pago)
   ↓
Inserir credenciais API
   ↓
Copiar webhook URL Typebot
   ↓
Configurar webhook no provedor WhatsApp
```

**Prós:**
- ✅ Open-source (self-host grátis)
- ✅ ChatGPT nativo (OpenAI block)
- ✅ Lógica condicional avançada
- ✅ Webhooks ilimitados
- ✅ White-label (sua marca)

**Contras:**
- ⚠️ Precisa VPS (self-host)
- ⚠️ Curva aprendizado média

---

## Método 3: Criar Chatbot com Evolution API + ChatGPT (Gratuito)

### Setup Completo

**Passo 1: Instalar Evolution API**

```bash
# VPS Ubuntu
docker run -d \
  --name evolution-api \
  -p 8080:8080 \
  -e AUTHENTICATION_API_KEY=sua-chave-secreta \
  atendai/evolution-api:latest

# Acessar: http://IP:8080
```

**Passo 2: Criar Instância WhatsApp**

```bash
curl -X POST 'http://IP:8080/instance/create' \
-H 'apikey: sua-chave-secreta' \
-H 'Content-Type: application/json' \
-d '{
  "instanceName": "chatbot-loja",
  "qrcode": true
}'

# Escanear QR Code WhatsApp
```

**Passo 3: Código Chatbot (Node.js exemplo)**

```javascript
const express = require('express');
const axios = require('axios');
const OpenAI = require('openai');

const app = express();
app.use(express.json());

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const EVOLUTION_URL = 'http://localhost:8080';
const API_KEY = 'sua-chave-secreta';
const INSTANCE = 'chatbot-loja';

// Webhook recebe mensagens
app.post('/webhook/whatsapp', async (req, res) => {
  const data = req.body;

  // Ignorar mensagens próprias
  if (data.data?.key?.fromMe) return res.send('ok');

  const from = data.data?.key?.remoteJid;
  const message = data.data?.message?.conversation || '';

  if (!from || !message) return res.send('ok');

  console.log(`Mensagem de ${from}: ${message}`);

  // ChatGPT responde
  const resposta = await gerarResposta(message);

  // Enviar WhatsApp
  await enviarMensagem(from, resposta);

  res.send('ok');
});

async function gerarResposta(mensagem) {
  const completion = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [
      {
        role: 'system',
        content: `
Você é chatbot WhatsApp da TechStore.

Informações:
- Vendemos notebooks, celulares, acessórios
- Horário: Seg-Sex 8h-18h
- Entrega: Todo Brasil (5-10 dias)

Regras:
1. Seja breve (2-3 frases)
2. Use emojis 😊
3. Sempre pergunte se resolveu
4. Se cliente quer comprar, diga "vou chamar vendedor!"
        `
      },
      { role: 'user', content: mensagem }
    ],
    temperature: 0.7,
    max_tokens: 150
  });

  return completion.choices[0].message.content;
}

async function enviarMensagem(numero, texto) {
  await axios.post(
    `${EVOLUTION_URL}/message/sendText/${INSTANCE}`,
    {
      number: numero,
      textMessage: { text: texto }
    },
    {
      headers: { apikey: API_KEY }
    }
  );
}

app.listen(3000, () => console.log('Chatbot rodando porta 3000'));
```

**Passo 4: Configurar Webhook**

```bash
curl -X POST 'http://IP:8080/webhook/set/chatbot-loja' \
-H 'apikey: sua-chave-secreta' \
-H 'Content-Type: application/json' \
-d '{
  "url": "https://seu-dominio.com/webhook/whatsapp",
  "events": ["messages.upsert"]
}'
```

**Resultado:** Chatbot 100% funcional com IA conversacional!

**Custo total:**
- Evolution API: $0 (self-host)
- VPS: $5-20/mês (DigitalOcean/Hostinger)
- ChatGPT API: $10-50/mês (uso)
- **Total: $15-70/mês**

---

## 10 Templates Chatbot Prontos (Copiar/Colar)

### 1. FAQ Básico (Respostas Fixas)

```
[Mensagem recebida]
   ↓
SE contém "horário" OU "funciona"
   → "Funcionamos Seg-Sex 8h-18h, Sáb 9h-13h 😊"

SE contém "entrega" OU "delivery"
   → "Entregamos todo Brasil! Prazo 5-10 dias úteis 📦"

SE contém "pagamento" OU "forma"
   → "Aceitamos: PIX, cartão, boleto 💳"

SENÃO
   → "Não entendi 😅 Pode reformular?"
```

### 2. Qualificação Lead Imobiliária

```
"Olá! Procura imóvel? 🏠"
[Botões: Sim / Não]
   ↓ Sim
"Qual região?"
[Input texto]
   ↓
"Quantos quartos?"
[Botões: 1 / 2 / 3 / 4+]
   ↓
"Orçamento disponível?"
[Input texto]
   ↓
[Se orçamento > R$ 200k]
   → "Perfeito! Temos 8 opções. Vou chamar corretor! 🎉"
   → [Notificar vendedor]

[Se orçamento < R$ 200k]
   → "Legal! Enviei catálogo por email 📧"
   → [Follow-up automático D+3]
```

### 3. Agendamento Consulta Clínica

```
"Oi! Quer agendar consulta? 👨‍⚕️"
[Botões: Sim / Não]
   ↓ Sim
"Qual especialidade?"
[Botões: Clínico Geral / Dermatologista / Pediatra]
   ↓ (escolheu Dermatologista)
"Horários disponíveis terça:"
[Botões: 10h / 14h / 16h]
   ↓ (escolheu 14h)
"✅ Agendado! Terça 14h com Dra. Maria
📍 Rua X, 123
⏰ Lembrete: Envio 24h antes"
   ↓
[Criar evento Google Calendar]
[Enviar lembrete D-1]
```

### 4. Carrinho Abandonado E-commerce

```
[Trigger: Shopify webhook - carrinho abandonado]
   ↓ Delay 2h
"Oi {{nome}}! Notei que deixou itens no carrinho 🛒

{{produto_1}}
{{produto_2}}

Ainda disponíveis! Finalize: {{link}}
Cupom 10% OFF: VOLTA10 (válido 24h)"
   ↓ Delay 24h (se não comprou)
"Últimas {{quantidade}} unidades! 😱
Não perca: {{link}}"
```

### 5. Pesquisa Satisfação NPS

```
[Trigger: Pedido entregue]
   ↓ Delay 2 dias
"Oi {{nome}}! Como foi sua experiência? 😊"
[Botões: 😀 Ótima / 😐 Boa / 😞 Ruim]
   ↓ (se Ótima/Boa)
"Que bom! Deixe review: {{link_google}}"
   ↓ (se Ruim)
"Lamento 😔 O que aconteceu?"
[Input texto]
   ↓
[Criar ticket suporte]
[Notificar gerente]
"Equipe responde em 1h! Obrigado feedback."
```

### 6. Cobrança Boleto Vencido

```
[Trigger: Boleto venceu]
   ↓ D+1 (8h manhã)
"Bom dia {{nome}}!
Boleto venceu ontem: R$ {{valor}}
Nova via (sem juros hoje): {{link}} 💳"
   ↓ D+3 (se não pagou)
"Pagamento pendente há 3 dias 😔
Juros: R$ {{juros}}
Regularize: {{link}}"
   ↓ D+7
"Última cobrança. Após hoje: restrição crédito.
Pagar: {{link}}"
```

### 7. Onboarding Novo Cliente SaaS

```
[Trigger: Novo cadastro]
   ↓ Imediato
"🎉 Bem-vindo {{nome}}!
Login: {{link}}
Senha: Enviamos por email

Já logou? SIM/NÃO"
   ↓ D+1
"Dica Dia 1: Como criar primeiro projeto
Vídeo (3 min): {{link_tutorial}}"
   ↓ D+3
"Conseguiu criar projeto? SIM/NÃO"
   ↓ (se NÃO)
"Deixa eu ajudar! Quer call rápida?
Agendar: {{link_calendly}}"
```

### 8. Menu Restaurante (Pedido Completo)

```
"Olá! Cardápio: {{link_pdf}} 😊
Pronto pra pedir?"
[Botões: Sim / Ver promoções]
   ↓ Sim
"Escolha categoria:"
[Botões: 🍔 Hambúrguer / 🍕 Pizza / 🍹 Bebidas]
   ↓ (escolheu Hambúrguer)
[Carrossel 5 hambúrgueres com foto+preço]
"Escolha número:"
   ↓ (digitou 2)
"✅ X-Bacon R$ 28 adicionado!
Mais alguma coisa? SIM/NÃO"
   ↓ (NÃO)
"Total: R$ 28. Endereço entrega?"
[Input texto]
   ↓
"Taxa: R$ 5. Chega em 40 min.
Pagamento na entrega: PIX/Dinheiro/Cartão?"
   ↓
"✅ Pedido confirmado #{{numero}}!
Acompanhe: {{link_rastreio}}"
```

### 9. Lead Magnet (Ebook Gratuito)

```
"Quer nosso ebook GRATUITO? 📚
'10 Estratégias Marketing Digital 2025'"
[Botões: Sim / Não]
   ↓ Sim
"Seu melhor email?"
[Input texto]
   ↓
"✅ Enviado para {{email}}!
Chegou? SIM/NÃO"
   ↓ D+2
"Leu o ebook? Dúvidas? Responda aqui! 😊"
   ↓ D+7
"Quer ajuda implementar estratégias?
Consultoria grátis: {{link_calendly}}"
```

### 10. Suporte Técnico (Triagem)

```
"Olá! Qual problema? 🔧"
[Botões: Login / Pagamento / Bug / Outro]
   ↓ (escolheu Login)
"Não consegue logar?"
[Botões: Esqueci senha / Conta bloqueada / Email não chega]
   ↓ (Esqueci senha)
"Resetar senha: {{link_reset}}
Chegou email? SIM/NÃO"
   ↓ (NÃO)
"Vou criar ticket urgente!
Suporte responde em 10 min. Aguarda? 😊"
[Criar ticket Zendesk]
[Notificar atendente]
```

---

## Casos Reais ROI

### Caso 1: Clínica Odontológica - 300% mais agendamentos

**Antes:** Secretária atendia telefone (8h-18h)
- Agendamentos: 10/dia
- Fora horário: 0 (perdidos)

**Depois:** Chatbot WhatsApp 24/7
- Agendamentos: 40/dia (+300%)
- Taxa no-show: 35% → 5% (lembrete automático)
- Economia: R$ 8k/mês (não contratou 2ª secretária)

**Custo chatbot:** R$ 150/mês (ManyChat + 360Dialog)

### Caso 2: E-commerce Moda - Recuperação carrinho 18%

**Chatbot:**
```
Carrinho abandonado → Delay 2h → WhatsApp:
"Esqueceu algo? 10% OFF válido 24h"
```

**Resultado:**
- 1.200 carrinhos/mês × 18% recuperação = 216 vendas
- Ticket médio: R$ 150
- Receita extra: R$ 32k/mês
- Custo: R$ 300/mês (automação)
- **ROI: 10.566%**

### Caso 3: Imobiliária - 5x mais visitas agendadas

**Chatbot qualificação:**
```
Lead site → WhatsApp imediato → Qualifica:
Orçamento? Região? Prazo?
→ Score 80+: Agenda visita automaticamente (Google Calendar)
```

**Resultado:**
- Leads atendidos: 35/mês → 180/mês (+414%)
- Visitas agendadas: 8/mês → 42/mês (+425%)
- Vendas: 2/mês → 9/mês (+350%)

---

## Próximos passos

1. **[Chatbot WhatsApp IA](/blog/chatbot-whatsapp-guia-completo-2025/)** - Guia completo IA
2. **[Evolution API](/blog/evolution-api-tutorial-completo/)** - API WhatsApp oficial
3. **[WhatsApp Bot Python](/blog/whatsapp-bot-python-guia-2025/)** - Desenvolvimento custom
4. **[N8N WhatsApp](/blog/n8n-whatsapp-tutorial-2025/)** - Workflows automação
5. **[Automação WhatsApp](/blog/automacao-whatsapp-2025/)** - Estratégias avançadas
6. **[ChatGPT Marketing](/blog/chatgpt-marketing-guia-2025/)** - IA conversacional
7. **[CRM Vendas](/blog/crm-vendas-guia-completo-2025/)** - Integrar chatbot + CRM

**Precisa chatbot WhatsApp personalizado?** A Agência Café Online já criou 60+ chatbots (ROI médio 500%). [Consultoria grátis](https://agenciacafeonline.com.br).

---

**Sobre o autor:** Felipe Zanoni criou chatbots WhatsApp para empresas processando 500k+ conversas/mês com 85% automação e NPS 82+.
