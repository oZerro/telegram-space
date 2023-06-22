import os
import telegram
import time
import argparse
import random
from dotenv import load_dotenv
from telegram.error import BadRequest


def loads_endless_posts(chat_id, image_name, images, interval=60*60*4):
    if image_name:
        loads_one_image(image_name, chat_id)      
    while True:
        for img in images:
            try:
                with open(f'./images/{img}', 'rb') as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
                    time.sleep(interval)
            except BadRequest as ex:
                print(ex)
                continue
        random.shuffle(images)


def loads_one_image(image_name, chat_id):
    if image_name:
        try:
            with open(f'./images/{image_name}', 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
        except BadRequest as ex:
            print("Вы пытаетесь загрузить слишком тяжелое изображение, лимит - 20 MB.\n \
                  Попробуйте загрузить другое изображение.")


if __name__ == "__main__":
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    images = list(os.walk("images"))[0][2]

    parser = argparse.ArgumentParser(
         description='Публикует на канале изображения из папки images.\
                      По дефолту 1 раз в 4 часа. В качестве аргументов принимает 1 обязательный аргумент - id\
                      вашего канала в формате @channel_name. И 2 не обязательных - название изображения из папки,\
                      которое вы хотите загрузить и интервал постов. Если вы не передали название изображения,\
                      то будут выбираться рандомные изображения из папки images.'
    )
    parser.add_argument("chat_id", help="id вашего канала в формате @channel_name")
    parser.add_argument("--interval", type=int, help="интервал публикаций")
    parser.add_argument("--images_name", type=str, help="имя изображения в формате nasa.jpg")
    args = parser.parse_args()
    loads_endless_posts(args.chat_id, args.images_name, images, args.interval)

