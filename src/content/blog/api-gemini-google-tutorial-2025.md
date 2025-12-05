---
title: "API Gemini Google: Tutorial Completo 2025"
description: "Integre Google Gemini API em apps Python/JavaScript. Tutorial completo com exemplos práticos, multimodal (texto + imagem) e casos de uso reais."
publishDate: 2025-02-07
author: "Felipe Zanoni"
category: "IA"
tags: ["google gemini", "gemini api", "ia multimodal", "python api", "google ai"]
draft: false
---

> **📚 Série:** APIs de IA
> → [API OpenAI Python](/blog/api-openai-python-2025/) | [Como usar ChatGPT](/blog/como-usar-chatgpt-guia-2025/) | [Claude AI](/blog/claude-ai-guia-completo-2025/)

## O que é API Gemini Google?

API Gemini Google é a interface de programação que permite integrar o modelo de IA multimodal Gemini (texto, imagem, vídeo, áudio) em aplicações Python, JavaScript, Go e outras linguagens. Lançada em dezembro de 2023, oferece versão gratuita generosa (60 requisições/minuto) e modelos desde Gemini 1.5 Flash (rápido) até Gemini 2.0 Pro (máxima capacidade). Diferente de ChatGPT, processa nativamente imagens e vídeos sem precisar de APIs separadas.

Com contexto de até 2 milhões de tokens (vs 128k do GPT-4), Gemini é ideal para analisar documentos longos, transcrições de vídeos e bases de conhecimento extensas.

---

## Por Que Usar Gemini vs ChatGPT API

### Comparação técnica

| Critério | Gemini 1.5 Pro | GPT-4o | GPT-4o mini |
|----------|----------------|--------|-------------|
| **Contexto** | 2M tokens | 128k | 128k |
| **Multimodal nativo** | ✅ Texto, imagem, vídeo, áudio | ✅ Texto, imagem | ✅ Texto, imagem |
| **Custo (1M tokens)** | $1.25 entrada / $5 saída | $2.50 / $10 | $0.15 / $0.60 |
| **Velocidade** | Média | Rápida | Muito rápida |
| **Plano grátis** | 60 req/min | ❌ Não | ❌ Não |
| **Idioma PT-BR** | ✅ Excelente | ✅ Excelente | ✅ Bom |

**Quando usar Gemini:**
- Analisar PDFs/documentos longos (100+ páginas)
- Processar vídeos (transcrição + análise visual)
- Custo menor em alto volume
- Prototipagem (plano grátis generoso)

**Quando usar ChatGPT:**
- Conversação avançada
- Geração criativa de texto
- Ecossistema maduro (plugins, ferramentas)

Tutorial completo ChatGPT: [Como usar ChatGPT](/blog/como-usar-chatgpt-guia-2025/)

---

## Setup Rápido (10 Minutos)

### Passo 1: Obter API Key

