---
title: "API OpenAI Python: Guia Completo 2025"
description: "OpenAI API Python: GPT-4, GPT-4o, function calling, embeddings e fine-tuning. Tutorial completo com código, custos e casos reais. Implementação em 30 minutos."
publishDate: 2025-01-27
author: "Felipe Zanoni"
category: "IA"
tags: ["api openai", "gpt-4 api", "python openai", "chatgpt api"]
draft: false
---

> **📚 Série:** IA & Desenvolvimento
> → [Chatbot IA](/blog/chatbot-ia-2025/) | [GPT-4 API](/blog/gpt-4-api-2025/) | [Flask Python](/blog/flask-python-tutorial-2025/)

## O que é API OpenAI?

API OpenAI permite integrar modelos de IA (GPT-4, GPT-4o, DALL-E, Whisper) em aplicações via código Python/JavaScript. Usada por 2M+ desenvolvedores para criar [chatbots](/blog/chatbot-whatsapp-guia-completo-2025/), assistentes, automações e análise de dados. Custo: $0.15-$60 por 1M tokens conforme modelo. GPT-4o-mini (mais barato) = $0.15/1M tokens.

**Site oficial:** [platform.openai.com](https://platform.openai.com/)

---

## Modelos disponíveis (2025)

### GPT-4o (Recomendado)

**Custo:** $2.50/1M tokens input | $10/1M tokens output
**Velocidade:** ✅ Rápida
**Qualidade:** ✅ Excelente
**Uso:** Produção geral

### GPT-4o-mini (Mais barato)

**Custo:** $0.15/1M tokens input | $0.60/1M tokens output
**Velocidade:** ✅ Muito rápida
**Qualidade:** ⚠️ Boa
**Uso:** [Chatbots](/blog/chatbot-gratuito-2025/), tarefas simples

### GPT-4 Turbo

**Custo:** $10/1M tokens input | $30/1M tokens output
**Qualidade:** ✅ Máxima
**Uso:** Tarefas complexas

### Comparação:

| Modelo | Input | Output | Contexto | Velocidade | Uso |
|--------|-------|--------|----------|------------|-----|
| **GPT-4o** | $2.50 | $10 | 128k | ✅ Rápida | **Produção** |
| **GPT-4o-mini** | $0.15 | $0.60 | 128k | ✅ Muito rápida | **Chatbots** |
| **GPT-4 Turbo** | $10 | $30 | 128k | ⚠️ Lenta | Complexo |

**Recomendação:** GPT-4o-mini para 90% dos casos

---

## Instalação e setup

```bash
# Instalar biblioteca
pip install openai

# Verificar versão
pip show openai
# Version: 1.12.0
```

### Obter API Key:

1. Acesse: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Criar conta (precisa cartão)
3. Adicionar créditos ($5 mínimo)
4. Gerar API key
5. Copiar (começa com `sk-proj-...`)

**⚠️ Importante:** Adicionar créditos antes de usar (sem tier grátis em 2025)

---

## Hello World (primeira chamada)

```python
from openai import OpenAI

client = OpenAI(api_key="sk-proj-...")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Olá! Quem é você?"}
    ]
)

print(response.choices[0].message.content)
# "Olá! Sou um assistente de IA criado pela OpenAI..."
```

**Custo:** ~100 tokens = $0.000025 (R$ 0.0001)

---

## Chat completo (conversação)

```python
from openai import OpenAI

client = OpenAI(api_key="sk-proj-...")

# Histórico de conversação
messages = [
    {"role": "system", "content": "Você é um assistente útil e conciso."}
]

while True:
    # Input usuário
    user_input = input("Você: ")

    if user_input.lower() in ['sair', 'exit']:
        break

    # Adicionar mensagem do usuário
    messages.append({"role": "user", "content": user_input})

    # Chamar API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=150,
        temperature=0.7
    )

    # Resposta do assistente
    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})

    print(f"Assistente: {assistant_message}")
```

**Parâmetros:**
- `max_tokens`: Limite de resposta (150 = ~100 palavras)
- `temperature`: Criatividade (0 = determinístico, 1 = criativo)

---

## Function calling (ferramentas)

**Caso de uso:** [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/) que busca produtos

```python
from openai import OpenAI
import json

client = OpenAI(api_key="sk-proj-...")

# Definir funções disponíveis
tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Busca produto no banco de dados pelo nome",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome do produto"
                    }
                },
                "required": ["nome"]
            }
        }
    }
]

# Função Python real
def buscar_produto(nome):
    produtos = {
        "notebook": {"preco": 3500, "estoque": 10},
        "mouse": {"preco": 50, "estoque": 100}
    }
    return produtos.get(nome.lower(), {"erro": "Produto não encontrado"})

# Chamada com function calling
messages = [
    {"role": "user", "content": "Quanto custa um notebook?"}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# Verificar se ativou função
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]

    # Extrair argumentos
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)

    # Executar função
    if function_name == "buscar_produto":
        resultado = buscar_produto(function_args["nome"])

        # Enviar resultado de volta pra API
        messages.append(response.choices[0].message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(resultado)
        })

        # Segunda chamada com resultado
        final_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        print(final_response.choices[0].message.content)
        # "O notebook custa R$ 3.500 e temos 10 unidades em estoque."
```

---

## Streaming (respostas em tempo real)

```python
from openai import OpenAI

client = OpenAI(api_key="sk-proj-...")

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Conte uma história"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

**Benefício:** UX melhor (mostra texto conforme gera)

---

## Integração [Flask](/blog/flask-python-tutorial-2025/) (API REST)

```python
from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensagem = data.get('message')

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": mensagem}],
        max_tokens=200
    )

    resposta = response.choices[0].message.content

    return jsonify({
        'response': resposta,
        'tokens_used': response.usage.total_tokens
    })

