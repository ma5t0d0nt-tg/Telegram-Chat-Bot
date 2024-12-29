"""
Файл обработчик команд для администрирования ботом
"""

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import configparser

from config.parser_config_admin import get_status_bot, set_active_bot, set_inactive_bot
from app.check_user import check_user

router = Router()


@router.message(Command("act_bot"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_active_bot()
        await message.reply(text="_Бот включен_", parse_mode=ParseMode.MARKDOWN)


@router.message(Command("dis_bot"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        set_inactive_bot()
        await message.reply(text="_Бот отключен_", parse_mode=ParseMode.MARKDOWN)


@router.message(Command("get_status_bot"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        current_status = int(get_status_bot())
        if current_status == 0:
            await message.reply(text="Бот отключен")
        elif current_status == 1:
            await message.reply(text="Бот работает")
            await message.reply(text="_Бот отключен_", parse_mode=ParseMode.MARKDOWN)
            await message.reply(text="_Бот работает_", parse_mode=ParseMode.MARKDOWN)


@router.message(Command("get_config"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        conf = configparser.ConfigParser()
        conf.read('config/config.ini')
        str_f = (f"*[ACTIVE_BOT]*:\n"
                 f"is_active_bot: {conf['ACTIVE_BOT']['is_active_bot']}\n\n"
                 f"*[ACTIVE_CHAT_BOT]*:\n"
                 f"is_active_business: {conf['ACTIVE_CHAT_BOT']['is_active_business']}")
        await message.reply(text=str_f, parse_mode=ParseMode.MARKDOWN)
