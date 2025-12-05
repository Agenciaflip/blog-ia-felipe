#!/usr/bin/env python3
"""
Script para submeter sitemap e URLs no Google Search Console
Usa credenciais do MCP Google Workspace Flip
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import sys

# Credenciais do MCP Flip
CLIENT_SECRET_PATH = "/Users/felipezanonimini/Desktop/automacoes/.claude/mcp-google-workspace-flip/client_secret.json"

# Site
SITE_URL = "https://blog.agenciacafeonline.com.br"
SITEMAP_URL = f"{SITE_URL}/sitemap-index.xml"

# URLs dos 15 artigos
ARTIGOS = [
    "/blog/chatbot-whatsapp-guia-completo-2025/",
    "/blog/automacao-whatsapp-2025/",
    "/blog/crm-vendas-guia-completo-2025/",
    "/blog/api-whatsapp-guia-completo/",
    "/blog/evolution-api-tutorial-completo/",
    "/blog/pipedrive-guia-completo-2025/",
    "/blog/flask-python-tutorial-2025/",
    "/blog/docker-tutorial-completo-2025/",
    "/blog/chatbot-gratuito-2025/",
    "/blog/whatsapp-bot-2025/",
    "/blog/crm-gratuito-2025/",
    "/blog/api-openai-python-2025/",
    "/blog/chatbot-ia-2025/",
    "/blog/funil-de-vendas-2025/",
    "/blog/gpt-4-api-2025/",
]

def get_credentials():
    """Carrega credenciais OAuth do MCP"""
    try:
        # Tentar token salvo primeiro
        token_path = "/Users/felipezanonimini/Desktop/automacoes/credentials/search_console_token.json"

        try:
            with open(token_path, 'r') as f:
                creds_data = json.load(f)

            creds = Credentials(
                token=creds_data.get('token'),
                refresh_token=creds_data.get('refresh_token'),
                token_uri=creds_data.get('token_uri'),
                client_id=creds_data.get('client_id'),
                client_secret=creds_data.get('client_secret'),
                scopes=creds_data.get('scopes')
            )

            return creds
        except FileNotFoundError:
            print("⚠️ Token não encontrado. Execute primeiro:")
            print("python3 gerar_token_search_console.py")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Erro ao carregar credenciais: {e}")
        sys.exit(1)

def submeter_sitemap(service, site_url, sitemap_url):
    """Submete sitemap no Search Console"""
    try:
        request = service.sitemaps().submit(
            siteUrl=site_url,
            feedpath=sitemap_url
        )
        request.execute()
        print(f"✅ Sitemap submetido: {sitemap_url}")
        return True
    except HttpError as e:
        if e.resp.status == 404:
            print(f"⚠️ Site não verificado no Search Console: {site_url}")
            print("   Primeiro adicione e verifique o site em: https://search.google.com/search-console")
        else:
            print(f"❌ Erro ao submeter sitemap: {e}")
        return False

def solicitar_indexacao(service, url):
    """Solicita indexação de URL específica via Indexing API"""
    try:
        indexing_service = build('indexing', 'v3', credentials=service._http.credentials)

        request_body = {
            'url': url,
            'type': 'URL_UPDATED'
        }

        request = indexing_service.urlNotifications().publish(body=request_body)
        response = request.execute()

        print(f"✅ Indexação solicitada: {url}")
        return True
    except HttpError as e:
        if e.resp.status == 403:
            print(f"⚠️ Indexing API não habilitada. Habilite em:")
            print("   https://console.cloud.google.com/apis/library/indexing.googleapis.com")
        else:
            print(f"❌ Erro: {e}")
        return False

def main():
    print("🔍 Google Search Console - Submeter Sitemap e URLs\n")

    # Carregar credenciais
    print("1️⃣ Carregando credenciais...")
    creds = get_credentials()

    # Conectar ao Search Console
    print("2️⃣ Conectando ao Search Console...")
    try:
        service = build('searchconsole', 'v1', credentials=creds)
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        sys.exit(1)

    # Submeter sitemap
    print(f"\n3️⃣ Submetendo sitemap...")
    sitemap_ok = submeter_sitemap(service, SITE_URL, SITEMAP_URL)

    if not sitemap_ok:
        print("\n⚠️ Não foi possível submeter sitemap.")
        print("   Verifique se o site está adicionado no Search Console primeiro.")
        return

    # Solicitar indexação dos artigos
    print(f"\n4️⃣ Solicitando indexação de {len(ARTIGOS)} artigos...")

    sucessos = 0
    erros = 0

    for artigo in ARTIGOS:
        url_completa = f"{SITE_URL}{artigo}"

        if solicitar_indexacao(service, url_completa):
            sucessos += 1
        else:
            erros += 1

    # Resumo
    print(f"\n📊 RESUMO:")
    print(f"✅ Sitemap: {'Submetido' if sitemap_ok else 'Falhou'}")
    print(f"✅ URLs indexadas: {sucessos}/{len(ARTIGOS)}")
    if erros > 0:
        print(f"❌ Erros: {erros}")

    print(f"\n🌐 Acompanhe em: https://search.google.com/search-console?resource_id={SITE_URL}")

if __name__ == '__main__':
    main()
