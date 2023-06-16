import os
import telegram
import time
import argparse
import random
from dotenv import load_dotenv
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Update


def post_img(images_name, interval=60*60*4):
    if images_name == None:
        while True:
            for img in list_img:
                bot.send_photo(chat_id='@spaceozerro', photo=open(f'./images/{img}', 'rb'))
                time.sleep(interval)
            random.shuffle(list_img)
    else:
        bot.send_photo(chat_id='@spaceozerro', photo=open(f'./images/{images_name}', 'rb'))


if __name__ == "__main__":
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    list_img = list(os.walk("images"))[0][2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type=int)
    parser.add_argument("--images_path", type=str)
    args = parser.parse_args()
    post_img(args.images_path, args.interval)

