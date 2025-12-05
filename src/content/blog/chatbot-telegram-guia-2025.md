---
title: "Chatbot Telegram: Guia Completo 2025"
description: "Crie chatbot Telegram com IA em 30 minutos. Tutorial passo a passo com Python, BotFather e integração OpenAI. Gratuito e sem limite de mensagens."
publishDate: 2025-02-06
author: "Felipe Zanoni"
category: "IA"
tags: ["chatbot telegram", "telegram bot", "python telegram", "bot ia", "automação telegram"]
draft: false
---

> **📚 Série:** Chatbots Inteligentes
> → [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/) | [Automação Telegram](/blog/automacao-telegram-guia-2025/) | [Chatbot Vendas](/blog/chatbot-vendas-guia-2025/)

## O que é Chatbot Telegram?

Chatbot Telegram é um programa automatizado que conversa com usuários via Telegram Messenger, respondendo perguntas, executando comandos e integrando-se com APIs externas. Funciona via Telegram Bot API (oficial e gratuita) e pode ser criado em 30 minutos com Python. Diferente do WhatsApp, não tem limite de mensagens, não precisa número de telefone e oferece recursos avançados (inline keyboards, webhooks, pagamentos integrados).

Com 800 milhões de usuários ativos mensalmente, Telegram é popular em comunidades tech, cripto, canais de notícias e grupos privados.

---

## Por Que Criar Bot no Telegram (vs WhatsApp)

### Vantagens Telegram

| Critério | Telegram | WhatsApp |
|----------|----------|----------|
| **API oficial grátis** | ✅ Sim, ilimitada | ❌ Não (precisa Z-API, Evolution API) |
| **Limite mensagens** | ✅ Ilimitado | ❌ 1.000/dia (oficial) |
| **Setup** | ✅ 10 minutos | ❌ 1-3 horas (depende da API) |
| **Custo** | ✅ R$ 0 | ❌ R$ 50-300/mês (APIs third-party) |
| **Recursos bot** | ✅ Inline keyboards, pagamentos, grupos | ✅ Básico |
| **Número telefone** | ✅ Não precisa | ❌ Obrigatório |
| **Usuários Brasil** | ⚠️ 50M (~23%) | ✅ 147M (~69%) |

**Quando usar Telegram:**
- Comunidades tech/cripto
- Canais de notícias/alertas
- Bots utilitários (conversão moeda, clima, etc)
- Prototipagem rápida (testar IA antes de migrar WhatsApp)

**Quando usar WhatsApp:**
- Vendas B2C (público geral)
- Atendimento cliente varejo
- Negócios locais (restaurantes, lojas)

---

## Como Criar Bot Telegram em 30 Minutos

### Passo 1: Criar bot no BotFather (5 min)

1. Abra Telegram e busque `@BotFather`
2. Envie comando `/newbot`
3. BotFather pergunta: "Qual nome do bot?"
   - Digite: `Meu Assistente IA`
4. BotFather pergunta: "Qual username?" (deve terminar com 'bot')
   - Digite: `meu_assistente_ia_bot`
5. BotFather retorna:
```
Done! Your bot is ready.
Token: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
Use this token to access HTTP API.
```

**Guarde este token!** É a chave de acesso ao bot.

---

### Passo 2: Instalar biblioteca Python (2 min)

```bash
pip install python-telegram-bot openai
```

---

### Passo 3: Código básico do bot (10 min)

**Arquivo: `bot.py`**

```python
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import openai
import os

# Configurações
TELEGRAM_TOKEN = "SEU_TOKEN_BOTFATHER"
OPENAI_API_KEY = "SUA_KEY_OPENAI"

openai.api_key = OPENAI_API_KEY

# Função: Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Responde quando usuário envia /start"""
    await update.message.reply_text(
        "Olá! Eu sou um assistente com IA. Como posso ajudar?"
    )

# Função: Responder mensagens com ChatGPT
async def responder_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Envia mensagem do usuário para ChatGPT e retorna resposta"""
    mensagem_usuario = update.message.text

    # Chama OpenAI GPT-4o mini
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente útil e amigável."},
            {"role": "user", "content": mensagem_usuario}
        ]
    )

    resposta_ia = response.choices[0].message.content
    await update.message.reply_text(resposta_ia)

# Main
def main():
    """Iniciar bot"""
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Adicionar handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensagem))

    # Rodar bot
    print("Bot rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()
```

---

### Passo 4: Rodar bot (1 min)

```bash
python bot.py
```

**Teste:**
1. Abra Telegram e busque `@meu_assistente_ia_bot`
2. Envie `/start`
3. Bot responde: "Olá! Eu sou um assistente com IA..."
4. Envie qualquer pergunta: "Quanto é 2+2?"
5. Bot responde via ChatGPT

**Custo:** R$ 0,50 a R$ 2,00 para 1.000 conversas (GPT-4o mini via API)

