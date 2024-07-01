import logging

from config import BOT_TOKEN
from telegram_bot import bot


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
