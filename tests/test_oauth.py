"""Manual end-to-end OAuth smoke test for SDE-0001.

Usage:
    copy .env.example .env
    # fill in values, then:
    py tests/test_oauth.py

The script prints the Salesforce authorize URL, waits for the authorization
code from the callback, exchanges it for tokens, and runs a smoke SOQL query.
"""

import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from auth_helper import (
    build_authorize_url,
    build_smoke_query,
    exchange_code,
    generate_pkce,
    load_config,
    refresh_access_token,
)


def _load_dotenv(path=".env"):
    """Set environment variables from a simple KEY=VALUE .env file."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key, value)


def main():
    _load_dotenv()
    config = load_config()
    pkce = generate_pkce()

    print("Open this URL in your browser and authorize the Connected App:")
    print(build_authorize_url(config, pkce=pkce))
    print()

    code = input("Paste the authorization code from the callback: ").strip()
    if not code:
        print("No code provided; exiting.")
        return 1

    tokens = exchange_code(config, code, code_verifier=pkce["code_verifier"])
    print("Access token:", tokens.get("access_token")[:20] + "...")
    print("Refresh token:", tokens.get("refresh_token", "")[:20] + "...")

    print("Running refresh token flow...")
    refreshed = refresh_access_token(config, tokens["refresh_token"])
    print("Refreshed access token:", refreshed.get("access_token")[:20] + "...")

    print("Running smoke SOQL query...")
    query = build_smoke_query()
    url = f"{config['login_url'].rstrip('/')}/services/data/v62.0/query"
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    response = requests.get(url, headers=headers, params={"q": query})
    response.raise_for_status()
    data = response.json()
    print("Total records:", data.get("totalSize"))
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
