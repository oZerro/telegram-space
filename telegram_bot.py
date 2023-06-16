import os
import telegram
import time
import argparse
import random
from dotenv import load_dotenv
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update


def infiniti_post(chat_id, list_img, interval):
    while True:
            for img in list_img:
                bot.send_photo(chat_id=chat_id, photo=open(f'./images/{img}', 'rb'))
                time.sleep(interval)
            random.shuffle(list_img)

def post_img(chat_id, images_name, interval=60*60*4):
    if images_name == None:
        infiniti_post(chat_id, list_img, interval)
    else:
        bot.send_photo(chat_id=chat_id, photo=open(f'./images/{images_name}', 'rb'))
        infiniti_post(chat_id, list_img, interval)
        

if __name__ == "__main__":
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    list_img = list(os.walk("images"))[0][2]
    parser = argparse.ArgumentParser()
    parser.add_argument("chat_id")
    parser.add_argument("--interval", type=int)
    parser.add_argument("--images_name", type=str)
    args = parser.parse_args()
    post_img(args.chat_id, args.images_name, args.interval)

