from aiogram import F, Router
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import os

from config.parser_config_business import get_active_business, set_active_business, set_inactive_business
from config.parser_config_admin import get_owner_user_id
from db.sqlite import db_start, get_count_record, get_all_chats, delete_message, delete_all_message, db_stop

router = Router()


def __check_user(user_id_message: int) -> bool:
    """
    Функция для проверки доступа к управлению ботом и его настройками
    :param user_id_message: int user_id пользователя, который пишет боту
    :return: true - дается доступ к функциям бота, false - запрет
    """
    user_id_owner = get_owner_user_id()
    return user_id_message == user_id_owner


@router.message(Command("act_bus"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_active_business()
        await message.reply(text="Чат-бот включен")


@router.message(Command("dis_bus"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_inactive_business()
        await message.reply(text="Чат-бот отключен")


@router.message(Command("get_status_bus"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        current_status = int(get_active_business())
        if current_status == 0:
            await message.reply(text="Чат-бот отключен")
        elif current_status == 1:
            await message.reply(text="Чат-бот работает")


@router.message(Command("get_file_db_size"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        file_size_byte = os.path.getsize("messages.db")
        file_size_kbyte = file_size_byte / 1024
        await message.reply(f"Размер файла с базой данных: {file_size_kbyte} КБ")


@router.message(Command("get_count_record"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        count = await get_count_record()
        await db_stop()
        await message.reply(f"Количество записей в базе данных: {count[0][0]}")


@router.message(Command("get_all_chats"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        chats = await get_all_chats()
        await db_stop()
        for chat in chats:
            await message.reply(text=f"id: {chat[0]}\nuser_id: {chat[1]}\n"
                                     f"num_question: {chat[2]}\nanswer: {chat[3]}\n")


@router.message(F.text.startswith("del"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        id_msg = message.text.split(" ")[1].strip()
        await db_start()
        await delete_message(id_message=id_msg)
        await db_stop()
        await message.reply(f"Сообщение с id = {id_msg} удалено")


@router.message(Command("del_all"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        await delete_all_message()
        await db_stop()
        await message.reply("Все собщения удалены из базы данных")


@router.message(Command("cmd_bus"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        str_f_cmd = (f"***Список команд для администрирования чат-бота***:\n\n"
                     f"/act_bus - активация чат-бота;\n"
                     f"/dis_bus - деактивация чат-бота;\n"
                     f"/get_status_bus - получить текущий статус чат-бота;\n"
                     f"/get_file_db_size - получить размер файла базы данных чат-бота;\n"
                     f"/get_count_record - получить количество записей в базе от чат-бота;\n"
                     f"/get_all_chats - получить все чаты от чат-бота;\n"
                     f"del X - удалить еденичную запись в таблице (X - число);\n"
                     f"/del_all - удалить все записи в таблице;")
        await message.reply(text=str_f_cmd, parse_mode=ParseMode.MARKDOWN)
