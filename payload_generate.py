def payload_merge(discipline, group, lesson, replies, student, started, finished, iat):
    payload = {"discipline": discipline,
               "group": group,
               "lessonName": lesson,
               "replies": replies,
               "studentName": student,
               "started": started,
               "finished": finished,
               "iat": iat}
    return payload


def generate_old_defined_payload():
    discipline = "СТЭКС"
    group = "ИУ4-44"
    lesson = "СТЭКС_2"
    replies = [{"questionNumber": 31, "answer": 3},
               {"questionNumber": 1, "answer": 2},
               {"questionNumber": 21, "answer": 2},
               {"questionNumber": 34, "answer": 1},
               {"questionNumber": 43, "answer": 4},
               {"questionNumber": 48, "answer": 3},
               {"questionNumber": 55, "answer": 3},
               {"questionNumber": 7, "answer": 3},
               {"questionNumber": 53, "answer": 1},
               {"questionNumber": 40, "answer": 4}]
    student = "5"
    started = "2020-11-20T14:59:07.296Z"
    finished = "2020-11-20T15:15:29.042Z"
    iat = 1605874529

    old_defined_payload = payload_merge(discipline, group, lesson, replies, student, started, finished, iat)
    return old_defined_payload
