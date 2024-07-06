"""Base class with the most common properties of handlers."""

from abc import abstractmethod
from typing import Optional

from telegram import Update
from telegram.ext import CommandHandler


class BaseHandler:
    """Base class with the most common properties of handlers."""

    def __init__(
        self,
        name: str,
        callback: CommandHandler,
        description: Optional[str] = None,
    ):
        self._name = name
        self._description = description
        self._handle = CommandHandler(self._name, callback)

    @property
    def handle(self):
        """Get handler's handle."""
        return self._handle

    @property
    def name(self) -> str:
        """Get name of a handler as a `str`."""
        return self._name

    @property
    def description(self) -> str:
        """Get description of a handler. Used in setting up of a command."""
        return self._description

    @abstractmethod
    async def callback(self, update: Update, _) -> None:
        """Print help message."""

    async def send_message(self, update: Update, text: str) -> None:
        """TODO: docsting"""
        await update.message.reply_text(text)