---

### Passo 5: Adicionar comandos customizados (10 min)

```python
# Comando /ajuda
async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = """
Comandos disponíveis:
/start - Iniciar conversa
/ajuda - Ver este menu
/clima [cidade] - Consultar clima
/piada - Ouvir uma piada
"""
    await update.message.reply_text(texto)

# Comando /clima
async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Uso: /clima [cidade]\nExemplo: /clima São Paulo")
        return

    cidade = " ".join(context.args)

    # Integração API clima (exemplo com WeatherAPI)
    import requests
    API_KEY = "sua_key_weatherapi"
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={cidade}&lang=pt"

    response = requests.get(url)
    dados = response.json()

    if "error" in dados:
        await update.message.reply_text(f"Cidade '{cidade}' não encontrada.")
        return

    temp = dados["current"]["temp_c"]
    condicao = dados["current"]["condition"]["text"]

    await update.message.reply_text(
        f"🌤️ Clima em {cidade}:\n{temp}°C - {condicao}"
    )

# Comando /piada
async def piada(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Conte uma piada curta e engraçada"}
        ]
    )
    piada_text = response.choices[0].message.content
    await update.message.reply_text(piada_text)

# Adicionar no main()
app.add_handler(CommandHandler("ajuda", ajuda))
app.add_handler(CommandHandler("clima", clima))
app.add_handler(CommandHandler("piada", piada))
```

---

## Caso Real: Canal Cripto com 12k Membros Usa Bot

**Empresa:** Canal Telegram sobre criptomoedas (12.000 membros, comunidade paga R$ 97/mês)

**Problema:**
- Membros fazem mesmas perguntas 50x/dia ("Como comprar?", "Qual carteira usar?")
- Admin gastava 4-6h/dia respondendo
- Novos membros sem onboarding estruturado

**Solução:**

**Bot Telegram com IA + Base de conhecimento**

```python
# Prompt system do ChatGPT
PROMPT_SISTEMA = """
Você é o assistente oficial do canal CriptoMaster.

Base de conhecimento:
- Carteira recomendada: MetaMask (mobile) ou Ledger (hardware)
- Exchange recomendada: Binance ou Coinbase
- Telegram do suporte: @criptomaster_suporte

Responda dúvidas sobre cripto de forma educativa e técnica.
Se não souber, diga "Consulte @criptomaster_suporte".
"""

# Comando /start personalizado
async def start_cripto(update, context):
    await update.message.reply_text(
        "Bem-vindo ao CriptoMaster! 🚀\n\n"
        "Comandos:\n"
        "/carteira - Como criar carteira\n"
        "/comprar - Como comprar cripto\n"
        "/seguranca - Dicas de segurança\n"
        "/suporte - Falar com admin\n\n"
        "Ou me faça qualquer pergunta sobre cripto!"
    )
```

**Resultados (60 dias):**
- ✅ Mensagens respondidas: 2.100/mês (antes 0 automático)
- ✅ Taxa de resolução bot: 78% (apenas 22% vão para admin)
- ✅ Tempo admin: 4-6h/dia → 1h/dia (83% redução)
- ✅ Satisfação membros: 4.2 → 4.7 (de 5)
- ✅ Custo: R$ 15/mês (API OpenAI)
- ✅ **ROI:** 580% (economizou 5h/dia × R$ 50/h = R$ 250/dia)

**Depoimento admin:** "Bot responde melhor que eu em 80% dos casos, com muito mais paciência. Agora foco em conteúdo exclusivo e análises."

---

## Recursos Avançados Telegram Bots

