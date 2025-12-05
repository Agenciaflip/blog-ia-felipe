#!/usr/bin/env python3
"""
Gerador de 50 Briefings para Blog IA & Automação
Pesquisa keywords em lote (eficiente) via DataForSEO
Custo total: ~$0.40 para 50 keywords
"""

import requests
import json
import os
from datetime import datetime
from pathlib import Path
import time

def pesquisar_keywords_batch(keywords_list, login, password):
    """
    Pesquisa múltiplas keywords de uma vez (mais eficiente)
    """
    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"

    payload = [{
        "location_code": 2076,  # Brasil
        "language_code": "pt",
        "keywords": keywords_list
    }]

    response = requests.post(
        url,
        auth=(login, password),
        headers={"Content-Type": "application/json"},
        json=payload
    )

    if response.status_code == 200:
        result = response.json()
        if result['tasks'][0]['status_code'] == 20000:
            return result['tasks'][0]['result']

    return []

def gerar_briefing(keyword, volume, cpc, competition, categoria):
    """
    Gera briefing markdown otimizado
    """

    # Normalizar valores None
    volume = volume or 0
    cpc = cpc or 0

    # Análise de valor
    valor = "MUITO ALTO" if cpc > 4 else "ALTO" if cpc > 2 else "MÉDIO" if cpc > 1 else "BAIXO"

    # Análise de dificuldade
    comp_str = str(competition).upper()
    if comp_str == "HIGH":
        dif = "ALTA"
    elif comp_str == "MEDIUM":
        dif = "MÉDIA"
    elif comp_str == "LOW":
        dif = "BAIXA"
    else:
        dif = "MÉDIA"

    # Prioridade (quanto maior volume + CPC, melhor)
    score = (volume * cpc) / 1000
    prioridade = "🔥 URGENTE" if score > 10 else "⭐ ALTA" if score > 5 else "✅ MÉDIA" if score > 1 else "⏳ BAIXA"

    # Gerar título otimizado
    keyword_title = keyword.title()
    titulo = f"{keyword_title}: Guia Completo 2025"

    if "como" in keyword.lower():
        titulo = f"{keyword_title} [Tutorial Passo a Passo]"
    elif "melhor" in keyword.lower() or "top" in keyword.lower():
        titulo = f"{keyword_title} - Ranking Atualizado 2025"

    briefing = f"""# BRIEFING - {keyword}

**Categoria:** {categoria}
**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}
**Prioridade:** {prioridade}

---

## 📊 DADOS BRASIL

| Métrica | Valor | Análise |
|---------|-------|---------|
| Volume mensal | **{volume:,}** buscas/mês | {'🔥 ALTO' if volume > 1000 else '📈 MÉDIO' if volume > 300 else '📉 BAIXO'} |
| CPC (Google Ads) | **R$ {cpc:.2f}** | {valor} |
| Competition | **{comp_str}** | {dif} |
| Score (Oportunidade) | **{score:.1f}** | {prioridade} |

---

## 💰 ANÁLISE COMERCIAL

**Valor por lead:** {'R$ 50-200 (alto valor comercial)' if cpc > 3 else 'R$ 20-80 (médio valor)' if cpc > 1.5 else 'R$ 5-30 (baixo valor)'}

**Intenção de busca:** {'🛒 Comercial (pronto para comprar)' if cpc > 3 else '🔍 Informacional (pesquisando)' if cpc < 1.5 else '🤔 Mista (comparando opções)'}

**ROI esperado (12 meses):**
- Tráfego estimado: {int(volume * 0.05)} - {int(volume * 0.15)} visitas/mês (após rankear)
- Leads: {int(volume * 0.001)} - {int(volume * 0.005)}/mês
- Receita potencial: R$ {int(volume * 0.001 * 2000):,} - R$ {int(volume * 0.005 * 5000):,}/ano

---

## ✍️ ESTRUTURA RECOMENDADA

### 📌 Title Tag (50-60 chars):
{titulo}

### 📝 Meta Description (150-160 chars):
Aprenda {keyword} com tutorial completo, código funcional e cases reais. Implementação em 3-5 horas. ROI 200%+ comprovado.

### 🎯 H1:
{titulo}

### 📋 H2 (Featured Snippet - 40-60 palavras):
**{keyword.capitalize()}?**

[Resposta direta: passos numerados OU definição concisa]

### 📖 Estrutura do Artigo:

**H2:** Por que {keyword.split()[0]} é importante em 2025
**H2:** Principais ferramentas/métodos para {keyword}
**H2:** Tutorial passo a passo (código quando aplicável)
**H2:** 3 casos reais de sucesso (ROI + métricas)
**H2:** Quanto custa: análise financeira completa
**H2:** Erros comuns e como evitar
**H2:** Conclusão + próximos passos

---

## 🎨 DIRETRIZES DE CONTEÚDO

**Palavra count:** 2.000-2.500 palavras

**Tom:** Profissional mas acessível (como conversa com especialista)

**Incluir obrigatoriamente:**
- ✅ Código funcional (Python/JavaScript quando aplicável)
- ✅ 2-3 cases genéricos com ROI real
- ✅ Tabelas comparativas (ferramentas, custos, etc)
- ✅ Listas numeradas (Google adora)
- ✅ Screenshots/diagramas (quando útil)

**CTA (Call-to-Action):**
Sutil no final: "Precisa de ajuda para implementar? A Agência Café Online já automatizou [tema] para 20+ empresas."

---

## 🔑 KEYWORDS LSI (usar naturalmente):

{chr(10).join([f'- {keyword} tutorial',
               f'- {keyword} passo a passo',
               f'- {keyword} 2025',
               f'- como usar {keyword}',
               f'- {keyword} grátis'])}

---

## 🎯 OBJETIVOS SEO

1. **Featured Snippet:** Resposta 40-60 palavras no topo (60% chance)
2. **Top 10:** Rankear primeira página em 3-6 meses
3. **Internal Links:** Linkar para 3-5 artigos relacionados
4. **Backlinks:** Criar conteúdo "linkable" (infográfico, ferramenta, estudo)

---

## 📈 KPIs (12 meses):

- **Impressões:** {int(volume * 12 * 0.3):,} - {int(volume * 12 * 0.5):,}
- **Cliques:** {int(volume * 0.5 * 12):,} - {int(volume * 1.5 * 12):,}
- **Posição média:** Top 5-10
- **CTR:** 15-25%

---

## 💡 DICAS ESPECÍFICAS:

{f'⚡ Keyword HOT! Volume alto ({volume:,}/mês) = prioridade máxima' if volume > 1000 else ''}
{f'💰 CPC alto (R$ {cpc:.2f}) = conteúdo premium, foque em conversão' if cpc > 3 else ''}
{f'🎯 Competition {comp_str} = {"difícil rankear, foque em long-tail" if comp_str == "HIGH" else "boa oportunidade, invista!"}' if comp_str else ''}

---

**Custo desta pesquisa:** $0.0008 (R$ 0.004)
**Próximo passo:** Criar artigo seguindo esta estrutura
"""

    return briefing

