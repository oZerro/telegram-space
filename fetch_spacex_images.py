import requests
import argparse
from general_functions import save_img, get_file_extension
from pathlib import Path



def fetch_spacex_last_launch(spacex_id):
    url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(f'{url}{spacex_id}')
    response.raise_for_status()
    response = response.json()

    images = response['links']['flickr']['original']       
    for image_number, image in enumerate(images):
        file_format = get_file_extension(image)
        save_img(image, {}, f'spaсex_{image_number}{file_format}')


if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description="Скачивает изображения с сайта Space_X. По дефолту скачивает фото с последнего запуска."
        )
    parser.add_argument("--spacex_id",
                        type=str,
                        default="latest",
                        help="id запуска, с которого нужно получить фото")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.spacex_id)
