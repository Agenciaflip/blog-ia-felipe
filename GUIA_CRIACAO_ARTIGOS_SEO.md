# 📖 GUIA DE CRIAÇÃO DE ARTIGOS SEO - Blog IA & Automação

**Última atualização:** 30/11/2025 18:52 BRT

---

## 🎯 OBJETIVO

Criar artigos otimizados para SEO que **rankeiem no Top 3-10 do Google** para keywords de alto volume no Brasil, seguindo estratégia pillar-cluster com E-E-A-T.

---

## 📋 REGRAS OBRIGATÓRIAS (CHECKLIST)

### ✅ Estrutura do Frontmatter

```markdown
---
title: "[Keyword Principal]: Guia Completo 2025"
description: "[150-160 chars] Resumo com keyword + benefício claro + call-to-action implícito"
publishDate: 2025-01-XX
author: "Felipe Zanoni"
category: "[WhatsApp/Vendas/IA/Automação]"
tags: ["[keyword principal]", "[keyword secundária 1]", "[keyword secundária 2]", "[keyword secundária 3]"]
draft: false
---
```

**❌ NUNCA:**
- Colocar "[X Buscas/Mês]" no título
- Usar emojis no título
- Title com mais de 60 caracteres
- Description com mais de 160 caracteres

**✅ SEMPRE:**
- Title: Keyword exata + "Guia Completo 2025"
- Description: Keyword + benefício + CTA
- Category: Uma das 4 principais (WhatsApp/Vendas/IA/Automação)
- Tags: 3-5 keywords relacionadas

---

### ✅ Breadcrumbs (Cluster Navigation)

**SEMPRE começar artigo com:**

```markdown
> **📚 Série:** [Nome do Cluster]
> → [Artigo 1](/blog/slug-artigo-1/) | [Artigo 2](/blog/slug-artigo-2/) | [Artigo 3](/blog/slug-artigo-3/)
```

**Exemplos:**

```markdown
> **📚 Série:** Automação WhatsApp com IA
> → [Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/) | [API WhatsApp](/blog/api-whatsapp-guia-completo/) | [Evolution API](/blog/evolution-api-tutorial-completo/)
```

```markdown
> **📚 Série:** IA para Vendas
> → [CRM Vendas](/blog/crm-vendas-guia-completo-2025/) | [Automação Vendas](/blog/automacao-vendas-2025/) | [Follow-up Automático](/blog/follow-up-vendas-automatico/)
```

**Clusters existentes:**
1. **Automação WhatsApp com IA** (4 artigos publicados)
2. **IA para Vendas** (1 artigo publicado)
3. **Chatbots Inteligentes** (pendente)
4. **Infraestrutura & Deploy** (pendente)

---

### ✅ Featured Snippet (Resposta Direta)

**SEMPRE incluir logo após breadcrumbs:**

```markdown
## O que é [Keyword]?

[Resposta em 40-60 palavras que responde EXATAMENTE a pergunta]

[Opcional: 2-3 frases complementares expandindo a resposta]
```

**Regras:**
- Primeira frase: 40-60 palavras
- Formato: parágrafo OU lista numerada (se aplicável)
- Linguagem simples (8ª série)
- Resposta completa e autossuficiente

**Exemplo BOM:**

```markdown
## O que é chatbot WhatsApp?

Chatbot WhatsApp é um sistema de atendimento automatizado que usa inteligência artificial para responder mensagens no WhatsApp Business. Funciona 24/7, qualifica leads, tira dúvidas e transfere para humanos quando necessário. Empresas economizam 70-85% do tempo de atendimento e aumentam conversões em 40-60%.
```

**Exemplo RUIM:**

```markdown
## O que é chatbot WhatsApp?

É uma ferramenta muito útil para empresas que querem automatizar o atendimento. Existem várias opções no mercado...
```
(❌ Não responde diretamente, ❌ Vago, ❌ Sem dados concretos)

---

### ✅ Word Count (Contagem de Palavras)

**Mínimo:** 500 palavras
**Ideal:** 1.500-2.500 palavras
**Máximo:** 3.500 palavras (evitar artigos muito longos)

**Distribuição recomendada:**

| Tipo de artigo | Word count |
|----------------|------------|
| Tutorial técnico (Python, API) | 1.200-1.800 |
| Guia completo (Chatbot, CRM) | 1.500-2.500 |
| Comparação (X vs Y) | 800-1.200 |
| Lista (Top 10, 7 ferramentas) | 1.000-1.500 |

