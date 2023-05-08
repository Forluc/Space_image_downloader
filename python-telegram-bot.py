import os
import time
import random
import telegram.ext
from dotenv import load_dotenv
from os.path import join


def main():
    load_dotenv()
    token = os.environ['TG_API_TOKEN']
    bot = telegram.Bot(token=token)

    chat_id = os.environ['TG_CHAT_ID']
    time_delay = os.environ['TIME_DELAY']

    images = []
    for root, dirs, files in os.walk("img"):
        for filename in files:
            images.append(filename)

    while True:
        for filename in images:
            try:
                path = join('img', filename)
                with open(path, 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(int(time_delay))
            except telegram.error.NetworkError as error:
                print(f'An error occurred: {error}')
                time.sleep(30)
        random.shuffle(images)


if __name__ == '__main__':
    main()
