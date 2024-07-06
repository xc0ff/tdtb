"""Interface class for a handler."""

from abc import ABC, abstractmethod


class IHandler(ABC):
    """Interface class for a handler."""

    @abstractmethod
    @property
    def handle(self):
        """Get handler's handle."""

    @abstractmethod
    @property
    def name(self) -> str:
        """Get name of a handler as a `str`."""

    @abstractmethod
    @property
    def description(self) -> str:
        """Get description of a handler. Used in setting up of a command."""

    @abstractmethod
    async def callback(self) -> None:
        """Handler's callback function."""
