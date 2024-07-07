"""TODO: docstring"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler

from .base import BaseHandler


class SettingsHandler(BaseHandler):
    """TODO: docstring, maybe make separate classes for each settings menu?"""

    _OPTIONS = [
        [InlineKeyboardButton("Option 1", callback_data="1")],
        [InlineKeyboardButton("Option 2", callback_data="2")],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    def __init__(self):
        super().__init__(
            name="settings",
            description="manage your settings",
        )

        self._query_handle = CallbackQueryHandler(self.button)
        self._reply_markup = InlineKeyboardMarkup(self._OPTIONS)

    @property
    def query_handle(self):
        """TODO: docstring"""
        return self._query_handle

    async def _callback(self, update: Update, _) -> None:
        """TODO: docstring"""
        await self._send_message(update=update, text="Choose: ", reply_markup=self._reply_markup)

    async def button(self, update: Update, _) -> None:
        """TODO: docstring"""
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
        await query.answer()

        await query.edit_message_text(text=f"Selected option: {query.data}")
