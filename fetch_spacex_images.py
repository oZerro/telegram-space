import requests
import argparse
from general_functions import save_img, get_file_extension
from pathlib import Path



def fetch_spacex_last_launch(id_spacex):
    url = "https://api.spacexdata.com/v5/launches"
    
    if id_spacex == "latest":
        response = requests.get(f'{url}/latest')
    else:
        params = {
            "id": f"{id_spacex}",
        }
        response = requests.get(url, params=params)
    response.raise_for_status()

    dictionary_with_images = []
    response = response.json()
    if type(response) == dict:
        dictionary_with_images.append(response)
        response = dictionary_with_images

    image_number = 0
    for img in response:
        images = img['links']['flickr']['original']       
        for image in images:
            file_format = get_file_extension(image)
            save_img(image, {}, f'spasex_{image_number}{file_format}')
            image_number += 1


if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description="Скачивает изображения с сайта Space_X. По дефолту скачивает фото с последнего запуска."
        )
    parser.add_argument("--id_spacex",
                        type=str,
                        default="latest",
                        help="id запуска, с которого нужно получить фото")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id_spacex)