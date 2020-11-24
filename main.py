import json
from http_requests import get_questions, send_answers
from payload_generate import generate_test_payload
from jwt_generate import generate_jwt

ADDR = '95.31.21.148:7777'
LESSON = 'СТЭКС_2'


def main():
    questions = get_questions(LESSON, ADDR)
    # payload = generate_payload(questions)
    payload = generate_test_payload()
    jwt = generate_jwt(payload)
    http_payload = json.dumps({"crypted": jwt}).replace(" ", "").encode('utf-8')
    send_answers(http_payload=http_payload, dest_addr=ADDR)


if __name__ == "__main__":
    main()
