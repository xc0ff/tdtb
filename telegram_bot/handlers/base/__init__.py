"""Base module containing all the building blocks for handlers of the bot"""

__all__ = (
    "BaseHandler",
    "IHandler",
)

from .base_handler import BaseHandler
from .handler_interface import IHandler
