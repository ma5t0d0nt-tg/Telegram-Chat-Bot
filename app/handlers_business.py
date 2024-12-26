"""
Файл обработчик в чате с пользователем, для отправки и получения ответов от собеседника
"""

# aiogram
import pprint

from aiogram import Router
from aiogram.types import Message

# sqlite
from db.sqlite import db_start, check_answer_on_question, add_message, get_question_for_chats, db_stop

# my import
from message.parser_template_messages import *
from config.parser_config_business import get_active_business
from config.parser_config_admin import get_owner_user_id

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

        list_check_answer = [check_answer_0, check_answer_1, check_answer_2, check_answer_3]

        if not all(list_check_answer):
            for index, answer in enumerate(list_check_answer):
                if not answer:
                    await add_message(user_id=message.from_user.id, num_question=index, answer=message.text)
                    if index == 0:
                        await message.answer(text=get_welcome_messages())
                        await message.answer(text=get_question(index + 1))
                    elif index == len(list_check_answer) - 1:
                        await message.answer(text=all_answers_get())
                    else:
                        await message.answer(text=get_question(index + 1))
                    break

        await db_stop()
