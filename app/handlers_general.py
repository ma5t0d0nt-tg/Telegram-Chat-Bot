"""
Файл обработчик команд пользователей бота
"""

from aiogram import F, Router
from aiogram.types import Message, TelegramObject, ChatFullInfo, BotCommand, ReactionTypeEmoji
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import configparser

from config.parser_config_admin import get_status_bot, set_active_bot, set_inactive_bot, get_owner_user_id
from config.parser_config_business import get_bot_version

router = Router()


@router.message(Command("start"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(text=f"Здравствуйте, {message.from_user.first_name}.\n"
                                 f"Я бот, предназаченный для автоматических ответов в личных чатах Telegram Messenger.")


@router.message(Command("author"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(text=f"Ссылка на автора данного бота\nhttps://t.me/m/KPzniy-vOTcy")


@router.message(Command("pic"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(
            text=f"Ссылка на аватар бота: https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi2.wp.com"
                 f"%2Fuangonline.com%2Fwp-content%2Fuploads%2F2018%2F09%2Fbisnis-berbasis-tekno.jpg%3Ffit%3D1200"
                 f"%252C794%26ssl%3D1&lr=11256&pos=0&rpt=simage&text=telegram%20bot%20assistant%20pic")


@router.message(Command("description"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        await message.reply(text="Этот бот работает как менеджер чатов для личных переписок с его создателем. "
                                 "Чтобы использовать чат-бота, используйте команду /author. Вам ответит чат-бот.")


@router.message(Command("version"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        ver = get_bot_version()
        await message.reply(text=f"**Версия бота**: *{ver}*", parse_mode=ParseMode.MARKDOWN)
