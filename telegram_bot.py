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


bot.send_photo(chat_id='@spaceozerro', photo=open('./images/nasa_apod_1.jpg', 'rb'))

