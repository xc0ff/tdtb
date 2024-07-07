"""TODO: docstring"""

from html import escape
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import InlineQueryHandler

from .base import IHandler


class InlineDropsHandler(IHandler):
    """TODO: docstring"""

    def __init__(self):
        self._handle = InlineQueryHandler(self._callback)

    @property
    def handle(self):
        return self._handle

    async def _callback(self, update: Update, _) -> None:
        """Handle the inline query. This is run when you type: @botusername <query>"""
        query = update.inline_query.query

        if not query:  # empty query should not be handled
            return

        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="Caps",
                input_message_content=InputTextMessageContent(query.upper()),
            ),
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="Bold",
                input_message_content=InputTextMessageContent(
                    f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
                ),
            ),
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="Italic",
                input_message_content=InputTextMessageContent(
                    f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
                ),
            ),
        ]

        await update.inline_query.answer(results)
