from os import path
from typing import Text
from telegram import *
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from Dump_gitignore.parametrs import token 

class App():

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    

    def h(self,update: Update, context: CallbackContext) -> None:
        update.message.reply_text('так-так секундочку...')
        _text = (update.message.text).replace("/h ","")
        def func_h(text):
            if not update.message.reply_to_message:
                if not text.find('kick') == -1:
                    message = "ля, а за шо?"
                else: message = "не ошибся ли дверью,еблан?"
                return message
            else:
                message = "Еблан, харе перессылать сообщения"
                return message

        update.message.reply_text(func_h(_text))




    def main(self) -> None:
    
        updater = Updater(token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("h", self.h))
        updater.start_polling()
        updater.idle()

