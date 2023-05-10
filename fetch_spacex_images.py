import argparse
import os

from dotenv import load_dotenv

import all_func
import requests


def fetch_spacex_last_launch(path, launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    pictures = all_func.get_url_response(url)['links']['flickr']['original']

    media_path = all_func.get_media_path(path)

    for img_number, img_url in enumerate(pictures):
        filename = media_path / f'spacex_{img_number}{all_func.get_img_format(img_url)}'
        all_func.saving_media(filename, img_url)


def main():
    load_dotenv()
    media_path = os.getenv('MEDIA_PATH', default='images')

    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, help='Enter launch id', default='latest')
    parser.add_argument('-p', '--path', help='Enter the path to the media folder', default=media_path)
    args = parser.parse_args()
    fetch_spacex_last_launch(args.path, launch_id=args.id)  # 605b4b6aaa5433645e37d03f


if __name__ == '__main__':
    main()
