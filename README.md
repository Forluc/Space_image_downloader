# Программа для скачивания фотографий космоса(+скрипт для телеграм бота)
Скрипты позволяют скачивать фото APOD NASA, EPIC NASA, запуски ракет от SpaceX. А также скрипт телеграм бота для автоматического опубликовывания сообщений и медиафайлов в группу.
## Окружение
- Создайте файл ```.env``` в основном каталоге
### Требования к установке

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
``` 

### Получение API ключа для скачивания фотографий с сайта [NASA](https://api.nasa.gov/)

1. Прописать в файле переменную NASA_API_KEY со значением полученного токена на сайте [NASA](https://api.nasa.gov/)
2. .env содержит данные без кавычек


### Получение API токена telegram

1. Зарегистрировать бота ([инструкция](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html))
2. Прописать в файле переменную TG_API_TOKEN со значением полученного токена от [@BotFather](https://t.me/BotFather)
3. .env содержит данные без кавычек

### Присвоить значение TG_CHAT_ID для отправки медиафайлов в группу

1. Прописать в файле переменную TG_CHAT_ID со значением названия группы @example
2. .env содержит данные без кавычек

### Присвоить значение TIME_DELAY(не обязательное)

- По умолчанию TIME_DELAY=14400(4 часа)

1. Прописать в файле переменную TIME_DELAY со значением нужной задержки(в секундах) между отправкой медиафайлов и сообщений
2. .env содержит данные без кавычек

- Для примера, если прочитать файл .env можно увидеть следующее:

### Присвоить значение MEDIA_PATH(не обязательное)

- По умолчанию сохраняются в папку ```images``` 

1. Прописать в файле переменную MEDIA_PATH, в значение поставить нужное имя для папки
2. .env содержит данные без кавычек

```bash
$ cat .env
NASA_API_KEY=e2qq5HxalTZR1ZUxRx182n38ZrZzfbsT9jFoly8E
TG_API_TOKEN=5593251370:AAwetXpEn6E94EvZY8P1-uweDtXpEXAMPLE
TG_CHAT_ID=@example
TIME_DELAY=14400
MEDIA_PATH=example
```

## Запуск файла для скачивания фотографий [SpaceX](https://github.com/r-spacex/SpaceX-API)

Запуск на Linux(Python 3) или Windows:

Пример для скачивания фотографий последнего запуска:

```bash
$ python fetch_spacex_images.py
```

Пример для скачивания фотографий по нужному ID запуска:

```bash
$ python fetch_spacex_images.py --id 605b4b6aaa5433645e37d03f
```

Пример для скачивания фотографий в папку с другим именем:

```bash
$ python fetch_spacex_images.py --path example
```
![50291453997_aa715950e7_o](https://user-images.githubusercontent.com/75582238/235646218-469f5881-5f36-42a1-b95a-f337b7605c8b.jpg)


## Запуск файла для скачивания фотографий APOD [NASA](https://api.nasa.gov/)

Запуск на Linux(Python 3) или Windows:

Пример для скачивания фотографии дня:

```bash
$ python nasa_last_image_downloader.py
```
Пример для скачивания фотографий в папку с другим именем:

```bash
$ python nasa_last_image_downloader.py --path example
```
![apod](https://user-images.githubusercontent.com/75582238/235646328-79f9b69a-1d62-4eba-ad89-d772a4a46b22.jpg)


## Запуск файла для скачивания фотографий EPIC [NASA](https://api.nasa.gov/)

Запуск на Linux(Python 3) или Windows:

Пример для скачивания последней фотографии:

```bash
$ python epic_image_downloader.py
```

Пример для скачивания фотографий по нужной дате:

```bash
$ python epic_image_downloader.py --date 2023-04-28
```

Пример для скачивания последней фотографии в папку с другим именем:

```bash
$ python epic_image_downloader.py --path example
```

![epic_1b_20190530011359](https://user-images.githubusercontent.com/75582238/235646350-a1cfc15f-c015-4536-a836-e6146306e787.png)

## Запуск файла для автоматического опубликовывания в телеграм группу

Запуск на Linux(Python 3) или Windows:

Добавить в папку ```images``` медиафайлы.

После запуска скрипта, он будет бесконечное время опубликовывать медиафайлы. Если список файлов закончился, то он перемешает список и будет опубликовывать его заново.

```bash
$ python python-telegram-bot.py
```

## Цель проекта
Код был написан для удобства скачивания фотографий космоса и автоматического опубликовывания медиафайлов в телеграм.
