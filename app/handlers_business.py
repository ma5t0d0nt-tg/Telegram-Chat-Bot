import pprint

from aiogram import F, Router
from aiogram.types import Message, TelegramObject, ChatFullInfo, ReactionTypeEmoji
from aiogram.filters import CommandStart, Command
import logging
from start_telegram_bot import bot
import json
from sqlite import db_start, check_answer_on_question, add_message

from message.parser_template_messages import *
from send_message_bot.send_message import send_information_bot
from config.parser_config_business import get_active_business

router = Router()


@router.business_message()
async def handler(message: Message):
    status = get_active_business()

    if status == "1":
        await db_start()

        check_answer_0 = await check_answer_on_question(user_id=message.from_user.id, num_question=0)
        check_answer_1 = await check_answer_on_question(user_id=message.from_user.id, num_question=1)
        check_answer_2 = await check_answer_on_question(user_id=message.from_user.id, num_question=2)
        check_answer_3 = await check_answer_on_question(user_id=message.from_user.id, num_question=3)

        if not check_answer_0:

            await add_message(user_id=message.from_user.id, num_question=0, answer=message.text)
            await message.reply(text=get_welcome_messages())
            await message.reply(text=get_question_1())

        elif not check_answer_1:

            await add_message(user_id=message.from_user.id, num_question=1, answer=message.text)
            await message.reply(text=get_question_2())

        elif not check_answer_2:

            await add_message(user_id=message.from_user.id, num_question=2, answer=message.text)
            await message.reply(text=get_question_3())

        elif not check_answer_3:

            await add_message(user_id=message.from_user.id, num_question=3, answer=message.text)
            await message.reply(text="Ответы отправлены. Вам ответят позже")

        elif check_answer_1 and check_answer_2 and check_answer_3:

            await message.reply(text="Ответы отправлены. Вам ответят позже")
