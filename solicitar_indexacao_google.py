#!/usr/bin/env python3
"""
Solicita indexação Google Search Console para os 15 novos artigos do blog.
"""
import json
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Credentials Search Console
SERVICE_ACCOUNT_FILE = '/Users/felipezanonimini/Desktop/automacoes/credentials/search_console_token.json'
SCOPES = ['https://www.googleapis.com/auth/indexing']

# URLs dos 15 novos artigos
URLS_NOVOS_ARTIGOS = [
    # Artigos 6-15 (continuação dos 5 anteriores)
    "https://blog.agenciacafeonline.com.br/blog/ferramentas-ia-2025/",
    "https://blog.agenciacafeonline.com.br/blog/automacao-marketing-2025/",
    "https://blog.agenciacafeonline.com.br/blog/ia-para-criar-anuncios-2025/",
    "https://blog.agenciacafeonline.com.br/blog/seo-ia-2025/",
    "https://blog.agenciacafeonline.com.br/blog/rpa-automacao-guia-completo-2025/",
    "https://blog.agenciacafeonline.com.br/blog/make-automacao-2025/",
    "https://blog.agenciacafeonline.com.br/blog/n8n-automacao-guia-completo-2025/",
    "https://blog.agenciacafeonline.com.br/blog/chatbot-whatsapp-gratis-2025/",
    "https://blog.agenciacafeonline.com.br/blog/copywriting-ia-2025/",
    "https://blog.agenciacafeonline.com.br/blog/marketing-digital-ia-2025/",
]

def solicitar_indexacao():
    """Solicita indexação de todos os artigos novos."""
    print("\n🔍 Iniciando solicitação indexação Google Search Console...")
    print(f"Total URLs: {len(URLS_NOVOS_ARTIGOS)}\n")
    
    # Autenticar
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    
    service = build('indexing', 'v3', credentials=credentials)
    
    sucesso = 0
    erros = 0
    
    for i, url in enumerate(URLS_NOVOS_ARTIGOS, 1):
        try:
            body = {
                "url": url,
                "type": "URL_UPDATED"
            }
            
            response = service.urlNotifications().publish(body=body).execute()
            print(f"✅ {i}/{len(URLS_NOVOS_ARTIGOS)} - {url.split('/')[-2]}")
            sucesso += 1
            
            # Rate limit (200 requests/min)
            time.sleep(0.5)
            
        except Exception as e:
            print(f"❌ {i}/{len(URLS_NOVOS_ARTIGOS)} - ERRO: {url}")
            print(f"   Motivo: {str(e)}\n")
            erros += 1
    
    print(f"\n📊 RESULTADO:")
    print(f"✅ Sucesso: {sucesso}/{len(URLS_NOVOS_ARTIGOS)}")
    print(f"❌ Erros: {erros}/{len(URLS_NOVOS_ARTIGOS)}")
    print(f"\n✨ Google Search Console vai processar nos próximos dias.")
    print(f"📈 Verifique em: https://search.google.com/search-console\n")

if __name__ == "__main__":
    solicitar_indexacao()
