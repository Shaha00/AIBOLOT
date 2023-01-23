from aiogram.utils import executor
from config import dp
import logging
from handlers import client


client.register_handlers_client(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
