"""TODO: docstring"""

import logging

from types import SimpleNamespace

from telegram import MenuButtonCommands
from telegram.ext import Application, ApplicationBuilder

from .handlers import (
    StartHandler,
    HelpHandler,
    SettingsHandler,
    DropsHandler,
    NotificationsHandler,
    InlineDropsHandler,
)

logger = logging.getLogger(__name__)


class Bot:
    """Main class for the bot"""

    def __init__(self, token):
        self._token = token

        self._commands = SimpleNamespace(
            help=SimpleNamespace(
                name=HelpHandler().name,
                description=HelpHandler().description,
            ),
            settings=SimpleNamespace(
                name=SettingsHandler().name,
                description=SettingsHandler().description,
            ),
            drops=SimpleNamespace(
                name=DropsHandler().name,
                description=DropsHandler().description,
            ),
            notifications=SimpleNamespace(
                name=NotificationsHandler().name,
                description=NotificationsHandler().description,
            ),
        )

        self._application = (
            ApplicationBuilder().token(self._token).post_init(self._post_init).build()
        )

        self._application.add_handlers(
            [
                StartHandler().handle,
                HelpHandler().handle,
                SettingsHandler().handle,
                SettingsHandler().query_handle,
                DropsHandler().handle,
                NotificationsHandler().handle,
                InlineDropsHandler().handle,
            ]
        )

        self._application.run_polling()

    async def _post_init(self, application: Application) -> None:
        await application.bot.set_my_commands(
            [
                (self._commands.help.name, self._commands.help.description),
                (self._commands.settings.name, self._commands.settings.description),
                (self._commands.drops.name, self._commands.drops.description),
                (self._commands.notifications.name, self._commands.notifications.description),
            ]
        )
        await application.bot.set_chat_menu_button(menu_button=MenuButtonCommands())
