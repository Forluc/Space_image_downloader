import os
import time
import random
import telegram.ext
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ['api_token_tg']
    bot = telegram.Bot(token=token)

    chat_id = os.environ['chat_id_cosmos']
    time_delay = os.environ['time_delay']

    images = []
    for root, dirs, files in os.walk("img"):
        for filename in files:
            images.append(filename)

    while True:
        for filename in images:
            bot.send_document(chat_id=chat_id, document=open(f'img/{filename}', 'rb'))
            time.sleep(int(time_delay))
        random.shuffle(images)


if __name__ == '__main__':
    main()
