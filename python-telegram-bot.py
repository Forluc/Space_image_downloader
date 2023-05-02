import os
import time

import telegram.ext
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['api_token_tg']
bot = telegram.Bot(token=TOKEN)

chat_id = os.environ['chat_id_cosmos']
bot.send_message(chat_id=chat_id,
                 text="Привет, в этой группе ты найдешь много замечательных фотографий связанных с космосом!")
