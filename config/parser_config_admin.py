"""
Парсер скрипта для получения данных из конфигурационного файла
для управления ботом владельцем телеграмм-бота
"""

import configparser
import asyncio

conf = configparser.ConfigParser()
conf.read('config/config.ini')


def get_status_bot() -> str:
    """
    Функция для получения статуса работы бота
    :return: dict: is_active_bot - текущий статус работы бота
    """
    return str(conf['ACTIVE_BOT']['is_active_bot'])


def set_active_bot() -> None:
    """
    Функция для включения работы телеграмм бота
    :return: dict
    """
    conf.set('ACTIVE_BOT', 'is_active_bot', '1')
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None


def set_inactive_bot():
    """
    Функция для отключения работы телеграмм бота
    :return: dict
    """
    conf.set('ACTIVE_BOT', 'is_active_bot', '0')
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None
