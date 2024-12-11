import yaml

with open('message/tmp_messages.yaml', encoding="utf8") as f:
    templates = yaml.safe_load(f)


def get_welcome_messages() -> str:
    return str(templates["welcome_messages"])


def get_question_1() -> str:
    return str(templates["question_1"])


def get_question_2(*, name: str = "") -> str:
    if name is None or name == "":
        return str(templates["question_2_without_name"])
    else:
        return str(templates["question_2_with_name"])


def get_question_3(*, name: str = None) -> str:
    if name is None or name == "":
        return str(templates["question_3_without_name"])
    else:
        return str(templates["question_3_with_name"])


def get_info_about_new_message():
    return str(templates['info_about_new_message'])


def all_answers_get():
    return str(templates['all_answers_get'])
