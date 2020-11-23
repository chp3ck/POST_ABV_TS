from authlib.jose import jwt
from payload_generate import generate_old_defined_payload

JWT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaXNjaXBsaW5lIjoi0KHQotCt0JrQoSIsImdyb3VwIjoi0JjQo' \
      'zQtNDQiLCJsZXNzb25OYW1lIjoi0KHQotCt0JrQoV8yIiwicmVwbGllcyI6W3sicXVlc3Rpb25OdW1iZXIiOjMxLCJ' \
      'hbnN3ZXIiOjN9LHsicXVlc3Rpb25OdW1iZXIiOjEsImFuc3dlciI6Mn0seyJxdWVzdGlvbk51bWJlciI6MjEsImFuc' \
      '3dlciI6Mn0seyJxdWVzdGlvbk51bWJlciI6MzQsImFuc3dlciI6MX0seyJxdWVzdGlvbk51bWJlciI6NDMsImFuc3d' \
      'lciI6NH0seyJxdWVzdGlvbk51bWJlciI6NDgsImFuc3dlciI6M30seyJxdWVzdGlvbk51bWJlciI6NTUsImFuc3dlc' \
      'iI6M30seyJxdWVzdGlvbk51bWJlciI6NywiYW5zd2VyIjozfSx7InF1ZXN0aW9uTnVtYmVyIjo1MywiYW5zd2VyIjo' \
      'xfSx7InF1ZXN0aW9uTnVtYmVyIjo0MCwiYW5zd2VyIjo0fV0sInN0dWRlbnROYW1lIjoiNSIsInN0YXJ0ZWQiOiIyM' \
      'DIwLTExLTIwVDE0OjU5OjA3LjI5NloiLCJmaW5pc2hlZCI6IjIwMjAtMTEtMjBUMTU6MTU6MjkuMDQyWiIsImlhdCI' \
      '6MTYwNTg3NDUyOX0.Z6YvxglOQKfHyD_VBo51OSSZfqIaUqg13jnoD-1gc6s'
SECRET = 'abv_ts'


def generate_jwt_hs256(payload, secret):
    return jwt.encode({"alg": "HS256"}, payload, secret)


def test_jwt():
    raw_jwt = generate_jwt_hs256(generate_old_defined_payload(), SECRET)
    print(raw_jwt.decode().split('.'))
    claims_jwt = jwt.decode(raw_jwt, 'secret_so_secret')
    print(claims_jwt)
