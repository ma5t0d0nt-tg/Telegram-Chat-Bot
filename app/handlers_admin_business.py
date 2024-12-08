import types

from aiogram import F, Router
from aiogram.types import Message, TelegramObject, ChatFullInfo, BotCommand, ReactionTypeEmoji, FSInputFile, \
    CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.enums.parse_mode import ParseMode

import configparser

from typing import Callable
import sys
import os
import json

from config.parser_config_business import get_active_business, set_active_business, set_inactive_business
from config.parser_config_admin import get_owner_user_id
from sqlite import db_start, get_all_record, get_all_chats, delete_message, delete_all_message, db_stop

router = Router()


def check_user(user_id_message: int) -> bool:
    """
    Функция для проверки доступа к управлению ботом и его настройками
    :param user_id_message: int user_id пользователя, который пишет боту
    :return: true - дается доступ к функциям бота, false - запрет
    """
    user_id_owner = get_owner_user_id()
    return user_id_message == user_id_owner


@router.message(Command(commands=["act_bus"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_active_business()
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react([emoji_got_it])
        await message.reply(text="Чат-бот включен")


@router.message(Command(commands=["dis_bus"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_inactive_business()
        emoji_got_it = ReactionTypeEmoji(emoji='👍')
        await message.react([emoji_got_it])
        await message.reply(text="Чат-бот отключен")


@router.message(Command(commands=["get_status_bus"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        current_status = int(get_active_business())
        if current_status == 0:
            await message.reply(text="Чат-бот отключен")
            emoji_got_it = ReactionTypeEmoji(emoji='😴')
            await message.react([emoji_got_it])
        elif current_status == 1:
            await message.reply(text="Чат-бот работает")
            emoji_got_it = ReactionTypeEmoji(emoji='👨‍💻')
            await message.react([emoji_got_it])


@router.message(Command(commands=["get_file_db_size"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        file_size_byte = os.path.getsize("messages.db")
        file_size_kbyte = file_size_byte / 1024
        await message.reply(f"Размер файла с базой данных: {file_size_kbyte} КБ")


@router.message(Command(commands=["get_count_record"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        count = await get_all_record()
        await message.reply(f"Количество записей в базе данных: {count[0][0]}")


@router.message(Command(commands=["get_all_chats"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        chats = await get_all_chats()
        for chat in chats:
            await message.reply(text=f"id: {chat[0]}\nuser_id: {chat[1]}\n"
                                     f"num_question: {chat[2]}\nanswer: {chat[3]}\n")
        await db_stop()


@router.message(F.text.startswith("del"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        id_msg = message.text.split(" ")[1].strip()
        await db_start()
        await delete_message(id_message=id_msg)
        await message.reply(f"Сообщение с id = {id_msg} удалено")
        await db_stop()


@router.message(Command(commands=["del_all"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        await delete_all_message()
        await message.reply("Все собщения удалены из базы данных")
        await db_stop()


@router.message(Command(commands=["cmd_bus"], prefix="."))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        str_f_cmd = (f"<u>Список команд для администрирования чат-бота</u>:\n\n"
                     f"<b>act_bus</b> - активация чат-бота;\n"
                     f"<b>dis_bus</b> - деактивация чат-бота;\n"
                     f"<b>get_status_bus</b> - получить текущий статус чат-бота;\n"
                     f"<b>get_file_db_size</b> - получить размер файла базы данных чат-бота;\n"
                     f"<b>get_count_record</b> - получить количество записей в базе от чат-бота;\n"
                     f"<b>get_all_chats</b> - получить все чаты от чат-бота;\n"
                     f"<b>get_file_db</b> - получить файл базы данных;\n"
                     f"<b>del Х</b> - удалить еденичную запись в таблице;\n"
                     f"<b>del_all</b> - удалить все записи в таблице;")
        await message.reply(text=str_f_cmd, parse_mode=ParseMode.HTML)
