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
        str_f_cmd = (f"***Список команд для администрирования бота***:\n"
                     f"*/act_bot* - активация бота;\n"
                     f"*/dis_bot* - деактивация бота;\n"
                     f"*/get_status_bot* - получить текущий статус бота;\n"
                     f"*/get_config* - получить размер файла базы данных;\n\n"
                     f""
                     f"***Список команд для администрирования чат-бота***:\n"
                     f"*/act_bus* - активация чат-бота;\n"
                     f"*/dis_bus* - деактивация чат-бота;\n"
                     f"*/get_status_bus* - получить текущий статус чат-бота;\n"
                     f"*/get_file_db_size* - получить размер файла базы данных чат-бота;\n"
                     f"*/get_count_record* - получить количество записей в базе от чат-бота;\n"
                     f"*/get_all_chats* - получить все чаты от чат-бота;\n"
                     f"*del X* - удалить еденичную запись в таблице (X - число);\n"
                     f"*/del_all* - удалить все записи в таблице;\n\n"
                     f""
                     f"***Команды для пасхалки***:\n"
                     f"*/this_en* - пасхалка в английском варианте;\n"
                     f"*/this_ru* - пасхалка в русском варианте;\n\n"
                     f""
                     f"***Команды для получения отчетов***:\n"
                     f"*/get_report_pdf* - отчет в формате pdf;\n"
                     f"*/get_report_xlsx* - отчет в формате excel;\n")

        await message.reply(text=str_f_cmd, parse_mode=ParseMode.MARKDOWN)