**❌ NUNCA:**
- Artigo com menos de 500 palavras (penaliza SEO)
- Encher linguiça para atingir word count (Google detecta)

**✅ SEMPRE:**
- Conteúdo denso e útil
- Exemplos práticos
- Dados concretos (ROI, métricas, custos)

---

### ✅ Internal Links (Links Internos)

**Mínimo:** 6 links internos por artigo
**Ideal:** 8-12 links internos
**Máximo:** 15 links (evitar over-optimization)

**Onde colocar:**

1. **Breadcrumbs** (3-4 links) ✅ Obrigatório
2. **Corpo do artigo** (3-5 links) - contextuais, não forçados
3. **"Próximos passos"** (3-4 links) ✅ Obrigatório

**Formato links internos:**

```markdown
[Texto âncora descritivo](/blog/slug-do-artigo/)
```

**Exemplos BOM:**

```markdown
Integre com [CRM de vendas](/blog/crm-vendas-guia-completo-2025/) para centralizar leads.

Para conectar WhatsApp via API, use [Evolution API](/blog/evolution-api-tutorial-completo/) (grátis e open-source).

Automatize respostas com [chatbot IA](/blog/chatbot-whatsapp-guia-completo-2025/).
```

**Exemplos RUIM:**

```markdown
Clique [aqui](/blog/crm-vendas-guia-completo-2025/) para saber mais.
(❌ Âncora genérica)

Veja este [artigo](/blog/evolution-api-tutorial-completo/).
(❌ Não descritivo)

[https://blog.agenciacafeonline.com.br/blog/chatbot-whatsapp-guia-completo-2025/](/blog/chatbot-whatsapp-guia-completo-2025/)
(❌ URL como âncora)
```

**Seção "Próximos passos" (Obrigatória):**

```markdown
## Próximos passos

1. **[Criar Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Automatizar atendimento
2. **[Configurar Evolution API](/blog/evolution-api-tutorial-completo/)** - Setup completo
3. **[Integrar CRM](/blog/crm-vendas-guia-completo-2025/)** - Centralizar leads
4. **[Usar API WhatsApp](/blog/api-whatsapp-guia-completo/)** - Integrações avançadas
```

---

### ✅ External Links (Links Externos)

**Mínimo:** 5 links externos por artigo
**Ideal:** 8-12 links externos
**Máximo:** 20 links (evitar spam)

**Tipos obrigatórios:**

1. **Documentação oficial** (2-3 links)
   - developers.facebook.com
   - evolution-api.com
   - platform.openai.com
   - developers.hubspot.com

2. **Ferramentas mencionadas** (2-3 links)
   - zapier.com
   - n8n.io
   - hubspot.com
   - pipedrive.com

3. **Pesquisas/Estatísticas** (1-2 links)
   - salesforce.com/research
   - gartner.com
   - forrester.com

**Formato:**

```markdown
[Texto âncora](https://dominio.com/path)
```

**Exemplos BOM:**

```markdown
Segundo pesquisa da [Salesforce](https://www.salesforce.com/research/), 79% das empresas top-performers usam CRM.

Documentação: [WhatsApp Business API](https://developers.facebook.com/docs/whatsapp/cloud-api/)

**Site oficial:** [evolution-api.com](https://evolution-api.com/)
```

**❌ NUNCA:**
- Linkar para concorrentes diretos
- Linkar para sites de baixa qualidade (spam, afiliados)
- Usar rel="nofollow" em links editoriais

---

### ✅ Code Blocks (Blocos de Código)

**Formato CORRETO:**

```markdown
```python
import requests

def funcao():
    return "valor"
` ``
```

**❌ NUNCA:**

```markdown
\`\`\`python   ← Backslash escapa o bloco!
import requests
\`\`\`
```

**Regras:**

1. **Sempre especificar linguagem:** `python`, `javascript`, `bash`, `json`, `env`
2. **Comentários explicativos:** Use `# Comentário` para explicar código
3. **Código funcional:** Apenas código que realmente funciona (nada de pseudo-código)
4. **Syntax highlighting:** Astro usa Shiki automaticamente (theme: github-dark)

**Exemplo completo:**

```markdown
```python
import requests

# Configurações da API
EVOLUTION_URL = "https://sua-evolution.com.br"
API_KEY = "sua_api_key"

def enviar_mensagem(numero, texto):
    """Envia mensagem via Evolution API"""
    url = f"{EVOLUTION_URL}/message/sendText/instancia"

    payload = {
        "number": numero,  # Ex: 5511999999999
        "text": texto
    }

    headers = {"apikey": API_KEY}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Uso
