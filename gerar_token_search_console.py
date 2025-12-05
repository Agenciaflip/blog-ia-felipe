#!/usr/bin/env python3
"""
Gera token OAuth para Google Search Console + Indexing API
Usa credenciais do MCP Google Workspace Flip
"""

from google_auth_oauthlib.flow import InstalledAppFlow
import json

# Scopes necessários
SCOPES = [
    'https://www.googleapis.com/auth/webmasters',  # Search Console
    'https://www.googleapis.com/auth/indexing',    # Indexing API
]

# Client secret do MCP Flip
CLIENT_SECRET_FILE = '/Users/felipezanonimini/Desktop/automacoes/.claude/mcp-google-workspace-flip/client_secret.json'

# Onde salvar token
TOKEN_FILE = '/Users/felipezanonimini/Desktop/automacoes/credentials/search_console_token.json'

def main():
    print("🔐 Gerando token OAuth para Search Console + Indexing API\n")

    # Criar fluxo OAuth
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES
    )

    print("1️⃣ Abrindo navegador para autenticação...")
    print("   (Faça login com contato@agenciaflip.com.br)\n")

    # Executar fluxo (abre navegador)
    creds = flow.run_local_server(port=0)

    print("\n2️⃣ Autenticação concluída!")

    # Salvar token
    token_data = {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }

    with open(TOKEN_FILE, 'w') as f:
        json.dump(token_data, f, indent=2)

    print(f"3️⃣ Token salvo em: {TOKEN_FILE}")
    print("\n✅ Pronto! Agora execute:")
    print("   python3 submeter_search_console.py")

if __name__ == '__main__':
    main()
