"""Start command handler class."""

from telegram import Update

from .base import BaseHandler


class StartHandler(BaseHandler):
    """Start command handler class."""

    def __init__(self):
        super().__init__(name="start", callback=self.callback)

    async def callback(self, update: Update, _) -> None:
        """TODO: docstring"""
        await self.send_message("hi. see /help for more info.")
