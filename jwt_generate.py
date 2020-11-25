import json

import authlib
from authlib.jose import jwt


def check_secret(http_payload: str, secret: str):
    intercepted_jwt = json.loads(http_payload)["crypted"]
    return is_secret_valid(intercepted_jwt, secret)


def is_secret_valid(intercepted_jwt: str, secret: str) -> bool:
    try:
        jwt.decode(intercepted_jwt, secret)
        return True
    except authlib.jose.errors.BadSignatureError:
        return False


def generate_jwt(payload: dict, secret: str) -> bytes:
    return jwt.encode({"alg": "HS256"}, payload, secret).decode('utf-8')
