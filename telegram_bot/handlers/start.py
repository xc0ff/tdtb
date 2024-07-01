from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


class StartHandler:
    def __init__(self) -> None:
        self.handle = CommandHandler("start", self.start)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"hi",
        )
