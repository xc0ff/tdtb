import logging

from config import BOT_TOKEN
from telegram_bot.bot import Bot
from twitch_drops_overseer.overseer import Overseer

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    bot = Bot(BOT_TOKEN)
    # overseer = Overseer(CLIENT_ID, AUTH_TOKEN)
    # overseer.get_drop_campaigns()
