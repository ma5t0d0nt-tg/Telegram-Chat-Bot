from aiogram import Router
from aiogram.types import Message
from db.sqlite import db_start, check_answer_on_question, add_message, db_stop

from message.parser_template_messages import *
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
            emoji_got_it = ReactionTypeEmoji(emoji='👍')
            await message.react(reaction=[emoji_got_it])
            await message.answer(text=get_welcome_messages())
            await message.answer(text=get_question_1())

        elif not check_answer_1:

            emoji_got_it = ReactionTypeEmoji(emoji='👍')
            await message.react(reaction=[emoji_got_it])
            await add_message(user_id=message.from_user.id, num_question=1, answer=message.text)
            await message.answer(text=get_question_2())

        elif not check_answer_2:

            emoji_got_it = ReactionTypeEmoji(emoji='👍')
            await message.react(reaction=[emoji_got_it])
            await add_message(user_id=message.from_user.id, num_question=2, answer=message.text)
            await message.answer(text=get_question_3())

        elif not check_answer_3:

            emoji_got_it = ReactionTypeEmoji(emoji='👍')
            await message.react(reaction=[emoji_got_it])
            await add_message(user_id=message.from_user.id, num_question=3, answer=message.text)
            await message.answer(text=all_answers_get())

        elif check_answer_1 and check_answer_2 and check_answer_3:

            await message.answer(text=all_answers_get())

        await db_stop()
