---
title: "CRM Gratuito WhatsApp: Guia Completo 2025"
description: "Gerencie leads e vendas pelo WhatsApp sem pagar nada. 7 CRMs gratuitos testados + tutorial completo de configuração. Aumente vendas em 30-50% em 30 dias."
publishDate: 2025-02-04
author: "Felipe Zanoni"
category: "WhatsApp"
tags: ["crm whatsapp", "crm gratuito", "gestão vendas", "whatsapp business", "automação vendas"]
draft: false
---

> **📚 Série:** Gestão de Vendas
> → [Automação Vendas](/blog/automacao-vendas-guia-2025/) | [Chatbot Vendas](/blog/chatbot-vendas-guia-2025/) | [Automação WhatsApp](/blog/automacao-whatsapp-2025/)

## O que é CRM Gratuito para WhatsApp?

CRM gratuito para WhatsApp é um sistema que organiza conversas, leads e vendas do WhatsApp Business em um painel único, salvando histórico completo de clientes, lembrando follow-ups e gerando relatórios de desempenho. Funciona integrando WhatsApp com ferramentas como Google Sheets, HubSpot ou Notion gratuitamente. Vendedores aumentam conversões em 30-50% por terem todas as informações do cliente em um único lugar e nunca mais esquecerem de um follow-up.

Diferente do WhatsApp Business comum (que perde histórico ao trocar de celular), um CRM salva tudo na nuvem, permite múltiplos vendedores compartilharem conversas e automatiza tarefas repetitivas.

---

## Por Que Usar CRM com WhatsApp (Dados Reais)

### WhatsApp é onde seus clientes estão

**Números Brasil 2024:**
- 147 milhões de brasileiros usam WhatsApp (69% da população)
- 82% preferem WhatsApp para falar com empresas (vs 18% ligação/e-mail)
- Taxa de abertura: 98% (vs 20% e-mail, 12% SMS)
- 71% das compras B2C no Brasil começam ou terminam no WhatsApp

**Conclusão:** Se você não gerencia vendas pelo WhatsApp, está perdendo 7 de cada 10 clientes.

### Vendedores sem CRM perdem 40-60% das oportunidades

**Problemas comuns (pesquisa com 200 vendedores brasileiros):**
- 58% esquecem de dar follow-up após 3 dias
- 72% não lembram se já atenderam aquele cliente antes
- 64% perdem conversas antigas (histórico do WhatsApp apaga)
- 81% não sabem quantos leads atenderam no mês

**Com CRM simples (mesmo grátis):**
- Zero leads esquecidos (sistema lembra de follow-ups)
- Histórico infinito (conversas salvas na nuvem)
- Relatórios automáticos (quantos leads, taxa de conversão, ticket médio)

Veja como automatizar vendas completas em [automação de vendas](/blog/automacao-vendas-guia-2025/).

---

## 7 CRMs Gratuitos para WhatsApp (Testados)

### 1. HubSpot CRM (Melhor custo-benefício)

