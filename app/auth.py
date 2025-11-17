from fastapi import Header, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
import os

API_KEY_NAME = "x-api-key"  # header name
# for study only:
API_KEY = os.getenv("API_KEY", "supersecret")
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def get_api_key(api_key: str = Security(api_key_header)):
    """
    Dependency: checks x-api-key header.
    Raises HTTPException 401 if missing or invalid.
    """
    if not api_key:
        raise HTTPException(status_code=401, detail="API key missing")
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key
