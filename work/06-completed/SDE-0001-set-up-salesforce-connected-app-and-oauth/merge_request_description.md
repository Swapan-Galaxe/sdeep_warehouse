# SDE-0001 - Set up Salesforce Connected App and OAuth

## 🎯 Purpose

Create and configure the Salesforce Connected App OAuth helper for the Sales Intelligence Assistant, enabling authenticated access for downstream data retrieval.

## 🚀 Implementation

- Added `auth_helper.py` with `load_config`, `build_authorize_url`, `exchange_code`, `refresh_access_token`, `build_smoke_query`, and `SalesforceAuthError`.
- Added `tests/test_auth_helper.py` with 6 unit tests using mocked `requests` responses.
- Added `tests/test_oauth.py` for manual end-to-end sandbox validation.
- Added `.env.example` and `.gitignore` to keep credentials out of version control.

## ✅ Verification

1. 🧪 **Run unit tests**

```powershell
py -m pytest -v
# Expected: 6 passed
```

2. ▶️ **Run manual end-to-end OAuth flow**

```powershell
copy .env.example .env
# Fill in real sandbox credentials, then:
py tests/test_oauth.py
# Expected: Authorization URL printed, then token exchange, refresh, and SOQL smoke query results
```

3. ✅ **Validate secret scanning**

```powershell
# Confirm .env is not tracked and .env.example only contains dummy values
git ls-files | findstr .env
# Expected: no output for .env
```
