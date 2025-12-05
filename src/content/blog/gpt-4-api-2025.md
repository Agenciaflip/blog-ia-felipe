---
title: "GPT-4 API: Guia Completo 2025"
description: "GPT-4 API: tutorial Python, function calling, streaming e fine-tuning. Comparação GPT-4o vs GPT-4 Turbo. Custos, limites e código completo."
publishDate: 2025-01-30
author: "Felipe Zanoni"
category: "IA"
tags: ["gpt-4 api", "gpt-4o", "openai api", "chatgpt api"]
draft: false
---

> **📚 Série:** OpenAI & IA
> → [API OpenAI](/blog/api-openai-python-2025/) | [Chatbot IA](/blog/chatbot-ia-2025/) | [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)

## O que é GPT-4 API?

GPT-4 API é interface de programação que permite integrar o modelo GPT-4 da OpenAI em aplicações via Python/JavaScript. GPT-4 é o modelo de IA mais avançado (2025), com raciocínio superior, menos alucinações e melhor seguimento de instruções vs GPT-3.5. Usado em produção por Duolingo, Khan Academy e Stripe. Custo: $2.50-$60/1M tokens conforme versão (GPT-4o, GPT-4 Turbo, GPT-4).

**Site oficial:** [platform.openai.com](https://platform.openai.com/)

---

## GPT-4o vs GPT-4 Turbo vs GPT-4

### Comparação (Janeiro 2025):

| Modelo | Input | Output | Contexto | Velocidade | Lançamento |
|--------|-------|--------|----------|------------|------------|
| **GPT-4o** | $2.50 | $10 | 128k | ✅ Rápida | Mai/2024 |
| **GPT-4o-mini** | $0.15 | $0.60 | 128k | ✅ Muito rápida | Jul/2024 |
| **GPT-4 Turbo** | $10 | $30 | 128k | ⚠️ Média | Nov/2023 |
| **GPT-4** | $30 | $60 | 8k | ❌ Lenta | Mar/2023 |

**Recomendação 2025:** 🏆 **GPT-4o** (melhor custo-benefício)

**Quando usar cada:**
- **GPT-4o-mini:** [Chatbots](/blog/chatbot-gratuito-2025/), tarefas simples (93% mais barato)
- **GPT-4o:** Produção geral (balanceado)
- **GPT-4 Turbo:** Tarefas muito complexas
- **GPT-4:** Legado (usar GPT-4o)

---

## Instalação

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI(api_key="sk-proj-...")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Explique IA em 2 linhas"}
    ]
)

print(response.choices[0].message.content)
```

**Tutorial básico:** [API OpenAI Python](/blog/api-openai-python-2025/)

---

## Function calling avançado

**Caso de uso:** [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/) com múltiplas ferramentas

```python
from openai import OpenAI
import json

client = OpenAI(api_key="sk-proj-...")

# Definir ferramentas
tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Busca produto no catálogo",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string", "description": "Nome do produto"}
                },
                "required": ["nome"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calcular_frete",
            "description": "Calcula frete pelo CEP",
            "parameters": {
                "type": "object",
                "properties": {
                    "cep": {"type": "string", "description": "CEP de 8 dígitos"}
                },
                "required": ["cep"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "criar_pedido",
            "description": "Cria pedido no sistema",
            "parameters": {
                "type": "object",
                "properties": {
                    "produtos": {"type": "array", "items": {"type": "string"}},
                    "quantidade": {"type": "array", "items": {"type": "integer"}}
                },
                "required": ["produtos", "quantidade"]
            }
        }
    }
]

# Funções Python reais
def buscar_produto(nome):
    produtos = {
        "notebook": {"preco": 3500, "estoque": 10},
        "mouse": {"preco": 50, "estoque": 100}
    }
    return produtos.get(nome.lower(), {"erro": "Não encontrado"})

def calcular_frete(cep):
    # Integração real com API Correios/Melhor Envio
    return {"valor": 25.00, "prazo": 5}

def criar_pedido(produtos, quantidade):
    # Criar no banco de dados
    pedido_id = 12345
    return {"pedido_id": pedido_id, "status": "criado"}

# Conversa com tools
messages = [
    {"role": "system", "content": "Você é assistente de vendas da Loja X"},
    {"role": "user", "content": "Quero 2 notebooks. Quanto fica o frete pro CEP 01310-100?"}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

# Processar tool calls
while response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)

    # Executar função
    if function_name == "buscar_produto":
        result = buscar_produto(function_args["nome"])
    elif function_name == "calcular_frete":
        result = calcular_frete(function_args["cep"])
    elif function_name == "criar_pedido":
        result = criar_pedido(function_args["produtos"], function_args["quantidade"])

    # Adicionar resultado
    messages.append(response.choices[0].message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result)
    })

    # Nova chamada com resultado
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools
    )