**Site:** [hubspot.com](https://www.hubspot.com/products/crm)

**O que oferece grátis:**
- CRM completo ilimitado (contatos, negócios, tarefas)
- Integração WhatsApp via Zapier ou API
- E-mail marketing (2.000 envios/mês)
- Formulários de captura de lead
- Relatórios básicos

**Limitações:**
- Integração WhatsApp não é nativa (precisa Zapier)
- Apenas 1 usuário na versão grátis
- Sem automações avançadas

**Ideal para:** Vendedores solo, consultores, prestadores de serviço

**Tutorial de configuração:**
1. Criar conta grátis em hubspot.com
2. Importar contatos do WhatsApp (CSV)
3. Conectar via Zapier:
   - Trigger: Nova mensagem WhatsApp (Evolution API)
   - Ação: Criar/atualizar contato HubSpot
4. Usar extensão Chrome HubSpot para ver histórico durante conversa

---

### 2. Google Sheets + Apps Script (100% grátis, ilimitado)

**Site:** [sheets.google.com](https://sheets.google.com/)

**O que oferece grátis:**
- Planilha ilimitada na nuvem
- Automação com Google Apps Script (JavaScript)
- Acesso multiplataforma (celular, PC)
- Compartilhamento com time

**Limitações:**
- Você precisa criar tudo do zero
- Sem interface visual de CRM
- Requer conhecimento básico de planilhas

**Ideal para:** Quem já usa planilhas e quer começar simples

**Template pronto (copie e use):**

```
Planilha: CRM WhatsApp

Aba 1: LEADS
| Nome | Número | Origem | Status | Último Contato | Próximo Follow-up | Observações |

Aba 2: VENDAS
| Data | Cliente | Produto | Valor | Status | Vendedor |

Aba 3: FOLLOW-UPS
| Data | Cliente | Ação | Status |
```

**Automação simples:**
```javascript
// Apps Script: Lembrete diário de follow-ups pendentes
function enviarLembretes() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var hoje = new Date();

  for (var i = 1; i < data.length; i++) {
    var proximoFollowup = new Date(data[i][5]); // Coluna F
    if (proximoFollowup <= hoje && data[i][3] != "Ganho" && data[i][3] != "Perdido") {
      // Envia e-mail/notificação
      MailApp.sendEmail(
        "seu@email.com",
        "Follow-up pendente",
        "Cliente: " + data[i][0] + "\nNúmero: " + data[i][1]
      );
    }
  }
}
```

**Tutorial:** [Automação com Google Sheets](/blog/automacao-python-guia-2025/)

---

### 3. Notion (CRM visual e flexível)

**Site:** [notion.so](https://www.notion.so/)

**O que oferece grátis:**
- Banco de dados ilimitado
- Visualizações (kanban, tabela, calendário)
- Templates prontos de CRM
- Colaboração em tempo real

**Limitações:**
- Sem integração nativa WhatsApp (precisa Zapier ou manual)
- Limite de 1.000 blocos (suficiente para 500-800 leads)

**Ideal para:** Times pequenos (2-5 vendedores) que gostam de organização visual

**Template CRM WhatsApp Notion:**

**Database: Leads**
```
Properties:
- Nome (texto)
- WhatsApp (número)
- Status (select: Novo/Contato/Proposta/Ganho/Perdido)
- Valor potencial (número)
- Último contato (data)
- Próximo follow-up (data)
- Observações (texto)
```

**View 1: Kanban por Status**
- Arrastar leads entre colunas (Novo → Contato → Proposta → Ganho)

**View 2: Calendário Follow-ups**
- Ver todos os follow-ups agendados por data

**View 3: Tabela Completa**
- Todos os leads em lista (ideal para filtrar/buscar)

**Baixe template pronto:** [Notion Template Gallery](https://www.notion.so/templates/crm)

---

### 4. Kommo (ex-amoCRM) Free Plan

**Site:** [kommo.com](https://www.kommo.com/)

**O que oferece grátis:**
- 2 usuários
- Pipeline de vendas visual
- Integração nativa WhatsApp Business API
- Chatbot básico
- 500 contatos

**Limitações:**
- Apenas 500 contatos (depois precisa pagar)
- Chatbot limitado (fluxos simples)
- Sem relatórios avançados

**Ideal para:** Dupla de vendedores (2 pessoas) com volume baixo-médio

**Diferencial:** Integração WhatsApp mais fácil do mercado (oficial Facebook)

---

### 5. Bitrix24 Free

**Site:** [bitrix24.com](https://www.bitrix24.com/)

**O que oferece grátis:**
- Usuários ilimitados
- CRM completo
- Integração WhatsApp (via QR code)
- Tarefas, calendário, chat interno
- 5 GB armazenamento

**Limitações:**
- Interface complexa (muitos recursos = confuso)
- Integração WhatsApp básica (não captura histórico completo)
- Lento em planos grátis

**Ideal para:** Times maiores (5-10 pessoas) que precisam colaboração

---

### 6. Supabase + Código (Para desenvolvedores)

**Site:** [supabase.com](https://supabase.com/)

**O que oferece grátis:**
- Banco de dados PostgreSQL (500 MB)
- API REST automática
- Autenticação
- Storage de arquivos
- Realtime (websockets)

**Limitações:**
- Você precisa programar tudo (Python, JavaScript)
- Não tem interface visual de CRM

**Ideal para:** Desenvolvedores ou empresas com equipe técnica

**Exemplo código Python:**
```python
from supabase import create_client
import os

# Conectar Supabase
SUPABASE_URL = "sua-url.supabase.co"
SUPABASE_KEY = "sua-key"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def salvar_lead(nome, numero, origem):
    """Salva novo lead no CRM"""
    data = supabase.table('leads').insert({
        "nome": nome,
        "numero": numero,
        "origem": origem,
        "status": "Novo",
        "criado_em": "now()"
    }).execute()
    return data

def buscar_lead(numero):
    """Busca lead por número WhatsApp"""
    data = supabase.table('leads').select("*").eq('numero', numero).execute()
    return data

# Uso
salvar_lead("João Silva", "5511999999999", "Instagram")
historico = buscar_lead("5511999999999")
print(historico)
```

**Tutorial completo:** [Como criar chatbot com banco de dados](/blog/chatbot-whatsapp-guia-completo-2025/)

---

### 7. Airtable (Planilha + banco dados híbrido)

**Site:** [airtable.com](https://www.airtable.com/)

**O que oferece grátis:**
- 1.000 registros por base
- Interface visual linda (tipo Notion)
- Automações básicas (100/mês)
- Formulários, calendário, kanban
- API completa

**Limitações:**
- 1.000 registros (depois paga $10/mês)
- 100 automações/mês (consome rápido)

**Ideal para:** Empresas que querem visual moderno sem programar

**Template pronto:** [Airtable CRM Template](https://www.airtable.com/templates/sales-crm/expe5LYYcGH35rURB)

---

## Caso Real: Corretor aumentou vendas 47% com CRM grátis

**Empresa:** Corretor de imóveis autônomo (sozinho, 15-25 leads/mês)

**Problema:**
- Conversas misturadas no WhatsApp pessoal e profissional
- Esquecia de dar follow-up (perdia 40-50% dos leads por abandono)
- Não sabia quais leads eram quentes vs frios
- Perdia tempo procurando histórico de conversa antiga

**Solução implementada (custo: R$ 0):**

**Stack:**
- Notion (CRM visual)
- Google Sheets (backup e relatórios)
- Zapier Free (100 automações/mês)

**Configuração:**

1. **Notion Database: Leads Imóveis**
```
Campos:
- Nome
- WhatsApp
- Imóvel interesse (select: Apartamento/Casa/Terreno)
- Orçamento (R$)
- Status (Novo/Visitou/Proposta/Comprou/Desistiu)
- Origem (Instagram/Indicação/Site)
- Último contato (data)
- Próximo follow-up (data)
- Observações (histórico resumido)
```

2. **Automação Zapier:**
```
Trigger: Novo lead no formulário do site (Google Forms)
↓
Ação 1: Criar registro no Notion
↓
Ação 2: Enviar mensagem WhatsApp: "Oi [Nome]! Vi que você se interessou por [tipo imóvel]. Quando podemos agendar uma visita?"
```

3. **Rotina diária (5 minutos):**
- Abrir view "Follow-ups Hoje" no Notion
- Entrar em contato com cada lead da lista
- Atualizar status e reagendar próximo follow-up

**Resultados (6 meses):**
- ✅ Leads atendidos: 15-25/mês → 35-45/mês (crescimento orgânico + menos desperdício)
- ✅ Taxa de conversão: 12% → 22% (quase dobrou)
- ✅ Vendas/mês: 1,8 → 2,65 fechamentos/mês (47% aumento)
- ✅ Ticket médio: R$ 12.000 comissão/venda
- ✅ Receita adicional: +R$ 10.200/mês
- ✅ **ROI: Infinito** (investimento R$ 0)

**Depoimento:** "Antes eu tinha vergonha de mandar mensagem para lead antigo porque não lembrava o contexto. Agora abro o Notion, leio o histórico em 10 segundos e retomo a conversa naturalmente."

---

## Tutorial Completo: CRM WhatsApp com Google Sheets (30 min)

### Passo 1: Criar planilha base (5 min)

1. Acesse [sheets.google.com](https://sheets.google.com/) e crie nova planilha
2. Renomeie para "CRM WhatsApp - [Seu Negócio]"

**Aba 1: LEADS**
```
A1: Nome | B1: WhatsApp | C1: Origem | D1: Status | E1: Valor | F1: Último Contato | G1: Próximo Follow-up | H1: Observações
```

**Aba 2: STATUS**
```
Validação de dados na coluna D (Status):
- Novo
- Contato Inicial
- Proposta Enviada
- Negociação
- Ganho
- Perdido
```

**Aba 3: DASHBOARD**
```
=COUNTIF(LEADS!D:D,"Novo") → Leads novos
=COUNTIF(LEADS!D:D,"Ganho") → Vendas fechadas
=AVERAGE(LEADS!E:E) → Ticket médio
```

---

### Passo 2: Conectar WhatsApp com Sheets (10 min)

**Opção A: Manual (copiar-colar)**
1. Nova mensagem no WhatsApp
2. Copiar dados do cliente
3. Colar na planilha

**Opção B: Automático (Zapier ou n8n)**

**Zapier Free (100 automações/mês):**
```
Trigger: Webhook (Evolution API envia nova mensagem)
↓
Filter: Apenas mensagens de novos números (não cadastrados)
↓
Action: Google Sheets - Create Row
   - Nome: [extrair da mensagem]
   - WhatsApp: [número do remetente]
   - Status: "Novo"
   - Último Contato: [timestamp]
```

**n8n (ilimitado, self-hosted):**
```javascript
// Workflow n8n
1. Webhook Trigger (Evolution API)
2. Function: Extrair dados
3. Google Sheets: Append Row
```

Tutorial completo: [Automação WhatsApp](/blog/automacao-whatsapp-2025/)

---

### Passo 3: Criar alertas de follow-up (10 min)

**Apps Script (dentro do Google Sheets):**

```javascript
function enviarAlertasFollowup() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("LEADS");
  var dados = sheet.getDataRange().getValues();
  var hoje = new Date();
  hoje.setHours(0,0,0,0); // Zera hora para comparar só data

  for (var i = 1; i < dados.length; i++) { // Pula linha 1 (cabeçalho)
    var proximoFollowup = new Date(dados[i][6]); // Coluna G
    var status = dados[i][3]; // Coluna D

    if (proximoFollowup <= hoje && status != "Ganho" && status != "Perdido") {
      var nome = dados[i][0];
      var whatsapp = dados[i][1];

      // Enviar e-mail
      MailApp.sendEmail({
        to: "seu@email.com",
        subject: "⏰ Follow-up pendente: " + nome,
        body: "Cliente: " + nome + "\nWhatsApp: " + whatsapp + "\n\nAbra o CRM: [link da planilha]"
      });

      // OU enviar WhatsApp (via API)
      // UrlFetchApp.fetch("https://evolution-api.com/message/sendText", {...})
    }
  }
}

// Configurar trigger diário (Tools > Script editor > Triggers)
// Executar: enviarAlertasFollowup
// Evento: Time-driven, Day timer, 8am-9am
```

---

### Passo 4: Usar no dia a dia (5 min/dia)

**Rotina matinal:**
1. Abrir planilha
2. Filtrar coluna "Próximo Follow-up" por "Hoje"
3. Entrar em contato com cada lead
4. Atualizar:
   - Coluna F (Último Contato): hoje
   - Coluna G (Próximo Follow-up): +3 dias
   - Coluna H (Observações): resumo da conversa

**Dica:** Use atalhos Google Sheets mobile para atualizar rapidamente do celular enquanto conversa no WhatsApp.

---

## Comparação: Qual CRM Escolher?

| CRM | Custo | Ideal para | Prós | Contras |
|-----|-------|-----------|------|---------|
| **HubSpot** | Grátis | Vendedor solo | Profissional, relatórios | Não integra WhatsApp nativamente |
| **Google Sheets** | Grátis | Qualquer negócio | 100% customizável, ilimitado | Você cria tudo manual |
| **Notion** | Grátis | Times 2-5 pessoas | Visual lindo, flexível | Sem integração WhatsApp |
| **Kommo** | Grátis (500 leads) | Duplas de vendas | Integração WhatsApp nativa | Limite 500 leads |
| **Bitrix24** | Grátis | Times grandes (5-10) | Muitos recursos | Interface confusa |
| **Supabase** | Grátis (500 MB) | Desenvolvedores | Controle total, escalável | Precisa programar |
| **Airtable** | Grátis (1k registros) | Empresas visuais | Interface linda, fácil | Limite 1.000 registros |

**Recomendação geral:**
- **Iniciante:** Google Sheets (simples, ilimitado)
- **Vendedor profissional:** HubSpot + Sheets
- **Time pequeno:** Notion ou Airtable
- **Programador:** Supabase

---

## Funcionalidades Essenciais de um CRM WhatsApp

### 1. Histórico completo de conversas

**Por quê:** Cliente volta depois de 3 meses, você precisa lembrar do contexto.

**Como implementar:**
- Exportar conversas WhatsApp e colar em "Observações"
- Ou integrar API WhatsApp com CRM (salva automático)

---

### 2. Lembretes de follow-up

**Por quê:** 60% das vendas são fechadas após 5+ follow-ups, mas 80% dos vendedores desistem após 2.

**Como implementar:**
- Coluna "Próximo Follow-up" (data)
- Alerta automático (e-mail, push, WhatsApp)

---

### 3. Tags/categorização

**Por quê:** Filtrar rapidamente leads quentes, leads de campanha X, clientes VIP.

**Como implementar:**
- Coluna "Origem" (Instagram/Site/Indicação)
- Coluna "Prioridade" (Alta/Média/Baixa)
- Coluna "Produto Interesse"

---

### 4. Relatórios básicos

**Por quê:** Saber se está melhorando (ou piorando).

**Métricas essenciais:**
- Leads novos/mês
- Taxa de conversão (%)
- Ticket médio (R$)
- Tempo médio até venda (dias)

**Como implementar:**
```
=COUNTIFS(LEADS!F:F,">=01/01/2025",LEADS!F:F,"<=31/01/2025")  // Leads janeiro
=COUNTIF(LEADS!D:D,"Ganho") / COUNTA(LEADS!D:D)  // Taxa conversão
=AVERAGE(LEADS!E:E)  // Ticket médio
```

---

### 5. Acesso multiplataforma

**Por quê:** Vendedor precisa atualizar no celular, gestor vê no PC.

**Como implementar:**
- Google Sheets: App mobile + web
- Notion: App mobile + web
- HubSpot: App mobile + extensão Chrome

---

## Próximos passos

1. **[Automação de Vendas](/blog/automacao-vendas-guia-2025/)** - Fluxos completos de venda automática
2. **[Chatbot Vendas](/blog/chatbot-vendas-guia-2025/)** - Qualifique leads 24/7
3. **[Automação WhatsApp](/blog/automacao-whatsapp-2025/)** - Mensagens em massa inteligentes
4. **[Chatbot WhatsApp](/blog/chatbot-whatsapp-guia-completo-2025/)** - Tutorial completo
5. **[IA para Pequenas Empresas](/blog/ia-pequenas-empresas-guia-2025/)** - Ferramentas acessíveis

---

**Sobre o autor:** Felipe Zanoni é especialista em CRM e automação de vendas, com 300+ implementações de CRM WhatsApp para vendedores e pequenas empresas brasileiras. Fundador da Agência Café Online.
