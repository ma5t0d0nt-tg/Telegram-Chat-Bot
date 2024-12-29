import asyncio
from aiogram import Bot, Dispatcher
from app import (handlers_business, handlers_admin_bot, handlers_admin_business, handlers_general, handlers_report,
                 handlers_cmd, handlers_easter_eggs)

from dotenv import load_dotenv, get_key, set_key
import os

load_dotenv()

TOKEN = os.getenv("KEY")
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(handlers_business.router,
                       handlers_admin_bot.router,
                       handlers_admin_business.router,
                       handlers_general.router,
                       handlers_report.router,
                       handlers_cmd.router,
                       handlers_easter_eggs.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        bot.session.close()
