#!/usr/bin/env python3
"""
Autenticazione OAuth2 per Google Search Console
Esegui questo script UNA SOLA VOLTA per ottenere il token di accesso.
Il token viene salvato in .agent/credentials/gsc-token.json e si rinnova automaticamente.

Requisiti:
    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

Usage:
    python gsc_auth.py --client-secret <path-to-client-secret.json>
"""

import argparse
import json
import os
import sys

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
TOKEN_PATH = os.path.join(os.path.dirname(__file__), "gsc-token.json")


def main():
    if not HAS_DEPS:
        print("Installa le dipendenze:")
        print("  pip install google-api-python-client google-auth-oauthlib google-auth-httplib2")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Setup OAuth2 per Google Search Console")
    parser.add_argument("--client-secret", required=True,
                        help="Percorso al file client_secret_*.json scaricato da Google Cloud")
    args = parser.parse_args()

    creds = None

    # Controlla se esiste già un token valido
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("Token rinnovato automaticamente.")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(args.client_secret, SCOPES)
            # Porta fissa 8080 — assicurati che sia libera
            creds = flow.run_local_server(port=8080, open_browser=True, timeout_seconds=120)
            print("\n✅ Autenticazione completata!")

        # Salva il token per usi futuri
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
        print(f"Token salvato in: {TOKEN_PATH}")

    print("\n✅ Credenziali valide. Puoi ora usare gsc_checker_oauth.py")


if __name__ == "__main__":
    main()
