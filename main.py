import logging
from aiogram import executor
from bot_init import dp, bot, db


#logging.basicConfig(level=logging.WARN)
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

async def on_startup(_):
    print("BOT Started!")

from handlers import registration

registration.register_handlers_registration(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)