1. Acesse [aistudio.google.com](https://aistudio.google.com/app/apikey)
2. Clique "Get API Key"
3. Crie novo projeto ou use existente
4. Copie API key gerada

**Plano grátis:** 60 requisições/minuto, ilimitado/mês

---

### Passo 2: Instalar biblioteca Python

```bash
pip install google-generativeai
```

---

### Passo 3: Primeiro código (Texto)

```python
import google.generativeai as genai

# Configurar API key
genai.configure(api_key="SUA_API_KEY_AQUI")

# Escolher modelo
model = genai.GenerativeModel('gemini-1.5-flash')

# Gerar resposta
response = model.generate_content("Explique computação quântica em 3 frases")
print(response.text)
```

**Output:**
```
Computação quântica usa propriedades da mecânica quântica (superposição e entrelaçamento) para processar informação. Enquanto bits clássicos são 0 ou 1, qubits podem estar em ambos estados simultaneamente. Isso permite resolver problemas exponencialmente mais rápido que computadores tradicionais em tarefas específicas como simulação molecular e criptografia.
```

---

## Casos de Uso Práticos

### 1. Análise de Imagem

```python
import PIL.Image

# Carregar imagem
img = PIL.Image.open('produto.jpg')

# Analisar
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content([
    "Descreva este produto em detalhes para um anúncio de venda online. Inclua cores, materiais e estado de conservação.",
    img
])

print(response.text)
```

**Exemplo real:**
```
Input: Foto de tênis Nike usado
Output: "Tênis Nike Air Max preto com detalhes em vermelho. Material sintético com malha respirável. Sola de borracha com amortecimento visível. Estado de conservação 8/10: pequenos sinais de uso na sola, mas upper impecável. Tamanho aparente 42-43."
```

**Casos de uso:**
- E-commerce: Gerar descrições automáticas de produtos
- Moderação: Detectar conteúdo impróprio
- Acessibilidade: Descrições de imagens para deficientes visuais

---

### 2. Transcrição + Análise de Vídeo

```python
# Upload vídeo
video_file = genai.upload_file(path="reuniao.mp4")

# Aguardar processamento
import time
while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = genai.get_file(video_file.name)

# Analisar
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content([
    "Resuma os principais pontos desta reunião e extraia lista de tarefas mencionadas:",
    video_file
])

print(response.text)
```

**Output exemplo:**
```
Principais pontos:
1. Decisão de lançar produto em Q2 2025
2. Orçamento aprovado: R$ 50k
3. Responsável: João (marketing)

Tarefas:
- [ ] João: Criar landing page (prazo: 15/mar)
- [ ] Maria: Pesquisa de mercado (prazo: 01/mar)
- [ ] Pedro: Protótipo físico (prazo: 20/mar)
```

---

### 3. Chatbot com Histórico

```python
# Iniciar chat
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Conversa
response1 = chat.send_message("Olá, me chamo Felipe")
print(response1.text)
# "Olá Felipe! Como posso ajudar?"

response2 = chat.send_message("Qual meu nome?")
print(response2.text)
# "Seu nome é Felipe!"

# Ver histórico completo
print(chat.history)
```

**Integração com app:**
```python
# Salvar histórico em banco (Supabase, PostgreSQL)
import json

def salvar_historico(user_id, chat_history):
    with open(f'historico_{user_id}.json', 'w') as f:
        json.dump(chat_history, f)

def carregar_historico(user_id):
    with open(f'historico_{user_id}.json') as f:
        return json.load(f)

# Retomar conversa
historico_anterior = carregar_historico(user_id="123")
chat = model.start_chat(history=historico_anterior)
```

Veja integração com WhatsApp: [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)

---

### 4. Análise de PDF Longo

```python
# Upload PDF
pdf_file = genai.upload_file('contrato_50_paginas.pdf')

# Analisar
response = model.generate_content([
    "Resuma este contrato em 5 tópicos principais. Identifique cláusulas de rescisão e multas.",
    pdf_file
])

print(response.text)
```

**Vantagem:** Gemini suporta até 2M tokens (equivalente a ~1.500 páginas). ChatGPT suporta apenas 128k tokens (~100 páginas).

---

## Caso Real: Startup Analisa 10k Currículos com Gemini

**Empresa:** Startup RH tech (triagem de currículos para clientes)

**Problema:**
- 10.000 currículos/mês para analisar
- Tempo humano: 5 min/currículo = 833 horas/mês
- Custo: R$ 25.000/mês (3 analistas)

**Solução:**

```python
import google.generativeai as genai
import PyPDF2

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def analisar_curriculo(pdf_path, vaga_requisitos):
    # Upload PDF
    cv = genai.upload_file(pdf_path)

    # Prompt estruturado
    prompt = f'''
    Analise este currículo para vaga de {vaga_requisitos["titulo"]}.

    Requisitos obrigatórios:
    {vaga_requisitos["obrigatorios"]}

    Requisitos desejáveis:
    {vaga_requisitos["desejaveis"]}

    Retorne JSON:
    {{
        "score": 0-100,
        "atende_obrigatorios": true/false,
        "pontos_fortes": [],
        "pontos_fracos": [],
        "recomendacao": "Aprovar/Reprovar/Entrevistar"
    }}
    '''

    response = model.generate_content([prompt, cv])
    return response.text

# Uso
vaga = {
    "titulo": "Desenvolvedor Python Sênior",
    "obrigatorios": "5+ anos Python, Django, PostgreSQL",
    "desejaveis": "Docker, AWS, React"
}

resultado = analisar_curriculo("curriculo_001.pdf", vaga)
print(resultado)
```

**Resultados (6 meses):**
- ✅ Currículos analisados: 60.000 (vs 10.000 manual)
- ✅ Tempo análise: 5 min → 30 segundos (90% redução)
- ✅ Custo: R$ 25k/mês → R$ 1.200/mês (API Gemini)
- ✅ Precisão: 87% (vs 92% humano)
- ✅ Economia: R$ 23.800/mês
- ✅ **ROI: 1.983%**

**Aprendizado:** IA não substitui completamente humanos (precisão 87% vs 92%), mas acelera triagem inicial. Analistas focam apenas nos top 20% candidatos pré-selecionados.

---

## Modelos Disponíveis

| Modelo | Velocidade | Capacidade | Contexto | Custo (1M tokens) | Uso ideal |
|--------|-----------|------------|----------|-------------------|-----------|
| **Gemini 2.0 Flash** | Muito rápida | Alta | 1M | $0.10 / $0.40 | Chatbots, apps tempo real |
| **Gemini 1.5 Flash** | Rápida | Média-Alta | 1M | $0.075 / $0.30 | Uso geral |
| **Gemini 1.5 Pro** | Média | Máxima | 2M | $1.25 / $5.00 | Análise complexa, raciocínio |
| **Gemini 1.0 Pro** | Média | Básica | 32k | $0.50 / $1.50 | Legacy (descontinuado) |

**Recomendação:**
- **Prototipagem:** Gemini 2.0 Flash (rápido e barato)
- **Produção alto volume:** Gemini 1.5 Flash
- **Tarefas complexas:** Gemini 1.5 Pro

---

## Limitações e Como Contornar

### 1. Rate Limits (Plano grátis)

**Limites:**
- 60 requisições/minuto
- 1.500 requisições/dia
- 1M tokens/minuto

**Solução:**
```python
import time
from tenacity import retry, wait_exponential

@retry(wait=wait_exponential(min=1, max=60))
def gerar_com_retry(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):  # Rate limit
            print("Rate limit atingido, aguardando...")
            time.sleep(60)
            raise
        else:
            raise
```

---

### 2. Alucinações (inventar fatos)

**Problema:** Gemini pode inventar dados, especialmente em tópicos obscuros.

**Solução:**
```python
# Pedir fontes
prompt = "Explique fusão nuclear. Cite fontes confiáveis para cada afirmação."

# Ou adicionar verificação
prompt2 = "Se não tiver certeza sobre alguma informação, diga 'Não tenho dados confiáveis sobre isso'."
```

---

### 3. Custo em escala

**Cenário:** 1 milhão de requisições/mês com Gemini 1.5 Pro

**Cálculo:**
- Entrada média: 1k tokens
- Saída média: 500 tokens
- Custo entrada: 1M × $1.25 = $1.250
- Custo saída: 0.5M × $5 = $2.500
- **Total: $3.750/mês (~R$ 18.750)**

**Solução:** Usar Gemini 2.0 Flash (10x mais barato):
- **Total: $375/mês (~R$ 1.875)**

---

## Integração com Frameworks

### 1. LangChain

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=API_KEY)

