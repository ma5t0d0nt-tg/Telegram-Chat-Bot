from dotenv import load_dotenv
import os


def check_user(user_id_message: int) -> bool:
    """
    Функция для проверки доступа к управлению ботом и его настройками
    :param user_id_message: int user_id пользователя, который пишет боту
    :return: true - дается доступ к функциям бота, false - запрет
    """
    load_dotenv()
    return str(user_id_message) == os.getenv("USER_ID")