enviar_mensagem("5511999999999", "Olá!")
` ``
```

---

### ✅ Cases Reais (Exemplos)

**Obrigatório:** 1-3 cases por artigo

**Formato:**

```markdown
## Caso Real: [Tipo de empresa] [resultado %]

**Empresa:** [Tipo genérico] ([Tamanho], [Setor])

**Problema:**
- [Dor 1]
- [Dor 2]
- [Métrica antes]

**Solução:**
- [Ferramenta 1]
- [Ferramenta 2]
- [Implementação]

**Resultados ([tempo]):**
- ✅ [Métrica 1]: [antes] → [depois]
- ✅ [Métrica 2]: [antes] → [depois]
- ✅ [ROI]: [%]
- ✅ [Custo]: [valor/mês]
```

**Exemplo:**

```markdown
## Caso Real: E-commerce recuperou R$ 47k/mês

**Empresa:** Loja online de eletrônicos (porte médio)

**Problema:**
- 320 carrinhos abandonados/mês
- Taxa de recuperação: 2% (manual)
- Receita perdida: ~R$ 180k/mês

**Solução:**
- N8N + Evolution API
- Após 1h: "Olá! Vi que você deixou produtos no carrinho. Posso ajudar?"
- Após 24h: Cupom 10% desconto
- Após 3 dias: Última chance + 15% desconto

**Resultados (3 meses):**
- ✅ Taxa recuperação: 2% → 18%
- ✅ 58 vendas recuperadas/mês
- ✅ R$ 47.200 receita adicional/mês
- ✅ Custo automação: R$ 380/mês
- ✅ **ROI: 12.300%**
```

**❌ NUNCA usar:**
- Nomes reais de clientes (usar genéricos)
- Nomes de empresas específicas
- Dados que possam identificar cliente

**✅ SEMPRE usar:**
- Nomes genéricos: "Padaria Regional", "Clínica Odontológica", "E-commerce Moda"
- Dados reais mas genéricos: "porte médio", "5 vendedores", "50 clientes"
- ROI e métricas concretas

---

### ✅ E-E-A-T (Experience, Expertise, Authoritativeness, Trust)

**Obrigatório em TODOS artigos:**

1. **Experience (Experiência)**
   - Cases reais (genéricos)
   - "Testamos 15 ferramentas..."
   - "Implementamos em 20+ clientes..."
   - Screenshots (quando aplicável)

2. **Expertise (Especialização)**
   - Author bio no final
   - Código funcional (Python/JavaScript)
   - Tutoriais técnicos passo-a-passo
   - Comparações profundas

3. **Authoritativeness (Autoridade)**
   - Links para docs oficiais
   - Citações de pesquisas (Salesforce, Gartner)
   - Mention Agência Café Online
   - Dados concretos (não "muitos", mas "79%")

4. **Trustworthiness (Confiabilidade)**
   - Sem clickbait
   - Sem promessas impossíveis
   - Transparência (custos, limitações)
   - Links para fontes primárias

**Author bio (final de TODOS artigos):**

```markdown
**Sobre o autor:** Felipe Zanoni é especialista em [tema específico do artigo], com [300-500]+ horas de experiência [contexto específico].
```

**Exemplos:**

```markdown
**Sobre o autor:** Felipe Zanoni é especialista em Evolution API, com 300+ implementações para empresas brasileiras.

**Sobre o autor:** Felipe Zanoni é desenvolvedor especializado em integrações WhatsApp, com 500+ horas de experiência.

**Sobre o autor:** Felipe Zanoni é especialista em automação de vendas com IA, com 500+ horas implementando CRMs.
```

---

### ✅ Schema.org (Markup Estruturado)

**Astro implementa automaticamente:**

- ✅ BlogPosting schema (title, description, author, publishDate)
- ✅ Organization schema (Agência Café Online)
- ✅ Breadcrumbs schema (navegação)

**NÃO precisa adicionar manualmente** no artigo.

---

### ✅ Images & Media

**Opcional mas recomendado:**

```markdown
![Alt text descritivo](/images/nome-imagem.webp)
```

**Regras:**
- Formato: WebP (melhor compressão)
- Alt text: Descritivo, com keyword quando natural
- Tamanho máximo: 200KB por imagem
- Dimensões: 1200×630 (ideal para OG)

**Pasta:**
- Local: `/public/images/`
- URL: `/images/nome-imagem.webp`

