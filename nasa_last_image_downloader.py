import os
from datetime import date
from pathlib import Path
from dotenv import load_dotenv
import requests
from all_func import get_img_format


def get_nasa_picture_of_day(url, token):
    params = {
        'api_key': f'{token}'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    picture_url = response.json()['url']
    response_picture = requests.get(picture_url)
    response_picture.raise_for_status()

    images_nasa_path = Path('nasa_images')
    images_nasa_path.mkdir(parents=True, exist_ok=True)

    filename = images_nasa_path / f'last_photo_{date.today()}{get_img_format(picture_url)}'
    with open(filename, 'wb') as file:
        file.write(response_picture.content)


def main():
    load_dotenv()
    token = os.environ['api_key']
    base_nasa_url = 'https://api.nasa.gov/planetary/apod'
    get_nasa_picture_of_day(base_nasa_url, token)


if __name__ == '__main__':
    main()
