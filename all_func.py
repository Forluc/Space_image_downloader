from os.path import splitext
from pathlib import Path
from urllib.parse import urlsplit

import requests


def get_img_format(url):
    url_split = urlsplit(url)
    img_format = splitext(url_split.path)
    return img_format[1]


def get_media_path(name_path):
    media_path = Path(name_path)
    media_path.mkdir(parents=True, exist_ok=True)
    return media_path


def get_url_response(url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def saving_media(filename, url, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
