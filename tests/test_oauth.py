"""Automated end-to-end OAuth smoke test for SDE-0001.

Usage:
    copy .env.example .env
    # fill in values, then:
    py tests/test_oauth.py

The script starts a local callback server, prints the Salesforce authorize URL,
waits for the browser to redirect back, exchanges the code for tokens, and runs
a smoke SOQL query.
"""

import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

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


class _CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/auth/callback":
            query = parse_qs(parsed.query)
            self.server.auth_code = query.get("code", [None])[0]
            self.server.event.set()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authorization successful. You may close this tab.")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def _start_callback_server():
    HTTPServer.allow_reuse_address = True
    server = HTTPServer(("localhost", 8000), _CallbackHandler)
    server.event = threading.Event()
    server.auth_code = None
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def main():
    _load_dotenv()
    config = load_config()
    pkce = generate_pkce()

    server, thread = _start_callback_server()

    print("Open this URL in your browser and authorize the Connected App:")
    print(build_authorize_url(config, pkce=pkce))
    print()
    print("Waiting for callback on http://localhost:8000/auth/callback ...")

    server.event.wait()
    server.shutdown()
    thread.join()

    code = server.auth_code
    if not code:
        print("No authorization code received; exiting.")
        return 1

    tokens = exchange_code(config, code, code_verifier=pkce["code_verifier"])
    instance_url = tokens.get("instance_url", config["login_url"]).rstrip("/")
    print("Instance URL:", instance_url)
    print("Access token:", tokens.get("access_token")[:20] + "...")
    print("Refresh token:", tokens.get("refresh_token", "")[:20] + "...")

    print("Running refresh token flow...")
    refreshed = refresh_access_token(config, tokens["refresh_token"])
    print("Refreshed access token:", refreshed.get("access_token")[:20] + "...")

    print("Running smoke SOQL query...")
    query = build_smoke_query()
    url = f"{instance_url}/services/data/v62.0/query"
    access_token = refreshed.get("access_token", tokens["access_token"])
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers, params={"q": query})
    if not response.ok:
        print("SOQL query failed:", response.status_code, response.text)
        return 1
    data = response.json()
    print("Total records:", data.get("totalSize"))
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