---

## 📝 TEMPLATE COMPLETO DE ARTIGO

```markdown
---
title: "[Keyword]: Guia Completo 2025"
description: "[150-160 chars com keyword + benefício]"
publishDate: 2025-01-XX
author: "Felipe Zanoni"
category: "[WhatsApp/Vendas/IA/Automação]"
tags: ["keyword 1", "keyword 2", "keyword 3"]
draft: false
---

> **📚 Série:** [Nome do Cluster]
> → [Artigo 1](/blog/slug-1/) | [Artigo 2](/blog/slug-2/) | [Artigo 3](/blog/slug-3/)

## O que é [Keyword]?

[Resposta em 40-60 palavras]

[2-3 frases complementares]

---

## [H2 Principal 1]

[Conteúdo denso com exemplos práticos]

[Internal link contextual](/blog/artigo-relacionado/)

### [H3 Subtópico]

[Detalhamento]

---

## [H2 Principal 2]

### Comparação / Tutorial / Lista

[Conteúdo estruturado]

```python
# Código funcional
def exemplo():
    return "valor"
` ``

---

## Caso Real: [Título do case]

**Empresa:** [Tipo genérico]

**Problema:**
- [Dor 1]
- [Dor 2]

**Solução:**
- [Ferramenta 1]
- [Ferramenta 2]

**Resultados:**
- ✅ [Métrica 1]
- ✅ [ROI]

---

## [Links externos para ferramentas]

- [Ferramenta 1](https://exemplo.com)
- [Ferramenta 2](https://exemplo.com)

**Documentação oficial:**
- [Docs oficiais](https://developers.exemplo.com/)

---

## Próximos passos

1. **[Artigo relacionado 1](/blog/slug-1/)** - Descrição
2. **[Artigo relacionado 2](/blog/slug-2/)** - Descrição
3. **[Artigo relacionado 3](/blog/slug-3/)** - Descrição

---

**Sobre o autor:** Felipe Zanoni é especialista em [tema], com [X]+ horas de experiência [contexto].
```

---

## 🚀 WORKFLOW DE CRIAÇÃO

### 1. Preparação (5 min)

1. Escolher keyword do briefing
2. Ler briefing completo
3. Verificar artigos relacionados já publicados (para internal links)

### 2. Pesquisa (10 min)

1. Google: pesquisar keyword
2. Analisar Top 3 resultados
3. Identificar gaps (o que falta nos concorrentes)
4. Listar 5-10 external links úteis

### 3. Estrutura (10 min)

1. Criar outline H2/H3
2. Definir featured snippet (40-60 palavras)
3. Planejar cases (1-3)
4. Listar internal links (6-12)

### 4. Redação (30-60 min)

1. Escrever featured snippet
2. Desenvolver H2s em ordem
3. Adicionar code blocks (se aplicável)
4. Inserir cases reais
5. Adicionar internal/external links
6. Escrever "Próximos passos"
7. Adicionar author bio

### 5. Revisão (10 min)

1. **Checklist SEO:**
   - [ ] Title sem "[X Buscas/Mês]"
   - [ ] Description 150-160 chars
   - [ ] Breadcrumbs com cluster
   - [ ] Featured snippet 40-60 palavras
   - [ ] 500-2.500 palavras
   - [ ] 6-12 internal links
   - [ ] 5-12 external links
   - [ ] 1-3 cases reais
   - [ ] Author bio
   - [ ] "Próximos passos"

