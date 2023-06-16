import requests
import argparse
from telegram_space import save_img, file_extension
from pathlib import Path



def fetch_spacex_last_launch(id_spacex):
    url = "https://api.spacexdata.com/v5/launches/"
    
    if id_spacex == "":
        url += "latest"
        response = requests.get(url)
    else:
        params = {
            "id": f"{id_spacex}",
        }
        response = requests.get(url, params=params)
    response.raise_for_status()
    count_iter = 0
    count_images = 0
    arr = []
    list_response = response.json()
    if type(list_response) == dict:
        arr.append(list_response)
        list_response = arr

    for dict_images in list_response:
        list_images = dict_images['links']['flickr']['original']
        if len(list_images) == 0:
            break
        if len(list_images) > 0:
            for image in list_images:
                file_extensio = file_extension(image)
                save_img(image, f'spasex_{count_images}{file_extensio}')
                count_images += 1
            count_iter += 1
    
            if count_iter > 1:
                break


if __name__ == "__main__":
    Path("images").mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("--id_spacex", type=str)
    args = parser.parse_args()

    if args.id_spacex == None:
        args.id_spacex = ""
        fetch_spacex_last_launch(args.id_spacex)
    else:
        fetch_spacex_last_launch(args.id_spacex)