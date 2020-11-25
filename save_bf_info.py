import csv
import io
import operator
from pathlib import Path

from typing import List, Tuple


def sort_bf_csv(path):
    f_csv = csv.reader(open(path, 'r'), delimiter=",")
    list_csv = list(f_csv)
    for i in range(len(list_csv)):
        list_csv[i][0] = int(list_csv[i][0])
    list_csv_sorted = sorted(list_csv, key=operator.itemgetter(0))
    f_csv = csv.writer(open(path, 'w'), delimiter=",")
    f_csv.writerows(list_csv_sorted)


def write_bf_file(path: str, updated_info: List[str]):
    with io.open(path, 'w', encoding='utf8') as f:
        s_updated_info = ''.join(updated_info)
        f.write(s_updated_info)


def update_info(old_info, new_info) -> Tuple[List[str], List[str]]:
    updated_info = set(old_info) | set(new_info)
    unique_new_info = set(new_info) - set(old_info)
    updated_info = list(updated_info)
    unique_new_info = list(unique_new_info)
    return updated_info, unique_new_info


def create_new_info(questions: list, answers: list) -> List[str]:
    new_info = [
        f'{questions[i]["number"]},{answers[i]},{questions[i]["question"]},{questions[i]["answers"][answers[i] - 1]}\n'
        for i in range(len(questions))]
    return new_info


def open_read_bf_file(path: str) -> List[str]:
    if check_bf_file_exists(path):
        with io.open(path, 'r', encoding='utf8') as f:
            old_info = f.readlines()
    else:
        with io.open(path, 'x', encoding='utf8') as f:
            old_info = f.readlines()
    return old_info


def check_bf_file_exists(path: str) -> bool:
    bf_file = Path(path)
    if bf_file.is_file():
        return True
    else:
        return False


def save_bf_info(path: str, questions: list, answers: list) -> List[str]:
    # read old info
    old_info = open_read_bf_file(path)
    # create new info from questions & answers
    new_info = create_new_info(questions, answers)
    # add new unique lines to old info
    updated_info, unique_new_info = update_info(old_info, new_info)
    # write updated info
    write_bf_file(path, updated_info)
    # sort final .csv
    sort_bf_csv(path)
    return unique_new_info
