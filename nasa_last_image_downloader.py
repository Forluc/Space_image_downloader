import argparse
import os
from datetime import date
from dotenv import load_dotenv
import requests
import all_func


def get_nasa_picture_of_day(token, path):
    params = {
        'api_key': token
    }
    base_nasa_url = 'https://api.nasa.gov/planetary/apod'
    picture_url = all_func.get_url_response(url=base_nasa_url, params=params)['url']

    media_path = all_func.get_media_path(path)

    filename = media_path / f'last_photo_{date.today()}{all_func.get_img_format(picture_url)}'
    all_func.saving_media(filename, picture_url, params=params)


def main():
    load_dotenv()
    token = os.environ['NASA_API_KEY']
    media_path = os.getenv('MEDIA_PATH', default='images')

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Enter the path to the media folder', default=media_path)
    args = parser.parse_args()

    get_nasa_picture_of_day(token, args.path)


if __name__ == '__main__':
    main()
