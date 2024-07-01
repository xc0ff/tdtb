import asyncio

from telegram.ext import ApplicationBuilder

from .handlers import EchoHandler, StartHandler


class Bot:
    """Main class for the bot
    """
    def __init__(self, token):
        self._token = token
        self._application = ApplicationBuilder().token(self._token).build()
    
        start_handler = StartHandler()
        echo_handler = EchoHandler()

        self._application.add_handler(start_handler.handle)
        self._application.add_handler(echo_handler.handle)

        self._application.run_polling()

    async def run(self):
        while True:
            # 1. make a twitch api query
            # 2. check for updated info on drops
            # 3. if updates found, query for users subbed to a game from db 
            # 4. if at least one user is found, send notification

            # 5. await asyncio.sleep(1800) # sleep for 30 mins
            pass