def main():
    # Credenciais
    login = "contato@agenciaflip.com.br"
    password = "5bbf090558f5620b"

    # 50 Keywords categorizadas
    keywords_50 = {
        "Vendas": [
            "chatbot vendas",
            "ia para vendas",
            "automação vendas",
            "crm vendas",
            "funil de vendas",
            "prospecção vendas",
            "cold email vendas",
            "follow up vendas",
            "chatbot qualificação leads",
            "vendas b2b automação"
        ],
        "Marketing": [
            "marketing digital ia",
            "chatgpt marketing",
            "ia para criar anúncios",
            "automação marketing",
            "email marketing automação",
            "copywriting ia",
            "seo ia",
            "conteúdo ia",
            "redes sociais automação",
            "tráfego pago automação"
        ],
        "WhatsApp": [
            "chatbot whatsapp",
            "automação whatsapp",
            "whatsapp business automação",
            "api whatsapp",
            "chatbot whatsapp grátis",
            "como criar chatbot whatsapp",
            "whatsapp bot python",
            "evolution api",
            "zapier whatsapp",
            "n8n whatsapp"
        ],
        "Automação": [
            "automação python",
            "automação processos",
            "rpa automação",
            "zapier automação",
            "n8n tutorial",
            "make automação",
            "integração api",
            "webhook automação",
            "automação tarefas",
            "workflow automação"
        ],
        "Produtividade": [
            "chatgpt produtividade",
            "ia produtividade",
            "automação escritório",
            "ferramentas ia",
            "gemini ia",
            "claude ai",
            "gpt-4 uso",
            "prompts chatgpt",
            "ia para estudar",
            "ia para trabalho"
        ]
    }

    # Preparar todas keywords
    todas_keywords = []
    mapa_categoria = {}

    for categoria, keywords in keywords_50.items():
        for kw in keywords:
            todas_keywords.append(kw)
            mapa_categoria[kw] = categoria

    print(f"🔍 Pesquisando {len(todas_keywords)} keywords no Brasil...\n")

    # Pesquisar em lote (eficiente!)
    resultados = pesquisar_keywords_batch(todas_keywords, login, password)

    if not resultados:
        print("❌ Erro ao buscar dados da API")
        return

    # Ordenar por oportunidade (volume * CPC)
    resultados_sorted = sorted(
        resultados,
        key=lambda x: (x.get('search_volume') or 0) * (x.get('cpc') or 0),
        reverse=True
    )

    # Criar diretório
    output_dir = Path("briefings")
    output_dir.mkdir(exist_ok=True)

    # Gerar briefings
    print(f"📝 Gerando {len(resultados)} briefings...\n")
    print(f"{'Keyword':<30} {'Volume':<12} {'CPC':<10} {'Score':<10} {'Status'}")
    print("-" * 80)

    briefings_criados = 0
    custo_total = len(resultados) * 0.0008

    for item in resultados_sorted:
        keyword = item['keyword']
        volume = item.get('search_volume', 0)
        cpc = item.get('cpc', 0)
        competition = item.get('competition', 'MEDIUM')
        categoria = mapa_categoria.get(keyword, "Geral")

        score = ((volume or 0) * (cpc or 0)) / 1000

        # Gerar briefing
        briefing = gerar_briefing(keyword, volume, cpc, competition, categoria)

        # Salvar
        filename = f"{keyword.replace(' ', '_')}.md"
        filepath = output_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(briefing)

        briefings_criados += 1

        status = "🔥" if score > 10 else "⭐" if score > 5 else "✅" if score > 1 else "⏳"

        print(f"{keyword:<30} {(volume or 0):>10,}/mês  R$ {(cpc or 0):>6.2f}  {score:>8.1f}  {status}")

    # Resumo final
    print(f"\n{'='*80}")
    print(f"🎉 CONCLUÍDO!")
    print(f"✅ {briefings_criados} briefings criados")
    print(f"💰 Custo total: ${custo_total:.2f} (R$ {custo_total * 5:.2f})")
    print(f"📂 Salvos em: {output_dir}/")
    print(f"{'='*80}\n")

    # Top 10 melhores oportunidades
    print("🏆 TOP 10 MELHORES OPORTUNIDADES:\n")
    print(f"{'#':<4} {'Keyword':<30} {'Volume':<12} {'CPC':<10} {'Score'}")
    print("-" * 70)

    for i, item in enumerate(resultados_sorted[:10], 1):
        kw = item['keyword']
        vol = item.get('search_volume', 0)
        cpc_val = item.get('cpc', 0)
        score_val = ((vol or 0) * (cpc_val or 0)) / 1000

        print(f"{i:<4} {kw:<30} {(vol or 0):>10,}/mês  R$ {(cpc_val or 0):>6.2f}  {score_val:>8.1f}")

    print(f"\n💡 Recomendação: Comece pelos 10 primeiros (maior ROI)\n")

    # Criar índice
    criar_indice(output_dir, resultados_sorted, mapa_categoria)

