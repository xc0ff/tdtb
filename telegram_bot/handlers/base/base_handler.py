"""Base class with the most common properties of handlers."""

from typing import Optional

from telegram.ext import CommandHandler


class BaseHandler:
    """Base class with the most common properties of handlers."""

    def __init__(
        self,
        name: str,
        description: Optional[str] = None,
        callback: Optional[CommandHandler] = None,
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

    async def callback(self) -> None:
        """Handler's callback function."""
