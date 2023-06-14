import requests
import datetime
from pathlib import Path
from urllib.parse import urlparse
from os.path import split, splitext


Path("images").mkdir(parents=True, exist_ok=True)

def save_img(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def file_extension(path):
    o = urlparse(path)
    filename = split(o.path)[1]
    file_extension = splitext(filename)[1]
    return file_extension


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/"
    params = {
        "id": "5eb87d47ffd86e000604b38a",
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    count_iter = 0
    count_images = 0
    
    for dict_images in response.json():
        list_images = dict_images['links']['flickr']['original']
        if len(list_images) > 0:
            for image in list_images:
                file_extensio = file_extension(image)
                save_img(image, f'spasex_{count_images}{file_extensio}')
                count_images += 1
            count_iter += 1
    
            if count_iter > 1:
                break


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


def get_nasa_epik():
    params = {
        "api_key": "sYS08d5zEM7LSNrdGsJdgeIN1oPvCPmlHqIBdUQ8"
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
        archive_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{img['image']}.png?api_key=sYS08d5zEM7LSNrdGsJdgeIN1oPvCPmlHqIBdUQ8"
        file_extensio = file_extension(archive_url)
        save_img(archive_url, f'nasa_epik_{count_image}{file_extensio}')
        count_image += 1
        count_iter += 1

        if count_iter > 9:
            break