if __name__ == '__main__':
    app.run(port=5000)
```

**Testar:**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Olá!"}'
```

**Tutorial completo:** [Flask Python](/blog/flask-python-tutorial-2025/)

---

## Embeddings (similaridade de textos)

```python
from openai import OpenAI
import numpy as np

client = OpenAI(api_key="sk-proj-...")

def get_embedding(text):
    """Gera embedding de texto"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Textos para comparar
texto1 = "Como funciona inteligência artificial?"
texto2 = "O que é IA?"
texto3 = "Receita de bolo de chocolate"

# Gerar embeddings
emb1 = np.array(get_embedding(texto1))
emb2 = np.array(get_embedding(texto2))
emb3 = np.array(get_embedding(texto3))

# Calcular similaridade (cosine similarity)
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(f"Similaridade 1-2: {cosine_similarity(emb1, emb2):.2f}")
# 0.92 (muito similar)

print(f"Similaridade 1-3: {cosine_similarity(emb1, emb3):.2f}")
# 0.15 (diferente)
```

**Custo:** $0.02/1M tokens (muito barato)

**Uso:** Busca semântica, recomendações, classificação

---

## Casos reais

### Caso 1: Startup automatizou atendimento

**Empresa:** SaaS B2B

**Stack:**
- [Evolution API](/blog/evolution-api-tutorial-completo/) (WhatsApp)
- GPT-4o-mini ($0.15/1M tokens)
- [Flask](/blog/flask-python-tutorial-2025/) webhook

**Volume:** 3.000 conversas/mês

**Custo:**
- Tokens: 1.5M input + 500k output = $0.52/mês
- VPS: R$ 30/mês
- **Total:** R$ 32.60/mês

**vs Humano:** 1 atendente = R$ 2.500/mês
**Economia:** R$ 2.467/mês (98%)

### Caso 2: E-commerce criou busca inteligente

**Solução:**
- Embeddings de 10.000 produtos
- Busca semântica (não precisa palavra exata)

