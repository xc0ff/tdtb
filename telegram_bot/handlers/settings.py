"""TODO: docstring"""

from telegram import Update

from .base import BaseHandler


class SettingsHandler(BaseHandler):
    """TODO: docstring"""

    def __init__(self):
        super().__init__(
            name="settings",
            description="manage your settings",
            callback=self.callback,
        )

    async def callback(self, update: Update, _) -> None:
        """TODO: docstring"""
