---
title: "Automação Python: Guia Completo 2025"
description: "Automatize tarefas com Python: scripts que economizam 20h/semana, libraries essenciais (Selenium, Pandas, Schedule) e projetos práticos."
publishDate: 2025-01-18
author: "Felipe Zanoni"
category: "Automação"
tags: ["python", "automação", "selenium", "pandas", "scripts"]
draft: false
---

> **📚 Série:** Automação com Python
> → [Zapier](/blog/zapier-automacao-guia-completo-2025/) | [RPA](/blog/rpa-automacao-guia-completo-2025/) | [N8N](/blog/n8n-automacao-guia-completo-2025/)

## O que é Automação Python?

Automação Python usa scripts e libraries (Selenium, BeautifulSoup, Pandas, Schedule) para executar tarefas repetitivas de TI (web scraping, processamento arquivos, envio emails, testes QA) que antes exigiam horas de trabalho manual. Python = linguagem ideal para automação por sintaxe simples + 300k+ packages PyPI cobrindo QUALQUER caso uso. Empresas economizam 20-40h/semana automatizando data entry, reports, backups e integrações vs trabalho manual ou ferramentas SaaS limitadas.

Diferença vs no-code (Zapier/Make): Python = 100% customizável (qualquer lógica complexa) vs no-code = templates prontos (mais rápido setup, menos flexibilidade).

---

## Por Que Python para Automação?

### Vantagens Python:

1. **Sintaxe Simples:**
```python
# Enviar email (3 linhas)
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.sendmail('from@email.com', 'to@email.com', 'Mensagem')
```

2. **Libraries para TUDO:**
- **Web scraping:** Selenium, BeautifulSoup, Scrapy
- **Data processing:** Pandas, NumPy
- **Automação desktop:** PyAutoGUI, Pywin32
- **APIs:** Requests, FastAPI
- **Schedule:** APScheduler, Cron

3. **Cross-platform:**
- Roda Linux, Windows, macOS (mesmo código)
- Deploy em servidor (cron/systemd)

4. **Gratuito + Open-Source:**
- Zero licença (vs UiPath $2k/ano)
- Comunidade gigante (Stack Overflow)

---

## Top 10 Libraries Automação Python

### 1. Selenium - Web Automation

**Uso:** Automatizar navegador (login, forms, scraping dinâmico)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Abrir navegador
driver = webdriver.Chrome()
driver.get("https://site.com/login")

# Preencher form
driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("pass")
driver.find_element(By.ID, "submit").click()

# Extrair dados após login
dados = driver.find_element(By.CLASS_NAME, "dashboard").text
```

**Casos uso:**
- Testes QA automatizados
- Web scraping sites com JavaScript
- Bot WhatsApp Web
- Preenchimento forms repetitivos

**Install:** `pip install selenium`

### 2. Pandas - Data Processing

**Uso:** Manipular Excel/CSV (ler, transformar, salvar)

```python
import pandas as pd

# Ler Excel
df = pd.read_excel('vendas.xlsx')

# Filtrar (vendas >R$ 1k)
df_filtrado = df[df['valor'] > 1000]

# Agrupar por vendedor
resumo = df.groupby('vendedor')['valor'].sum()

# Salvar resultado
resumo.to_excel('resumo_vendedores.xlsx')
```

**Casos uso:**
- Relatórios automatizados
- Limpeza dados
- Merge múltiplos arquivos
- Data analysis

**Install:** `pip install pandas openpyxl`

### 3. Requests - API Calls

**Uso:** Integrar com APIs REST (GET/POST)

```python
import requests

# GET request
response = requests.get('https://api.com/users')
users = response.json()

# POST request (criar recurso)
data = {"name": "João", "email": "joao@email.com"}
requests.post('https://api.com/users', json=data)
```

**Casos uso:**
- Integração CRM/ERP
- Web scraping APIs
- Webhook envio/recebimento
- Testar endpoints

**Install:** `pip install requests`

### 4. Schedule - Agendar Tarefas

**Uso:** Executar scripts em horários específicos

```python
import schedule
import time

