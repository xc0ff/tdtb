"""TODO: docstring"""

from telegram import Update

from .base import BaseHandler


class DropsHandler(BaseHandler):
    """TODO: docstring"""

    def __init__(self):
        super().__init__(
            name="drops",
            description="get current drops for games from your list",
        )

    async def _callback(self, update: Update, _) -> None:
        """TODO: docstring"""
