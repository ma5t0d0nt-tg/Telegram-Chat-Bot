"""
Файл обработчик для создания отчетов в формате PDF и XLSX
"""

from aiogram import F, Router
from aiogram.types import Message, TelegramObject, ChatFullInfo, BotCommand, ReactionTypeEmoji, InputFile, FSInputFile
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import time
import os

# for pdf
import fpdf
# for xlsx
import pandas as pd

from config.parser_config_admin import get_owner_user_id

router = Router()


def __check_user(user_id_message: int) -> bool:
    """
    Функция для проверки доступа к управлению ботом и его настройками
    :param user_id_message: int user_id пользователя, который пишет боту
    :return: true - дается доступ к функциям бота, false - запрет
    """
    user_id_owner = get_owner_user_id()
    return user_id_message == user_id_owner


@router.message(Command("get_report_pdf"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt="", ln=1, align="C")
        pdf.output(f"reports/report_pdf.pdf")
        time.sleep(2)
        await message.answer_document(FSInputFile(f"./reports/report_pdf.pdf"))
        time.sleep(2)
        os.remove(f"./reports/report_pdf.pdf")


@router.message(Command("get_report_xlsx"))
async def handler(message: Message):
    is_owner = __check_user(user_id_message=message.from_user.id)
    if is_owner:
        df = pd.DataFrame(columns=['Имя', 'Адрес', 'Email', 'Телефон'])
        filepath = os.path.join('reports', 'report_xlsx.xlsx')
        excel_writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
        df.to_excel(excel_writer, index=False, sheet_name='Sheet1', freeze_panes=(1, 0))
        excel_writer._save()
        excel_writer.close()
        time.sleep(2)
        await message.answer_document(FSInputFile(f"./reports/report_xlsx.xlsx"))
        time.sleep(2)
        os.remove(f"./reports/report_xlsx.xlsx")