def tarefa():
    print("Executando backup...")
    # código backup aqui

# Agendar
schedule.every().day.at("02:00").do(tarefa)  # Todo dia 2am
schedule.every().monday.at("09:00").do(tarefa)  # Segundas 9am
schedule.every(30).minutes.do(tarefa)  # A cada 30min

# Loop infinito
while True:
    schedule.run_pending()
    time.sleep(60)
```

**Casos uso:**
- Backups automáticos
- Scraping periódico
- Envio relatórios (diário/semanal)
- Monitoramento

**Install:** `pip install schedule`

### 5. BeautifulSoup - HTML Parsing

**Uso:** Extrair dados HTML (scraping)

```python
from bs4 import BeautifulSoup
import requests

# Baixar página
html = requests.get('https://site.com/produtos').text

# Parsear
soup = BeautifulSoup(html, 'html.parser')

# Extrair elementos
produtos = soup.find_all('div', class_='produto')
for produto in produtos:
    nome = produto.find('h2').text
    preco = produto.find('span', class_='preco').text
    print(f"{nome}: {preco}")
```

**Casos uso:**
- Scraping preços competidores
- Monitorar mudanças site
- Extrair dados públicos
- Agregação notícias

**Install:** `pip install beautifulsoup4`

### 6. Openpyxl - Excel Avançado

**Uso:** Manipular Excel (formatar, fórmulas, gráficos)

```python
from openpyxl import load_workbook
from openpyxl.styles import Font

# Abrir Excel existente
wb = load_workbook('relatorio.xlsx')
ws = wb.active

# Adicionar dados
ws['A1'] = 'Vendedor'
ws['B1'] = 'Total'
ws['A1'].font = Font(bold=True)

# Adicionar fórmula
ws['B10'] = '=SUM(B2:B9)'

# Salvar
wb.save('relatorio_atualizado.xlsx')
```

**Casos uso:**
- Relatórios formatados
- Dashboards Excel
- Fórmulas dinâmicas
- Templates automatizados

**Install:** `pip install openpyxl`

### 7. PyAutoGUI - Desktop Automation

**Uso:** Controlar mouse/teclado (RPA simples)

```python
import pyautogui
import time

# Clicar posição específica
pyautogui.click(x=100, y=200)

# Digitar texto
pyautogui.write('Hello World', interval=0.1)

# Pressionar teclas
pyautogui.press('enter')

# Screenshot
screenshot = pyautogui.screenshot()
screenshot.save('tela.png')
```

**Casos uso:**
- Automação apps desktop (sem API)
- Testes GUI
- Preenchimento forms legados
- Screenshots automáticos

**Install:** `pip install pyautogui`

### 8. Pathlib - File Management

**Uso:** Manipular arquivos/pastas (Python moderno)

```python
from pathlib import Path

# Criar pasta
Path('relatorios/2025').mkdir(parents=True, exist_ok=True)

# Listar arquivos
for arquivo in Path('downloads').glob('*.pdf'):
    # Mover para pasta organizada
    arquivo.rename(f'pdfs/{arquivo.name}')

# Ler/escrever arquivo
Path('config.txt').write_text('configuração')
conteudo = Path('config.txt').read_text()
```

**Casos uso:**
- Organização arquivos
- Backup automático
- File watching (monitorar pasta)
- Batch rename

**Install:** Nativo Python 3.4+

### 9. Smtplib - Envio Emails

**Uso:** Enviar emails automaticamente

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurar
msg = MIMEMultipart()
msg['From'] = 'sender@email.com'
msg['To'] = 'recipient@email.com'
msg['Subject'] = 'Relatório Diário'

# Corpo email
body = "Anexo relatório vendas hoje."
msg.attach(MIMEText(body, 'plain'))

# Enviar
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender@email.com', 'senha')
server.send_message(msg)
server.quit()
```

**Casos uso:**
- Alertas automáticos
- Relatórios agendados
- Notificações sistema
- Email marketing

