from termcolor import colored
from config import COURSE, LESSON, INTERCEPTED_HTTP_PAYLOAD, SECRET, BRUTEFORCE_TIMES
from jwt_generate import check_secret
from bf_answers import bf_answers_n_times


def main():
    if check_secret(INTERCEPTED_HTTP_PAYLOAD, SECRET):
        bf_answers_n_times(BRUTEFORCE_TIMES, COURSE, LESSON)
    else:
        print(colored(f'WARNING, WRONG SECRET!!!\n   SECRET: {SECRET}', 'red'))


if __name__ == "__main__":
    main()
