from typing import Optional

from chalicelib.core.config import settings


def cafe24_key_authorize(token: str) -> Optional[str]:
    """API Key Authorizer

    Args:
        token (str): API Token

    Returns:
        Optional[str]: If Token is exists in Token List return Token, else will return Null
    """

    # FIXME(Dohyung): Should move to Database like DynamoDB
    store = {
        settings.MEDITHERAPHY_CAFE24_WEBHOOK_KEY: {
            "tenant": "meditheraphy",
            "token": settings.MEDITHERAPHY_CAFE24_WEBHOOK_KEY,
        }
    }
    if store.get(token):
        return store[token]
    return None
