import requests
import datetime
import os
import argparse
from telegram_space import save_img, file_extension
from pathlib import Path
from dotenv import load_dotenv


def get_nasa_epik(token, count=10):
    params = {
        "api_key": f"{token}"
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()

    count_image = 0
    count_iter = 0
    for img in response.json():
        list_date = img['date'].split(" ")[0].split("-")
        year, month, day = tuple(list_date)

        date = datetime.datetime(year=int(year), month=int(month), day=int(day))
        formatted_date = date.strftime("%Y/%m/%d")
        archive_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{img['image']}.png?api_key={token}"
        file_extensio = file_extension(archive_url)
        save_img(archive_url, f'nasa_epik_{count_image}{file_extensio}')
        count_image += 1
        count_iter += 1

        if count_iter > count-1:
            break


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['API_TOKEN_NASA']
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int)
    args = parser.parse_args()
    get_nasa_epik(token, args.count)