**Exemplo:**
```
Cliente busca: "roupa pra frio"
Sistema encontra: casacos, blusas, jaquetas
(mesmo sem palavra "frio" no nome)
```

**Custo embeddings:** $0.20 (one-time)
**Resultado:** +35% conversão vs busca tradicional

---

## Custos reais (calculadora)

### Exemplo: Chatbot 1.000 conversas/mês

**Premissas:**
- 1 conversa = 500 tokens input + 200 tokens output
- Total: 500k input + 200k output

**GPT-4o-mini:**
- Input: 500k × $0.15/1M = $0.075
- Output: 200k × $0.60/1M = $0.120
- **Total:** $0.195/mês (R$ 0.98)

**GPT-4o:**
- Input: 500k × $2.50/1M = $1.25
- Output: 200k × $10/1M = $2.00
- **Total:** $3.25/mês (R$ 16.25)

**Diferença:** 16x mais caro (GPT-4o vs GPT-4o-mini)

---

## Dicas para reduzir custos

### 1. Usar GPT-4o-mini

**Economia:** 93% vs GPT-4 Turbo

### 2. Limitar max_tokens

```python
# Ruim: 1.000 tokens/resposta
max_tokens=1000

# Bom: 150 tokens (suficiente)
max_tokens=150
```

**Economia:** 85%

### 3. Cache de respostas

```python
import hashlib

cache = {}

def get_cached_response(mensagem):
    key = hashlib.md5(mensagem.encode()).hexdigest()

    if key in cache:
        return cache[key]

    response = client.chat.completions.create(...)
    cache[key] = response.choices[0].message.content

    return cache[key]
```

**Economia:** 50-70% em perguntas repetidas

### 4. Usar system prompt eficiente

```python
# Ruim: prompt longo (500 tokens)
system_prompt = "Você é um assistente... [500 palavras]"

# Bom: prompt curto (50 tokens)
system_prompt = "Assistente conciso. Respostas max 2 linhas."
```

---

## Error handling

```python
from openai import OpenAI, OpenAIError, RateLimitError, APIError
import time

client = OpenAI(api_key="sk-proj-...")

def call_gpt_with_retry(messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                timeout=30
            )
            return response.choices[0].message.content

        except RateLimitError:
            print(f"Rate limit. Retry {attempt+1}/{max_retries}")
            time.sleep(2 ** attempt)  # Exponential backoff

        except APIError as e:
            print(f"API error: {e}")
            if attempt == max_retries - 1:
                raise

        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    return "Erro: Não foi possível gerar resposta"
```

---

## Boas práticas

### ✅ FAÇA:

1. **Usar variáveis de ambiente**
```python
import os
api_key = os.getenv('OPENAI_API_KEY')
```

2. **Validar input**
```python
if len(mensagem) > 1000:
    return "Mensagem muito longa"
```

3. **Monitorar custos**
```python
print(f"Tokens usados: {response.usage.total_tokens}")
```

4. **Timeout em chamadas**
```python
response = client.chat.completions.create(..., timeout=30)
```

### ❌ NÃO FAÇA:

1. ❌ Hardcode API key no código
2. ❌ Expor API key no frontend
3. ❌ Sem limite de tokens (custo infinito)
4. ❌ Sem error handling

---

## Documentação

- [OpenAI Docs](https://platform.openai.com/docs)
- [Python SDK](https://github.com/openai/openai-python)
- [API Reference](https://platform.openai.com/docs/api-reference)
- [Pricing](https://openai.com/api/pricing/)

---

## Próximos passos

1. **[GPT-4 API](/blog/gpt-4-api-2025/)** - Guia avançado
2. **[Chatbot IA](/blog/chatbot-ia-2025/)** - Criar chatbot
3. **[Flask Python](/blog/flask-python-tutorial-2025/)** - API REST
4. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Integração

---

**Sobre o autor:** Felipe Zanoni é desenvolvedor especializado em OpenAI API, com 200+ integrações para empresas brasileiras.
