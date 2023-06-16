import requests
import argparse
import os
from telegram_space import save_img, file_extension
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
    
    count_images = 0
    for url_imd in response.json():
        file_extensio = file_extension(url_imd['url'])
        save_img(url_imd['url'], f'nasa_apod_{count_images}{file_extensio}')
        count_images += 1


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['API_TOKEN_NASA']
    Path("images").mkdir(parents=True, exist_ok=True)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int)
    args = parser.parse_args()
    get_nasa_apod(token, args.count)