print(response.choices[0].message.content)
# "2 notebooks custam R$ 7.000. O frete para 01310-100 é R$ 25 (5 dias). Total: R$ 7.025. Confirmar pedido?"
```

---

## Streaming (tempo real)

```python
from openai import OpenAI

client = OpenAI(api_key="sk-proj-...")

stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Conte uma história"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

**Benefício:** UX melhor (mostra resposta conforme gera)

---

## Vision (análise de imagens)

```python
from openai import OpenAI

client = OpenAI(api_key="sk-proj-...")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "O que tem nesta imagem?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/imagem.jpg"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
# "Esta imagem mostra um gato laranja dormindo em um sofá..."
```

**Custo:** Mesmos valores (input tokens calculados pela imagem)

---

## Embeddings (busca semântica)

```python
from openai import OpenAI
import numpy as np

client = OpenAI(api_key="sk-proj-...")

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Exemplo: Busca em documentos
documentos = [
    "Como funciona inteligência artificial",
    "Receita de bolo de chocolate",
    "Tutorial de Python"
]

# Gerar embeddings
embeddings = [get_embedding(doc) for doc in documentos]

# Busca
pergunta = "O que é IA?"
embedding_pergunta = get_embedding(pergunta)

# Calcular similaridade
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similaridades = [cosine_similarity(embedding_pergunta, emb) for emb in embeddings]

# Doc mais similar
indice_mais_similar = np.argmax(similaridades)
print(f"Documento mais relevante: {documentos[indice_mais_similar]}")
# "Como funciona inteligência artificial"
```

**Custo:** $0.02/1M tokens (muito barato)

---

## Rate limits (2025)

### Tier 1 (novo usuário):

- **RPM:** 500 requests/min
- **TPM:** 30.000 tokens/min
- **TPD:** 200.000 tokens/dia

### Tier 4 ($100 gastos):

- **RPM:** 5.000
- **TPM:** 600.000
- **TPD:** Ilimitado

**Verificar tier:** [platform.openai.com/account/limits](https://platform.openai.com/account/limits)

---

## Custos reais (calculadora)

### Chatbot: 1.000 conversas/mês

**Premissas:**
- 500 tokens input + 200 tokens output por conversa
- Total: 500k input + 200k output

**GPT-4o:**
- Input: 500k × $2.50/1M = $1.25
- Output: 200k × $10/1M = $2.00
- **Total:** $3.25/mês (R$ 16.25)

**GPT-4o-mini:**
- Input: 500k × $0.15/1M = $0.075
- Output: 200k × $0.60/1M = $0.12
- **Total:** $0.195/mês (R$ 0.98)

**Economia:** 94% usando GPT-4o-mini

---

## Casos reais

### Caso 1: Suporte automatizado

**Empresa:** SaaS B2B

**Stack:**
- GPT-4o
- RAG (base conhecimento)
- [WhatsApp Bot](/blog/whatsapp-bot-2025/)

**Volume:** 5.000 conversas/mês

**Custo:**
- GPT-4o: $16/mês
- VPS: R$ 50/mês
- **Total:** R$ 130/mês

**vs Humano:** 2 atendentes = R$ 5.000/mês
**Economia:** R$ 4.870/mês (97%)

### Caso 2: Análise de contratos

**Empresa:** Escritório advocacia

**Uso:**
- Upload PDF de contratos
- GPT-4 Turbo analisa cláusulas
- Gera resumo executivo

**Resultado:**
- Tempo análise: 2h → 5min (96% redução)
- Custo: $0.50/contrato
- 100 contratos/mês = $50

---

## Documentação

- [OpenAI API Docs](https://platform.openai.com/docs)
- [GPT-4 Guide](https://platform.openai.com/docs/guides/gpt)
- [Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Pricing](https://openai.com/api/pricing/)

---

## Próximos passos

1. **[API OpenAI Python](/blog/api-openai-python-2025/)** - Tutorial completo
2. **[Chatbot IA](/blog/chatbot-ia-2025/)** - Implementar chatbot
3. **[Flask Python](/blog/flask-python-tutorial-2025/)** - Criar API
4. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - WhatsApp + GPT-4

---

**Sobre o autor:** Felipe Zanoni é especialista em GPT-4 API, com 300+ integrações para empresas brasileiras.
