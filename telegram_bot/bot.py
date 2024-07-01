from telegram.ext import ApplicationBuilder

from .handlers import EchoHandler, StartHandler


def run(bot_token):
    application = ApplicationBuilder().token(bot_token).build()
    start_handler = StartHandler()
    echo_handler = EchoHandler()

    application.add_handler(start_handler.handle)
    application.add_handler(echo_handler.handle)

    application.run_polling()
