"""
Файл обработчик команд для администрирования чат-бота
"""

from aiogram import F, Router
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import os

from config.parser_config_business import get_active_business, set_active_business, set_inactive_business
from config.parser_config_admin import get_owner_user_id
from db.sqlite import db_start, get_count_record, get_all_chats, delete_message, delete_all_message, db_stop
from app.check_user import check_user

router = Router()


@router.message(Command("act_bus"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_active_business()
        await message.reply(text="Чат-бот включен")


@router.message(Command("dis_bus"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_inactive_business()
        await message.reply(text="Чат-бот отключен")


@router.message(Command("get_status_bus"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        current_status = int(get_active_business())
        if current_status == 0:
            await message.reply(text="Чат-бот отключен")
        elif current_status == 1:
            await message.reply(text="Чат-бот работает")


@router.message(Command("get_file_db_size"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        file_size_byte = os.path.getsize("messages.db")
        file_size_kbyte = file_size_byte / 1024
        await message.reply(f"Размер файла с базой данных: {file_size_kbyte} КБ")


@router.message(Command("get_count_record"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        count = await get_count_record()
        await db_stop()
        await message.reply(f"Количество записей в базе данных: {count[0][0]}")


@router.message(Command("get_all_chats"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        chats = await get_all_chats()
        await db_stop()
        for chat in chats:
            await message.reply(text=f"id: {chat[0]}\nuser_id: {chat[1]}\n"
                                     f"num_question: {chat[2]}\nanswer: {chat[3]}\n")


@router.message(F.text.startswith("del"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        id_msg = message.text.split(" ")[1].strip()
        await db_start()
        await delete_message(id_message=id_msg)
        await db_stop()
        await message.reply(f"Сообщение с id = {id_msg} удалено из базы данных")


@router.message(Command("del_all"))
async def handler(message: Message):
    is_owner = check_user(user_id_message=message.from_user.id)
    if is_owner:
        await db_start()
        await delete_all_message()
        await db_stop()
        await message.reply("Все собщения удалены из базы данных")
