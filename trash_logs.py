from termcolor import colored

from config import ADDR
from http_requests import get_questions, send_answers
from payload_generate import generate_http_payload_logs


def send_multiple_times(num: int, discipline, group, lesson, answers, secret, student):
    for i in range(0, num):
        send_one_time(discipline, group, lesson, answers, secret, student)
        print(colored(f'    log packet №: {i+1}', 'green'))


def send_one_time(discipline, group, lesson, answers, secret, student):
    questions = get_questions(lesson)
    http_payload = generate_http_payload_logs(discipline, group, lesson, questions, answers, secret, student)
    response = send_answers(http_payload, ADDR)
    if response['status'] is not True:
        print(colored(f'WARNING, WRONG HTTP ANSWERS RESPONSE STATUS: {response["status"]}!!!', 'red'))
        return
