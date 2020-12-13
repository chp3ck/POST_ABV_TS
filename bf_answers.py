import random

from termcolor import colored

from http_requests import send_answers, get_questions
from config import SECRET, ADDR, GROUP, BF_FILE_PATH
from payload_generate import generate_http_payload
from save_bf_info import save_bf_info


def get_answers(discipline: str, lesson: str, questions: list, group: str = GROUP):
    # get question number for loop
    question_number = len(questions)
    # initialize answers pool
    answers = [random.randint(1, 4) for _ in range(question_number)]
    # create & send http payload with initial answers pool
    http_payload = generate_http_payload(discipline, group, lesson, questions, answers, SECRET)
    response = send_answers(http_payload, ADDR)
    # check response status

    if response['status'] is True and 'result' in response:
        # initialize number of correct answers
        result = response['result']
        if result == 10:
            return answers
        new_result = result

        # main loop, sequential answers bruteforce
        for i in range(question_number):
            # while result is equal next result -> increment & check
            while result == new_result:
                # increment current answer value
                answers[i] += 1
                # create & send new http payload with updated answers pool
                http_payload = generate_http_payload(discipline, group, lesson, questions, answers, SECRET)
                response = send_answers(http_payload, ADDR)
                # check response status
                if response['status'] is True:
                    # get new result value
                    new_result = response['result']
                else:
                    print(colored(f'WARNING, WRONG HTTP ANSWERS RESPONSE STATUS: {response["status"]}!!!', 'red'))
                    return
            if new_result > result:
                if new_result == 10:
                    return answers
                result = new_result
            elif new_result < result:
                answers[i] -= 1
                new_result = result
            else:
                print(colored(f'WARNING, UNEXPECTED RESULTS: result: {result}, new result: {new_result}!!!', 'red'))
                return

        if result == 10:
            return answers
        else:
            print(colored(f'WARNING, UNEXPECTED RESPONSE RESULT: {response["result"]}!!!', 'red'))
            return
    else:
        is_result = 'result' in response
        print(colored(f'WARNING, WRONG HTTP ANSWERS RESPONSE:'
                      f' status -> {response["status"]},'
                      f' result -> {is_result}!!!', 'red'))
        return


def bf_answers(course: str, lesson: str):
    questions = get_questions(lesson)
    if questions is None:
        return
    answers = get_answers(course, lesson, questions)
    if answers is None:
        return
    return save_bf_info(BF_FILE_PATH, questions, answers)


def bf_answers_n_times(n: int, course: str, lesson: str):
    for i in range(n):
        new_info = bf_answers(course, lesson)
        if not new_info:
            print(colored(f'New answers not bruteforced, check link, request or {BF_FILE_PATH}...', 'yellow'))
            break
        else:
            print(colored('New answers added:', 'green'))
            print('----№Q----№A--Question text--Question answer')
            for line in new_info:
                print(colored(f'    {line.replace(",", "    ")}', 'green'))
    print(colored(f'Finished bruteforced answers {n} times', 'green'))
