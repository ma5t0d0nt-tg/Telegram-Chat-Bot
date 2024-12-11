import pprint

from aiogram import F, Router
from aiogram.types import Message, TelegramObject, ChatFullInfo, BotCommand, ReactionTypeEmoji
from aiogram.filters import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode

import configparser

from typing import Callable
import sys
import json

from config.parser_config_admin import (get_status_bot, set_active_bot,
                                        set_inactive_bot, get_owner_user_id)

router = Router()


def check_user(user_id_message: int) -> bool:
    """
    Функция для проверки доступа к управлению ботом и его настройками
    :param user_id_message: int user_id пользователя, который пишет боту
    :return: true - дается доступ к функциям бота, false - запрет
    """
    user_id_owner = get_owner_user_id()
    return user_id_message == user_id_owner


@router.message(Command("act_bot"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_active_bot()
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text="Бот включен")


@router.message(Command("dis_bot"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_inactive_bot()
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text="Бот отключен")


@router.message(Command("get_status_bot"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        current_status = int(get_status_bot())
        if current_status == 0:
            await message.reply(text="Бот отключен")
            emoji_got_it = ReactionTypeEmoji(emoji='😴')
            await message.react(reaction=[emoji_got_it])
        elif current_status == 1:
            await message.reply(text="Бот работает")
            emoji_got_it = ReactionTypeEmoji(emoji='👨‍💻')
            await message.react(reaction=[emoji_got_it])


@router.message(Command("get_config"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        conf = configparser.ConfigParser()
        conf.read('config/config.ini')
        str_f = (f"[ACTIVE_BOT]:\n"
                 f"is_active_bot: {conf['ACTIVE_BOT']['is_active_bot']}\n\n"
                 f"[ACTIVE_CHAT_BOT]:\n"
                 f"is_active_business: {conf['ACTIVE_CHAT_BOT']['is_active_business']}")
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react(reaction=[emoji_got_it])
        await message.reply(text=str_f, parse_mode=ParseMode.HTML)


@router.message(Command("cmd_bot"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        str_f_cmd = (f"***Список команд для администрирования бота***:\n\n"
                     f"/act_bot - активация бота;\n"
                     f"/dis_bot - деактивация бота;\n"
                     f"/get_status_bot - получить текущий статус бота;\n"
                     f"/get_config - получить размер файла базы данных;")
        await message.reply(text=str_f_cmd, parse_mode=ParseMode.MARKDOWN)
