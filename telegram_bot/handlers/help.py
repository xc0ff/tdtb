"""TODO: docstring"""

from telegram import Update

from .base import BaseHandler


class HelpHandler(BaseHandler):
    """TODO: docstring"""

    def __init__(self):
        super().__init__(
            name="help",
            description="get some help",
            callback=self.callback,
        )

    async def callback(self, update: Update, _) -> None:
        """TODO: docstring"""
        await self.send_message(update=update, text="Ha-ha, nothing can help you (yet).")
