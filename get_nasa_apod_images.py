import requests
import argparse
import os
from telegram_space import save_img, get_file_extension
from pathlib import Path
from dotenv import load_dotenv


def get_nasa_apod(token, count=30):
    params = {
        "api_key": f"{token}",
        "count": count
    }
    url = "https://api.nasa.gov/planetary/apod" 
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    dictionary_set_with_images = []
    response = response.json()
    if type(response) == dict:
        dictionary_set_with_images.append(response)
        response = dictionary_set_with_images

    for image_number, link_for_image in enumerate(response):
        file_format = get_file_extension(link_for_image['url'])
        save_img(link_for_image['url'], {},f'nasa_apod_{image_number}{file_format}')
    


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['API_TOKEN_NASA']
    Path("images").mkdir(parents=True, exist_ok=True)
    
    parser = argparse.ArgumentParser(
        description='Скачивает "Астрономические картини дня" с сайта NASA. \
                    По дефолту скачивает 30 изображений.\n Если вам нужно определенное количество,\
                    то можете передать значание в аргумете COUNT при запуске. '
    )
    parser.add_argument("--count", type=int, help="Количество изображений для скачивания")
    args = parser.parse_args()
    get_nasa_apod(token, args.count)