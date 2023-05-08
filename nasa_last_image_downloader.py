import os
from datetime import date
from dotenv import load_dotenv
import requests
import all_func


def get_nasa_picture_of_day(token):
    params = {
        'api_key': token
    }
    base_nasa_url = 'https://api.nasa.gov/planetary/apod'
    picture_url = all_func.get_url_response(url=base_nasa_url, params=params)['url']
    response_picture = requests.get(picture_url)
    response_picture.raise_for_status()

    media_path = all_func.get_media_path('nasa_images')

    filename = media_path / f'last_photo_{date.today()}{all_func.get_img_format(picture_url)}'
    all_func.media_saving(filename, response_picture)


def main():
    load_dotenv()
    token = os.environ['NASA_API_KEY']
    get_nasa_picture_of_day(token)


if __name__ == '__main__':
    main()
