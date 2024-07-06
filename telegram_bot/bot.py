import asyncio
import logging

from types import SimpleNamespace

from telegram import MenuButtonCommands, Update
from telegram.ext import Application, ApplicationBuilder, ContextTypes, CommandHandler

from .handlers import StartHandler, HelpHandler, SettingsHandler, DropsHandler


logger = logging.getLogger(__name__)


class Bot:
    """Main class for the bot"""

    # 1. make a twitch api query
    # 2. check for updated info on drops
    # 3. if updates found, query for users subbed to a game from db
    # 4. if at least one user is found, send notification
    # 5. await asyncio.sleep(1800) # sleep for 30 mins

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
        )

        self._application = (
            ApplicationBuilder().token(self._token).post_init(self._post_init).build()
        )

        self._application.add_handlers(
            [
                StartHandler().handle,
                HelpHandler().handle,
                SettingsHandler().handle,
                DropsHandler().handle,
            ]
        )

        self._application.add_handler(CommandHandler("set", set_timer))
        self._application.add_handler(CommandHandler("unset", unset_timer))

        self._application.run_polling()

    async def _post_init(self, application: Application) -> None:
        await application.bot.set_my_commands(
            [
                (self._commands.help.name, self._commands.help.description),
                (self._commands.settings.name, self._commands.settings.description),
                (self._commands.drops.name, self._commands.drops.description),
                ("set", "set timer to test the job queue"),
                ("unset", "unset the job queue timer"),
            ]
        )
        await application.bot.set_chat_menu_button(menu_button=MenuButtonCommands())


async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Okay! Bot will send you notifications from now on."
    )

    chat_id = update.message.chat_id
    remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_repeating(
        callback_minute, chat_id=chat_id, interval=60, first=10, name=str(chat_id)
    )


async def callback_minute(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        context.job.chat_id, text="One message every minute."
    )


def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def unset_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = (
        "Timer successfully cancelled!" if job_removed else "You have no active timer."
    )
    await update.message.reply_text(text)
