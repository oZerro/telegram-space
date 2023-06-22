import requests
from urllib.parse import urlparse
from os.path import split, splitext


def save_img(url, params=None, filename=""):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def get_file_extension(path):
    o = urlparse(path)
    filename = split(o.path)[1]
    file_extension = splitext(filename)[1]
    return file_extension

