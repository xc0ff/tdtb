"""TODO: docstring"""

from telegram import Update
from telegram.ext import ContextTypes

from .base import BaseHandler


class NotificationsHandler(BaseHandler):
    """TODO: docstring
    
    rough draft of what we need to do:
    1. make a twitch api query
    2. check for updated info on drops
    3. if updates found, query for users subbed to a game from db
    4. if at least one user is found, send notification
    5. await asyncio.sleep(1800) # sleep for 30 mins
    """

    def __init__(self):
        super().__init__(
            name="notificator",
            description="turn notifications on or off",
            callback=self.callback,
        )

    async def _timer_callback(self, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(context.job.chat_id, text="One message every minute.")

    def _remove_job_if_exists(
        self,
        name: str,
        context: ContextTypes.DEFAULT_TYPE,
    ) -> bool:
        """Remove job with given name. Returns whether job was removed."""
        current_jobs = context.job_queue.get_jobs_by_name(name)
        if not current_jobs:
            return False
        for job in current_jobs:
            job.schedule_removal()
        return True

    async def callback(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ) -> None:
        chat_id = update.message.chat_id

        job_removed = self._remove_job_if_exists(str(chat_id), context)
        if job_removed:
            await self._send_message(
                update=update, text="Timer successfully cancelled!"
            )
            return

        await self._send_message(
            update=update, text="Okay! Bot will send you notifications from now on."
        )
        context.job_queue.run_repeating(
            self._timer_callback,
            chat_id=chat_id,
            interval=60,
            first=10,
            name=str(chat_id),
        )
