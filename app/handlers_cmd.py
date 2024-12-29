"""
Файл обработчик для получения всех возможных команд администрирования
"""

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

from message.parser_template_messages import get_cmd
from app.check_user import check_user

from dotenv import load_dotenv
import os

router = Router()


@router.message(Command("cmd"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        str_f_cmd = get_cmd()
        await message.reply(text=str_f_cmd, parse_mode=ParseMode.MARKDOWN)
