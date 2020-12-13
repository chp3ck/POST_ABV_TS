import datetime
import json
import random
from typing import Tuple

import pytz as pytz

from config import LOGS_QUESTIONS
from jwt_generate import generate_jwt
from student_names import STUDENT_NAMES


def payload_merge(discipline: str, group: str, lesson: str, replies: list, student: str, started: str, finished: str,
                  iat: int) -> dict:
    payload = {"discipline": discipline,
               "group": group,
               "lessonName": lesson,
               "replies": replies,
               "studentName": student,
               "started": started,
               "finished": finished,
               "iat": iat}
    return payload


def generate_replies(questions: list, answers: list) -> list:
    question_numbers = [questions[_]['number'] for _ in range(len(questions))]
    question_numbers = LOGS_QUESTIONS
    return [{"questionNumber": question_numbers[_], "answer": answers[_]} for _ in range(len(question_numbers))]


def generate_ts() -> Tuple[str, str, int]:
    ts = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    iat = int(ts.timestamp())
    finished = str(ts).replace(' ', 'T').split('+')[0]
    finished = f'{finished[:-3]}Z'
    delta_minutes_base = - (27 * 60)
    delta_minutes_offset = - random.randint(0, int(14.1 * 60)) + random.randint(0, int(6.7 * 60))
    delta_milliseconds_offset = - 0.001 * random.randint(0, 1000) + 0.001 * random.randint(0, int(1000))
    started = ts.timestamp() + delta_minutes_base + delta_minutes_offset + delta_milliseconds_offset
    started = f'{datetime.datetime.fromtimestamp(started)}'.replace(' ', 'T').split('+')[0]
    started = f'{started[:-3]}Z'
    return started, finished, iat


def generate_student() -> str:
    return random.choice(STUDENT_NAMES)


def generate_payload(discipline: str, group: str, lesson: str, questions: list, answers: list) -> dict:
    replies = generate_replies(questions, answers)
    student = generate_student()
    started, finished, iat = generate_ts()
    return payload_merge(discipline, group, lesson, replies, student, started, finished, iat)


def generate_http_payload(discipline: str, group: str, lesson: str, questions: list, answers: list,
                          secret: str) -> bytes:
    payload = generate_payload(discipline, group, lesson, questions, answers)
    jwt = generate_jwt(payload, secret)
    return json.dumps({"crypted": jwt}).replace(" ", "").encode('utf-8')


def generate_payload_logs(discipline: str, group: str, lesson: str, questions: list, answers: list,
                          student: str) -> dict:
    replies = generate_replies(questions, answers)
    started, finished, iat = generate_ts()
    return payload_merge(discipline, group, lesson, replies, student, started, finished, iat)


def generate_http_payload_logs(discipline: str, group: str, lesson: str, questions: list, answers: list,
                               secret: str, student: str) -> bytes:
    payload = generate_payload_logs(discipline, group, lesson, questions, answers, student)
    jwt = generate_jwt(payload, secret)
    return json.dumps({"crypted": jwt}).replace(" ", "").encode('utf-8')
