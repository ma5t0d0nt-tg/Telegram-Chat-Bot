import asyncio
import logging
from aiogram import Bot, Dispatcher
from app import handlers_business, handlers_admin_bot, handlers_admin_business, handlers_general, handlers_report

from config.parser_config_admin import get_token

TOKEN = get_token()
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(handlers_business.router,
                       handlers_admin_bot.router,
                       handlers_admin_business.router,
                       handlers_general.router,
                       handlers_report.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        bot.session.close()