**Install:** Nativo Python

### 10. Watchdog - File Watcher

**Uso:** Monitorar pasta (novos arquivos = trigger)

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith('.csv'):
            print(f"Novo CSV: {event.src_path}")
            # Processar arquivo
            processar_csv(event.src_path)

# Monitorar pasta
observer = Observer()
observer.schedule(Handler(), path='downloads', recursive=False)
observer.start()

# Rodar infinito
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
```

**Casos uso:**
- Processar uploads automático
- Sync pastas
- Hot reload development
- Import automático

**Install:** `pip install watchdog`

---

## 10 Projetos Automação Python Práticos

### Projeto 1: Scraping Preços Competidores

**Objetivo:** Monitorar preços 3 e-commerces diariamente

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

sites = {
    'Site A': 'https://sitea.com/produto-x',
    'Site B': 'https://siteb.com/produto-x',
    'Site C': 'https://sitec.com/produto-x'
}

precos = []
for nome, url in sites.items():
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    preco = soup.find('span', class_='preco').text
    precos.append({
        'site': nome,
        'preco': preco,
        'data': datetime.now()
    })

# Salvar Excel
df = pd.DataFrame(precos)
df.to_excel(f'precos_{datetime.now().date()}.xlsx', index=False)
```

**ROI:** E-commerce - Competitividade preços 24/7

### Projeto 2: Relatório Email Automático

**Objetivo:** Enviar relatório vendas diário 8am

```python
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def gerar_relatorio():
    df = pd.read_excel('vendas.xlsx')
    resumo = df.groupby('vendedor')['valor'].sum()
    resumo.to_excel('relatorio_diario.xlsx')
    return 'relatorio_diario.xlsx'

def enviar_email(arquivo):
    msg = MIMEMultipart()
    msg['From'] = 'sender@email.com'
    msg['To'] = 'gerente@empresa.com'
    msg['Subject'] = f'Relatório Vendas - {datetime.now().date()}'
    
    # Anexar arquivo
    with open(arquivo, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={arquivo}')
        msg.attach(part)
    
    # Enviar
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sender@email.com', 'senha')
    server.send_message(msg)
    server.quit()

# Agendar diariamente 8am
import schedule
schedule.every().day.at("08:00").do(lambda: enviar_email(gerar_relatorio()))

while True:
    schedule.run_pending()
    time.sleep(60)
```

**ROI:** Gerência - Visibilidade vendas diária automática

### Projeto 3: Backup Automático Google Drive

**Objetivo:** Backup pasta local → Google Drive diariamente

```python
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path

# Autenticar
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def backup_pasta(pasta_local, pasta_drive_id):
    for arquivo in Path(pasta_local).rglob('*'):
        if arquivo.is_file():
            file_drive = drive.CreateFile({
                'title': arquivo.name,
                'parents': [{'id': pasta_drive_id}]
            })
            file_drive.SetContentFile(str(arquivo))
            file_drive.Upload()
            print(f'Backup: {arquivo.name}')

# Agendar backup diário 2am
schedule.every().day.at("02:00").do(
    lambda: backup_pasta('documentos', 'ID_PASTA_DRIVE')
)
```

**ROI:** Backup 100% automático (zero risco perda dados)

### Projeto 4: Bot WhatsApp Resposta Automática

**Objetivo:** Responder mensagens WhatsApp fora horário

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input("Escaneie QR Code e pressione Enter...")

def verificar_novas_mensagens():
    mensagens = driver.find_elements(By.CLASS_NAME, 'message-in')
    if mensagens:
        ultima = mensagens[-1].text
        if not_respondido(ultima):
            enviar_resposta("Obrigado pela mensagem! Horário atendimento: 9h-18h.")

def enviar_resposta(texto):
    caixa_texto = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
    caixa_texto.send_keys(texto)
    botao_enviar = driver.find_element(By.XPATH, '//button[@aria-label="Enviar"]')
    botao_enviar.click()

