import requests
from telegram_space import save_img, file_extension
from pathlib import Path


def get_nasa_apod():
    params = {
        "count": 30
    }
    url = "http://etokosmo.ru:5678/v1/apod/" 
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    count_images = 0
    for url_imd in response.json():
        file_extensio = file_extension(url_imd['url'])
        save_img(url_imd['url'], f'nasa_apod_{count_images}{file_extensio}')
        count_images += 1


if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    get_nasa_apod()