2. **Checklist Técnico:**
   - [ ] Code blocks sem `\` (backslash)
   - [ ] Markdown válido
   - [ ] Links funcionando
   - [ ] Nomes genéricos (não clientes reais)

3. **Checklist Qualidade:**
   - [ ] Conteúdo útil e denso
   - [ ] Exemplos práticos
   - [ ] Dados concretos (ROI, métricas)
   - [ ] Sem clickbait
   - [ ] Linguagem clara

### 6. Publicação (5 min)

1. Salvar arquivo: `src/content/blog/keyword-slug.md`
2. Build: `npm run build`
3. Testar local: `npm run dev` (http://localhost:4321)
4. Deploy: `npm run deploy`
5. Verificar URL: https://blog.agenciacafeonline.com.br/blog/keyword-slug/

---

## 🔍 CHECKLIST FINAL (PRÉ-DEPLOY)

### Frontmatter ✅
- [ ] title: sem "[X Buscas/Mês]", com "2025"
- [ ] description: 150-160 chars
- [ ] publishDate: 2025-01-XX
- [ ] author: "Felipe Zanoni"
- [ ] category: válida
- [ ] tags: 3-5 keywords
- [ ] draft: false

### Estrutura ✅
- [ ] Breadcrumbs (Série + 3-4 links)
- [ ] Featured snippet (40-60 palavras)
- [ ] H2/H3 estruturados
- [ ] Cases reais (1-3)
- [ ] "Próximos passos" (3-4 links)
- [ ] Author bio

### Links ✅
- [ ] Internal: 6-12 links
- [ ] External: 5-12 links
- [ ] Todos funcionando
- [ ] Ânco ras descritivas

### Código ✅
- [ ] Blocos com ` ``` ` (sem `\`)
- [ ] Linguagem especificada
- [ ] Código funcional
- [ ] Comentários explicativos

### Qualidade ✅
- [ ] 500-2.500 palavras
- [ ] Conteúdo denso
- [ ] Exemplos práticos
- [ ] Dados concretos
- [ ] Sem nomes reais de clientes

### Build ✅
- [ ] `npm run build` sem erros
- [ ] `npm run dev` renderiza correto
- [ ] Código com syntax highlighting
- [ ] Links internos funcionando

---

## 🎨 EXEMPLOS DE REFERÊNCIA

**Artigos modelo (copiar estrutura):**

1. **Tutorial técnico:** `/blog/evolution-api-tutorial-completo/`
   - Código Python/Bash
   - Passo-a-passo
   - Troubleshooting

2. **Guia completo:** `/blog/chatbot-whatsapp-guia-completo-2025/`
   - Featured snippet
   - Cases reais
   - Pillar-cluster

3. **Comparação:** `/blog/api-whatsapp-guia-completo/`
   - Tabela comparativa
   - Prós/contras
   - Recomendação

4. **Ferramentas:** `/blog/crm-vendas-guia-completo-2025/`
   - Top 5 lista
   - Preços
   - Casos de uso

---

## ⚠️ ERROS COMUNS (EVITAR)

### ❌ Título
- "Chatbot WhatsApp [8.100 Buscas/Mês]" → Parece spam
- "Chatbot" → Muito genérico
- "O Melhor Chatbot WhatsApp de Todos os Tempos" → Clickbait

### ❌ Featured Snippet
- Resposta com mais de 100 palavras → Muito longo
- "Neste artigo vamos falar sobre..." → Não responde
- Resposta vaga sem dados → Não útil

### ❌ Code Blocks
- `\`\`\`python` → Escapa o bloco
- Código sem linguagem → Sem syntax highlighting
- Pseudo-código → Não funciona

### ❌ Links
- "Clique aqui" → Âncora genérica
- Link para URL completa → Feio
- Só external links → Sem topical authority

### ❌ Cases
- "Cliente X da empresa Y" → Expõe cliente real
- Case sem dados concretos → Não confiável
- ROI impossível (50.000%) → Não crível

---

## 📊 MÉTRICAS DE SUCESSO

**Após publicar, monitorar:**

1. **Google Search Console (Semana 1):**
   - Indexação (artigo apareceu?)
   - Impressões (quantas vezes apareceu?)
   - Cliques (quantos clicaram?)
   - CTR (% de cliques)

2. **Rankings (Mês 1-3):**
   - Posição para keyword principal
   - Posições para keywords secundárias
   - Featured snippet conquistado?

3. **Engagement (Mês 1-6):**
   - Tempo na página (ideal: >3 min)
   - Bounce rate (ideal: <60%)
   - Páginas/sessão (ideal: >1.5)

**Metas:**
- Mês 1: Indexado + Top 50
- Mês 2: Top 20
- Mês 3: Top 10
- Mês 6: Top 3

---

## 🔗 RECURSOS

**Documentação:**
- Índice completo: `/INDICE_COMPLETO_ARTIGOS_SEO.md`
- Estudo SEO: `/ESTUDO_COMPLETO_SEO_RANKEAMENTO_2025.md`
- Briefings: `/briefings/`

**Ferramentas:**
- DataForSEO: https://app.dataforseo.com/
- Google Search Console: https://search.google.com/search-console
- Cloudflare Pages: https://dash.cloudflare.com

**Comandos:**
```bash
# Desenvolvimento local
npm run dev

# Build
npm run build

# Deploy
npm run deploy
```

---

**Criado por:** Felipe Zanoni + Claude Code
**Data:** 30/11/2025 18:52 BRT
**Versão:** 1.0
