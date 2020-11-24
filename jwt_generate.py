from authlib.jose import jwt

SECRET = 'shhhhh'


def generate_jwt(payload):
    return jwt.encode({"alg": "HS256"}, payload, SECRET).decode('utf-8')
