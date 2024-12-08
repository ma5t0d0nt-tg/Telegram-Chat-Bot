"""
Парсер скрипта для получения данных из конфигурационного файла
для управления чат-ботом бизнес аккаунта
"""

import configparser
import asyncio

conf = configparser.ConfigParser()
conf.read('config/config.ini')


def get_active_business() -> str:
    """
    Функция для получения статуса работы бота
    :return: dict: is_active_bot - текущий статус работы бота
    """
    return str(conf['ACTIVE_CHAT_BOT']['is_active_business'])


def set_active_business() -> None:
    """
    Функция для установки статуса работы телеграмм бота для бизнес-аккаунта
    :return: dict
    """
    conf.set('ACTIVE_CHAT_BOT', 'is_active_business', '1')
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None


def set_inactive_business() -> None:
    """
    Функция для установки статуса работы телеграмм бота для бизнес-аккаунта
    :return: dict
    """
    conf.set('ACTIVE_CHAT_BOT', 'is_active_business', '0')
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None
