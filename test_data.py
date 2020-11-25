import json

TEST_QUESTIONS = json.loads(
    b'[{"number": 31,"question": "Question_31?","answers": ["First_answer","Second_answer","Third_answer",'
    b'"Fourth_answer"]},{"number": 1,"question": "Question_1?","answers": ["First_answer",'
    b'"Second_answer","Third_answer","Fourth_answer"]},{"number": 21,"question": "Question_21:",'
    b'"answers": ["First_answer","Second_answer","Third_answer","Fourth_answer"]},{"number": 34,'
    b'"question": "Question_34?","answers": ["First_answer","Second_answer","Third_answer",'
    b'"Fourth_answer"]},{"number": 43,"question": "Question_43?","answers": ["First_answer",'
    b'"Second_answer","Third_answer","Fourth_answer"]},{"number": 48,"question": "Question_48?",'
    b'"answers": ["First_answer","Second_answer","Third_answer","Fourth_answer"]},{"number": 55,'
    b'"question": "Question_55?","answers": ["First_answer","Second_answer","Third_answer",'
    b'"Fourth_answer"]},{"number": 7,"question": "Question_7?","answers": ["First_answer",'
    b'"Second_answer","Third_answer","Fourth_answer"]},{"number": 53,"question": "Question_53?",'
    b'"answers": ["First_answer","Second_answer","Third_answer","Fourth_answer"]},{"number": 40,'
    b'"question": "Question_40?","answers": ["First_answer","Second_answer","Third_answer",'
    b'"Fourth_answer"]}]'.decode('utf-8'))

TEST_ANSWERS = [1, 2, 3, 4, 4, 3, 2, 1, 3, 4]

TEST_RESULT = json.loads(b'{"status":true,"result":10}'.decode('utf-8'))
