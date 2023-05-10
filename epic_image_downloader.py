import datetime
import os
import argparse
import requests
from dotenv import load_dotenv
import all_func


def get_epic_image(_date, token, path):
    params = {
        'api_key': token
    }
    last_date_url = f'https://api.nasa.gov/EPIC/api/natural/date/{_date}'
    last_image_name = all_func.get_url_response(url=last_date_url, params=params)[0]['image']

    last_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{_date.year}/{"{0:0>2}".format(_date.month)}/{"{0:0>2}".format(_date.day)}/png/{last_image_name}.png'

    media_path = all_func.get_media_path(path)
    filename = media_path / f'img_{_date}.png'

    all_func.saving_media(filename, last_image_url, params=params)


def get_last_date(token):
    params = {
        'api_key': token
    }
    return datetime.datetime.strptime(
        all_func.get_url_response('https://api.nasa.gov/EPIC/api/natural/all', params=params)[0]['date'],
        "%Y-%m-%d").date()


def main():
    load_dotenv()
    token = os.environ['NASA_API_KEY']
    media_path = os.getenv('MEDIA_PATH', default='images')

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d').date(),
                        help='Enter launch data(year-month-day)')
    parser.add_argument('-p', '--path', help='Enter the path to the media folder', default=media_path)
    args = parser.parse_args()

    if args.date:
        get_epic_image(args.date, token, args.path)
    else:
        get_epic_image(get_last_date(token), token, args.path)


if __name__ == '__main__':
    main()