response = llm.invoke("Olá, como você funciona?")
print(response.content)
```

---

### 2. Flask (API REST)

```python
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/api/gerar', methods=['POST'])
def gerar():
    prompt = request.json['prompt']
    response = model.generate_content(prompt)
    return jsonify({"resposta": response.text})

if __name__ == '__main__':
    app.run(port=5000)
```

Veja tutorial completo: [API REST Flask](/blog/api-rest-flask-tutorial-2025/)

---

## Documentação Oficial

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- [Python SDK](https://ai.google.dev/gemini-api/docs/quickstart?lang=python)
- [Pricing](https://ai.google.dev/pricing)

---

## Próximos passos

1. **[API OpenAI Python](/blog/api-openai-python-2025/)** - Comparação com ChatGPT
2. **[Como usar ChatGPT](/blog/como-usar-chatgpt-guia-2025/)** - Interface web vs API
3. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Integração prática
4. **[Automação Python](/blog/automacao-python-guia-2025/)** - Scripts com IA
5. **[IA para Conteúdo](/blog/ia-para-conteudo-guia-2025/)** - Casos de uso criativos

---

**Sobre o autor:** Felipe Zanoni é especialista em integração de APIs de IA, com 200+ projetos usando Google Gemini e OpenAI para empresas brasileiras. Fundador da Agência Café Online.
