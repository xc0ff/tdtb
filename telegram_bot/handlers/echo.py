from os import sys
import random

from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


class EchoHandler:
    def __init__(self):
        self.handle = MessageHandler(filters.TEXT & ~(filters.COMMAND), self.echo)

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"test#{random.randint(~sys.maxsize, sys.maxsize)}",
        )
