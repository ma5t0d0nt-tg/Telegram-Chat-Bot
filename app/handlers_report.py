"""
Файл обработчик для создания отчетов в формате PDF и XLSX
"""

from aiogram import F, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

import time
import os

# for pdf
import fpdf
# for xlsx
import pandas as pd

from app.check_user import check_user

router = Router()


@router.message(Command("get_report_pdf"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=16)
        pdf.cell(200, 10, txt="The report is in pdf format using fpdf", ln=2, align="C")
        pdf.output("reports/report_pdf.pdf")
        time.sleep(2)
        await message.answer_document(document=FSInputFile(f"./reports/report_pdf.pdf"),
                                      caption="_Отчет в формате pdf с использованием fpdf_",
                                      parse_mode=ParseMode.MARKDOWN)


@router.message(Command("get_report_xlsx"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        df = pd.DataFrame(columns=['', '', 'Отчет в формате xlsx с использованием pandas'])
        filepath = os.path.join('reports', 'report_xlsx.xlsx')
        excel_writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
        df.to_excel(excel_writer, index=False, sheet_name='Sheet1', freeze_panes=(1, 0))
        excel_writer._save()
        excel_writer.close()
        time.sleep(2)
        await message.answer_document(document=FSInputFile("./reports/report_xlsx.xlsx"),
                                      caption="_Отчет в формате xlsx с использованием pandas_",
                                      parse_mode=ParseMode.MARKDOWN)


@router.message(Command("get_report_all"))
async def handler(message: Message):
    is_owner: bool = check_user(user_id_message=message.from_user.id)
    if is_owner:
        reports = os.listdir("./reports")
        if len(reports) > 0:
            for report in reports:
                await message.answer_document(document=FSInputFile(f"./reports/{report}"))
