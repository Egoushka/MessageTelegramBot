import logging
import funcs
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

updater = Updater(token="1240090560:AAEnXnrUJzqTbGR89uuNYT8FDgrzSMGMhCo", use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

dispather = updater.dispatcher

start_handler = CommandHandler('start', funcs.start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), funcs.echo)

dispather.add_error_handler(funcs.error_callback)

dispather.add_handler(start_handler)
dispather.add_handler(echo_handler)

updater.start_polling()