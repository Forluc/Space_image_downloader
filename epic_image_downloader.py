import datetime
import os
import argparse
import requests
from dotenv import load_dotenv
import all_func


def get_epic_image(_date, token):
    params = {
        'api_key': token
    }
    last_date_url = f'https://api.nasa.gov/EPIC/api/natural/date/{_date}'
    name_last_image = all_func.get_url_response(url=last_date_url, params=params)[0]['image']
    last_img_response = requests.get(
        f'https://api.nasa.gov/EPIC/archive/natural/{_date.year}/{"{0:0>2}".format(_date.month)}/{"{0:0>2}".format(_date.day)}/png/{name_last_image}.png',
        params=params)
    last_img_response.raise_for_status()

    media_path = all_func.get_media_path('epic_images')

    filename = media_path / f'img_{_date}.png'
    all_func.media_saving(filename, last_img_response)


def get_last_date(token):
    params = {
        'api_key': token
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/all', params=params)
    response.raise_for_status()
    return datetime.datetime.strptime(response.json()[0]['date'], "%Y-%m-%d").date()


def main():
    load_dotenv()
    token = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(),
                        help='Enter launch data(year-month-day)')
    args = parser.parse_args()

    if args.date:
        get_epic_image(args.date, token)
    else:
        get_epic_image(get_last_date(token), token)


if __name__ == '__main__':
    main()
