# Test Inventory: DFT-0001

## Unit Tests

- [x] `test_build_authorize_url_includes_all_parameters` — `build_authorize_url()` returns a URL with client_id, redirect_uri, response_type, scope, and state.
- [x] `test_exchange_code_returns_tokens_on_success` — `exchange_code()` posts to Salesforce token endpoint and returns access + refresh tokens.
- [x] `test_exchange_code_raises_on_error` — `exchange_code()` raises `SalesforceAuthError` for invalid/expired code.
- [x] `test_refresh_token_returns_new_access_token` — `refresh_access_token()` posts refresh token and returns new access token.
- [x] `test_load_config_missing_variable_raises` — `load_config()` raises if required env var is missing.
- [x] `test_build_soql_smoke_query` — `build_smoke_query()` returns a valid SOQL string.

## Integration Tests

- [ ] `test_oauth_flow_returns_token` — Manual end-to-end via `tests/test_oauth.py` (requires real Salesforce sandbox credentials).
- [ ] `test_smoke_query_returns_records` — Covered by `tests/test_oauth.py` after token exchange.
- [ ] `test_non_admin_user_permission_filter` — Not yet run; requires configured test user in sandbox.

## Error Handling Tests

- [x] `test_invalid_client_secret_raises` — Covered by `test_exchange_code_raises_on_error` (SalesforceAuthError on bad response).
- [x] `test_mismatched_redirect_uri_raises` — Covered by `test_exchange_code_raises_on_error`.

## Pipeline Tests

- [x] No CATS/Karate required (no service or API endpoint in this task).
- [x] Secret-scanning check: ensure `.env.example` contains dummy values and `.env` is in `.gitignore`.

## Implementation Strategy

1. **Foundation**: create `auth_helper.py` with URL builder, token exchange, refresh, and config loading.
2. **Unit tests**: write `test_auth_helper.py` with mocked `requests.post` responses.
3. **Integration script**: create `test_oauth.py` for manual end-to-end verification (real Salesforce sandbox required).
4. **Docs**: add `.env.example`, update `.gitignore`, and document refresh flow.
