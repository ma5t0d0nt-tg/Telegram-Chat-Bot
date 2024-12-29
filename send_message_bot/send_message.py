from aiogram.types import Message
from start_telegram_bot import bot
from message.parser_template_messages import get_info_about_new_message
from config.parser_config_admin import get_owner_user_id
import asyncio

from dotenv import load_dotenv
import os


async def send_information_bot(*, message: Message) -> None:
    """
    Функция для отправки информирующего сообщения владельцу бота в чате с ботом
    :param message: Message сообщение с информацией об отправителе этого собщения
    :return: None
    """
    info_msg = get_info_about_new_message().format(
        messages_from_user_id=message.from_user.id,
        message_type=message.chat.type,
        message_user_is_bot=message.from_user.is_bot,
        message_user_is_premium=message.from_user.is_premium,
        message_username=message.from_user.username,
        message_full_name=message.from_user.full_name,
        message_text=message.text,
        message_date=message.date.date(),
        message_time=message.date.time()
    )
    load_dotenv()
    await bot.send_message(os.getenv("USER_ID"), info_msg)
    return None
