import yaml

with open('message/tmp_messages.yaml', encoding="utf8") as f:
    templates = yaml.safe_load(f)


def get_welcome_messages() -> str:
    return str(templates["welcome_messages"])


def get_question(index: int) -> str:
    return str(templates[f"question_{index}"])


def get_info_about_new_message():
    return str(templates['info_about_new_message'])


def all_answers_get():
    return str(templates['all_answers_get'])


def get_cmd():
    return str(templates['cmd'])

