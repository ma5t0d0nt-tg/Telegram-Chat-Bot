"""
Файл обработчик пасхалок python в боте в двух вариантах
"""

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

from config.parser_config_admin import get_status_bot

router = Router()


# пасхалка
@router.message(Command("this_en"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        this_text = """
        ORIGIN
        <blockquote><i>The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!</i></blockquote>
        """
        await message.reply(text=this_text, parse_mode=ParseMode.HTML)


# пасхалка
@router.message(Command("this_ru"))
async def handler(message: Message):
    status = get_status_bot()
    if status == "1":
        this_text = """
        TRANSLATE
        <blockquote><i>Красивое лучше, чем уродливое.

Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложное лучше, чем запутанное.
Плоское лучше, чем вложенное.
Разреженное лучше, чем плотное.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибки никогда не должны замалчиваться.
Если они не замалчиваются явно.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один и, желательно, только один очевидный способ сделать это.
Хотя он поначалу может быть и не очевиден, если вы не голландец.
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить, то это плохая идея.
Если реализацию легко объяснить, то идея, возможно хороша.
Пространства имён - отличная штука! Будем делать их больше!
        </i></blockquote>
        """
        await message.reply(text=this_text, parse_mode=ParseMode.HTML)