### 1. Inline Keyboards (Botões)

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def menu(update, context):
    keyboard = [
        [InlineKeyboardButton("Ver produtos", callback_data='produtos')],
        [InlineKeyboardButton("Falar com vendedor", callback_data='vendedor')],
        [InlineKeyboardButton("Rastrear pedido", callback_data='rastreio')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Como posso ajudar?', reply_markup=reply_markup)

# Handler callback buttons
async def button_handler(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'produtos':
        await query.edit_message_text("Aqui estão nossos produtos: [lista]")
    elif query.data == 'vendedor':
        await query.edit_message_text("Transferindo... @vendedor_oficial")
```

---

### 2. Enviar Imagens/Documentos

```python
# Enviar imagem
await update.message.reply_photo(
    photo='https://example.com/produto.jpg',
    caption='Produto X - R$ 99'
)

# Enviar PDF
await update.message.reply_document(
    document=open('catalogo.pdf', 'rb'),
    caption='Nosso catálogo completo'
)

# Enviar vídeo
await update.message.reply_video(
    video=open('tutorial.mp4', 'rb'),
    caption='Tutorial de uso'
)
```

---

### 3. Webhooks (Escalável)

**Por quê:** Polling (método acima) consulta Telegram a cada 1 segundo. Webhooks recebem mensagens instantaneamente.

**Setup webhook (Flask):**

```python
from flask import Flask, request
from telegram import Update
import json

app = Flask(__name__)
TELEGRAM_TOKEN = "seu_token"

@app.route(f'/webhook/{TELEGRAM_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    # Processar update
    return 'ok'

if __name__ == '__main__':
    # Configurar webhook no Telegram
    import requests
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"
    data = {"url": f"https://seu-dominio.com/webhook/{TELEGRAM_TOKEN}"}
    requests.post(url, json=data)

    # Rodar Flask
    app.run(host='0.0.0.0', port=5000)
```

**Vantagens:**
- Respostas instantâneas (vs 1s delay polling)
- Menor uso de recursos (servidor não fica consultando)
- Escalável para milhões de mensagens

---

### 4. Pagamentos Integrados

Telegram permite receber pagamentos DENTRO do bot (Stripe, Mercado Pago).

```python
from telegram import LabeledPrice

async def criar_invoice(update, context):
    """Envia cobrança de R$ 50"""
    await update.message.reply_invoice(
        title="Produto Premium",
        description="Acesso vitalício ao curso",
        payload="produto_123",
        provider_token="SEU_TOKEN_STRIPE",
        currency="BRL",
        prices=[LabeledPrice("Produto Premium", 5000)]  # 5000 centavos = R$ 50
    )
```

Usuário clica, paga com cartão e bot recebe confirmação automaticamente.

---

## Bibliotecas e Frameworks Úteis

### 1. python-telegram-bot (Recomendado)

**Site:** [python-telegram-bot.org](https://python-telegram-bot.org/)

**Prós:**
- Mais popular (15k+ stars GitHub)
- Bem documentado
- Suporta async/await (moderno)

**Instalação:**
```bash
pip install python-telegram-bot
```

---

### 2. Telebot (Alternativa simples)

**Site:** [github.com/eternnoir/pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

**Prós:**
- Sintaxe mais simples
- Bom para iniciantes

**Instalação:**
```bash
pip install pyTelegramBotAPI
```

**Exemplo:**
```python
import telebot

bot = telebot.TeleBot("SEU_TOKEN")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Olá!")

@bot.message_handler(func=lambda m: True)
def responder(message):
    bot.reply_to(message, f"Você disse: {message.text}")

bot.polling()
```

---

### 3. Aiogram (Para bots complexos)

**Site:** [aiogram.dev](https://aiogram.dev/)

**Prós:**
- Performance superior (async nativo)
- Middleware avançado
- FSM (Finite State Machine) integrado

**Ideal para:** Bots com fluxos complexos (tipo chatbot e-commerce multi-step)

---

## Deploy do Bot (Rodar 24/7)

### Opção 1: VPS (DigitalOcean, Hostinger)

```bash
# Instalar dependências
sudo apt update
sudo apt install python3-pip
pip3 install python-telegram-bot openai

# Criar arquivo bot.py
nano bot.py
[colar código]

# Rodar em background
nohup python3 bot.py &

# Verificar se está rodando
ps aux | grep bot.py
```

**Custo:** R$ 25-50/mês (VPS básico)

---

### Opção 2: Heroku (Grátis com limitações)

```bash
# Criar Procfile
echo "web: python bot.py" > Procfile

# Criar requirements.txt
pip freeze > requirements.txt

# Deploy
git init
heroku create nome-do-bot
git add .
git commit -m "Bot Telegram"
git push heroku master
```

**Limitação:** Heroku free tier dorme após 30 min inatividade.

---

### Opção 3: Webhook + Vercel (Serverless)

```python
# api/webhook.py (Vercel Serverless)
from telegram import Update, Bot
from telegram.ext import Dispatcher
import json

bot = Bot(token="SEU_TOKEN")
dispatcher = Dispatcher(bot, None, use_context=True)

# Adicionar handlers
dispatcher.add_handler(CommandHandler("start", start))

def webhook(request):
    update = Update.de_json(json.loads(request.body), bot)
    dispatcher.process_update(update)
    return {'statusCode': 200}
```

**Custo:** R$ 0 (100k invocações grátis/mês)

---

## Próximos passos

1. **[Automação Telegram](/blog/automacao-telegram-guia-2025/)** - Casos de uso avançados
2. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Alternativa para Brasil
3. **[API OpenAI Python](/blog/api-openai-python-2025/)** - Integração ChatGPT
4. **[Automação Python](/blog/automacao-python-guia-2025/)** - Scripts utilitários
5. **[Chatbot Vendas](/blog/chatbot-vendas-guia-2025/)** - Monetização

---

**Sobre o autor:** Felipe Zanoni é especialista em bots Telegram e automação conversacional, com 100+ bots criados para comunidades brasileiras. Fundador da Agência Café Online.
