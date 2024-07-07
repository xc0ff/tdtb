"""Interface class for a handler."""

from abc import ABC, abstractmethod

from telegram import Update
from telegram.ext import ContextTypes


class IHandler(ABC):
    """Interface class for a handler."""

    @property
    def handle(self):
        """Get handler's handle."""

    @property
    def name(self) -> str:
        """Get name of a handler as a `str`."""

    @property
    def description(self) -> str:
        """Get description of a handler. Used in setting up of a command."""

    @abstractmethod
    async def _callback(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Handler's callback function."""
