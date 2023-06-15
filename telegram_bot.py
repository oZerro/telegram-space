import os
import telegram
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update

load_dotenv()

bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


bot.send_message(chat_id='@spaceozerro', text="I'm a bot, please talk to me!")

