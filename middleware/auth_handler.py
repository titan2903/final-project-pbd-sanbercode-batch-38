import time
from typing import Dict

import jwt
from decouple import config

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")

def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def signJWT(customer_id: str) -> Dict[str, str]:
    payload = {
        "user_id": customer_id,
        "expires": time.time() + 100000
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def get_current_user(jwtoken: str) -> str:
        userId: int = 0
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            userId = payload['user_id']
        return userId