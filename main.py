import json
from http_requests import get_questions, send_answers

ADDR = '95.31.21.148:7777'
LESSON = 'СТЭКС_2'


def main():
    questions = get_questions(LESSON, ADDR)
    payload = generate_payload(questions)
    jwt = generate_jwt(payload)
    http_payload = json.dumps({"crypted": jwt}).encode('utf-8')
    send_answers(http_payload=http_payload, dest_addr=ADDR)


if __name__ == "__main__":
    main()
