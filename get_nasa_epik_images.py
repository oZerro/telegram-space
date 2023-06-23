import requests
import datetime
import os
import argparse
from general_functions import save_img, get_file_extension
from pathlib import Path
from dotenv import load_dotenv


def get_nasa_epik(token, count):
    params = {
        "api_key": f"{token}"
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()

    for image_number, img in enumerate(response.json()):
        date_split = img['date'].split(" ")[0].split("-")
        year, month, day = tuple(date_split)
        date = datetime.datetime(year=int(year), month=int(month), day=int(day))
        formatted_date = date.strftime("%Y/%m/%d")
        archive_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{img['image']}.png"
        file_format = get_file_extension(archive_url)
        save_img(archive_url, params, f'nasa_epik_{image_number}{file_format}')

        count -= 1
        if count == 0:
            break        


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['API_TOKEN_NASA']
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='Скачивает "полихроматические изображения Земли" с сайта NASA.\
                     По дефолту скачивает 10 изображений. Если вам нужно определенное количество,\
                     то можете передать значание в аргуметы при запуске.'
    )
    parser.add_argument("--count", 
                        type=int, 
                        default=10,
                        help="Количество изображений для скачивания")
    args = parser.parse_args()
    get_nasa_epik(token, args.count)
