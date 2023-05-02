import datetime
import os
from pathlib import Path
import argparse
import requests
from dotenv import load_dotenv


def get_epic_image(_date, token):
    params = {
        'api_key': f'{token}'
    }
    response_last_date = requests.get(f'https://api.nasa.gov/EPIC/api/natural/date/{_date}',
                                      params=params)
    response_last_date.raise_for_status()

    name_last_image = response_last_date.json()[0]['image']

    last_img_response = requests.get(
        f'https://api.nasa.gov/EPIC/archive/natural/{_date.year}/{"{0:0>2}".format(_date.month)}/{"{0:0>2}".format(_date.day)}/png/{name_last_image}.png',
        params=params)

    img_path = Path('EPIC_images')
    img_path.mkdir(parents=True, exist_ok=True)

    filename = img_path / f'img_{_date}.png'
    with open(filename, 'wb') as file:
        file.write(last_img_response.content)


def get_last_date(token):
    params = {
        'api_key': f'{token}'
    }
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/all', params=params)
    response.raise_for_status()
    return datetime.datetime.strptime(response.json()[0]['date'], "%Y-%m-%d").date()


def main():
    load_dotenv()
    token = os.environ['api_key']

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
