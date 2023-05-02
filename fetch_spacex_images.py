from pathlib import Path
import argparse
from all_func import get_img_format
import requests


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']

    images_spacex_path = Path('spacex_images')
    images_spacex_path.mkdir(parents=True, exist_ok=True)

    for img_number, img_url in enumerate(pictures):
        response = requests.get(img_url)
        response.raise_for_status()
        filename = images_spacex_path / f'spacex_{img_number}{get_img_format(img_url)}'

        with open(filename, 'wb') as file:
            file.write(response.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, help='Enter launch id')
    args = parser.parse_args()
    if args.id:
        fetch_spacex_last_launch(f'https://api.spacexdata.com/v5/launches/{args.id}')  # 605b4b6aaa5433645e37d03f
    else:
        fetch_spacex_last_launch('https://api.spacexdata.com/v5/launches/latest')

if __name__ == '__main__':
    main()
