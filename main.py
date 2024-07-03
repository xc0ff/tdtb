import logging

from config import BOT_TOKEN, CLIENT_ID, AUTH_TOKEN
from telegram_bot.bot import Bot
from twitch_drops_overseer.overseer import Overseer


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

if __name__ == "__main__":
    bot = Bot(BOT_TOKEN)
    overseer = Overseer(CLIENT_ID, AUTH_TOKEN)
    overseer.get_drop_campaigns()