# Loop verificar mensagens
while True:
    verificar_novas_mensagens()
    time.sleep(30)  # Checar a cada 30seg
```

**ROI:** Atendimento 24/7 (expectativa cliente gerenciada)

### Projeto 5: Merge 100 Planilhas

**Objetivo:** Consolidar vendas 100 filiais em 1 Excel

```python
import pandas as pd
from pathlib import Path

# Ler todas planilhas pasta
dfs = []
for arquivo in Path('vendas_filiais').glob('*.xlsx'):
    df = pd.read_excel(arquivo)
    df['filial'] = arquivo.stem  # Adicionar coluna filial
    dfs.append(df)

# Concatenar todas
df_consolidado = pd.concat(dfs, ignore_index=True)

# Calcular totais
totais = df_consolidado.groupby('filial')['valor'].sum()

# Salvar
df_consolidado.to_excel('vendas_consolidado.xlsx', index=False)
totais.to_excel('totais_filiais.xlsx')
```

**ROI:** 100 arquivos processados em 10 segundos vs 3h manual

---

## Python vs No-Code (Zapier/Make)

| Aspecto | Python | Zapier/Make |
|---------|--------|-------------|
| **Curva aprendizado** | Alta (programação) | Baixa (visual) |
| **Flexibilidade** | 100% (qualquer lógica) | 70% (limitado templates) |
| **Custo** | Grátis | $20-100/mês |
| **Performance** | Rápido (local) | Médio (cloud delays) |
| **Manutenção** | Código (você) | Interface (vendor) |
| **Integrações** | Infinitas (APIs) | 7k apps prontos |
| **Deploy** | Servidor/cron | Cloud automático |

**Usar Python quando:**
- Lógica complexa (loops, condições aninhadas)
- Performance crítica (processar 1M rows)
- Budget limitado (grátis)
- Customização total (APIs proprietárias)

**Usar No-Code quando:**
- Time não-técnico
- Setup rápido (minutos vs horas)
- Integrações padrão (Gmail, Slack, CRM)
- Manutenção simplificada

---

## Deploy Automação Python (Produção)

### Opção 1: Cron (Linux/macOS)

**Setup:**
```bash
# Editar crontab
crontab -e

# Adicionar job (diário 8am)
0 8 * * * /usr/bin/python3 /caminho/script.py

# Logs (debugar erros)
0 8 * * * /usr/bin/python3 /caminho/script.py >> /var/log/automation.log 2>&1
```

### Opção 2: Task Scheduler (Windows)

**Setup:**
1. Abrir Task Scheduler
2. Create Basic Task
3. Trigger: Daily, 8:00 AM
4. Action: Start program
   - Program: `python.exe`
   - Arguments: `C:\scripts\automation.py`

### Opção 3: Docker Container

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY script.py .

CMD ["python", "script.py"]
```

**Deploy:**
```bash
docker build -t automation .
docker run -d --restart always automation
```

### Opção 4: Cloud (AWS Lambda, GCP Functions)

**Serverless** - pagar apenas execução

**Limitações:**
- Timeout max (AWS: 15min)
- RAM limitada
- Cold start latency

---

## Próximos passos

Explore automação com outras ferramentas:

1. **[Zapier](/blog/zapier-automacao-guia-completo-2025/)** - No-code (fácil para não-devs)
2. **[RPA](/blog/rpa-automacao-guia-completo-2025/)** - Desktop automation
3. **[N8N](/blog/n8n-automacao-guia-completo-2025/)** - Open-source workflows
4. **[Automação Processos](/blog/automacao-processos-2025/)** - Business processes
5. **[Selenium Tutorial](/blog/selenium-python-tutorial-2025/)** - Web automation

**Precisa desenvolver automações Python?** A Agência Café Online já criou 200+ scripts para clientes (economia média 25h/semana). [Consultoria grátis](https://agenciacafeonline.com.br).

---

**Sobre o autor:** Felipe Zanoni programa automações Python há 8 anos, com 500+ scripts em produção economizando 10.000+ horas/ano para clientes.