def criar_indice(output_dir, resultados, mapa_categoria):
    """
    Cria arquivo índice com todas keywords organizadas
    """

    indice = f"""# ÍNDICE DE BRIEFINGS - Blog IA & Automação

**Data:** {datetime.now().strftime('%d/%m/%Y %H:%M')}
**Total:** {len(resultados)} briefings

---

## 🏆 TOP 20 POR OPORTUNIDADE (Volume × CPC)

| # | Keyword | Volume/mês | CPC | Score | Categoria |
|---|---------|------------|-----|-------|-----------|
"""

    for i, item in enumerate(resultados[:20], 1):
        kw = item['keyword']
        vol = item.get('search_volume', 0)
        cpc = item.get('cpc', 0)
        score = ((vol or 0) * (cpc or 0)) / 1000
        cat = mapa_categoria.get(kw, "Geral")

        indice += f"| {i} | {kw} | {(vol or 0):,} | R$ {(cpc or 0):.2f} | {score:.1f} | {cat} |\n"

    indice += "\n---\n\n## 📚 POR CATEGORIA\n\n"

    # Agrupar por categoria
    categorias = {}
    for item in resultados:
        kw = item['keyword']
        cat = mapa_categoria.get(kw, "Geral")
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(item)

    for categoria, items in categorias.items():
        indice += f"\n### {categoria} ({len(items)} artigos)\n\n"

        for item in items:
            kw = item['keyword']
            vol = item.get('search_volume', 0)
            arquivo = f"{kw.replace(' ', '_')}.md"
            indice += f"- [{kw}]({arquivo}) - {(vol or 0):,}/mês\n"

    # Salvar índice
    with open(output_dir / "INDICE.md", 'w', encoding='utf-8') as f:
        f.write(indice)

    print(f"📋 Índice criado: {output_dir / 'INDICE.md'}")

if __name__ == "__main__":
    main()
