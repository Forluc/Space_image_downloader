import argparse

import all_func
import requests


def fetch_spacex_last_launch(args_id):
    url = f'https://api.spacexdata.com/v5/launches/{args_id}'
    pictures = all_func.get_url_response(url)['links']['flickr']['original']

    media_path = all_func.get_media_path('spacex_images')

    for img_number, img_url in enumerate(pictures):
        response = requests.get(img_url)
        response.raise_for_status()
        filename = media_path / f'spacex_{img_number}{all_func.get_img_format(img_url)}'

        all_func.media_saving(filename, response)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, help='Enter launch id', default='latest')
    args = parser.parse_args()
    fetch_spacex_last_launch(args_id=args.id)  # 605b4b6aaa5433645e37d03f


if __name__ == '__main__':
    main()
