# Программа для скачивания фотографий космоса

## Окружение

### Требования к установке

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

### Добавление ключа для скачивания фотографий с сайта [NASA](https://api.nasa.gov/)

- Создание API ключа

1. Создайте файл .env рядом с main.py
2. Прописать в файле переменную api_key со значением полученного токена на сайте [NASA](https://api.nasa.gov/)
3. .env содержит данные без кавычек

Для примера, если прочитать файл .env можно увидеть следующее:

```bash
$ cat .env
api_key=e2qq5HxalTZR1ZUxRx182n38ZrZzfbsT9jFoly8E
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
![50291453997_aa715950e7_o](https://user-images.githubusercontent.com/75582238/235646218-469f5881-5f36-42a1-b95a-f337b7605c8b.jpg)


## Запуск файла для скачивания фотографий APOD [NASA](https://api.nasa.gov/)

Запуск на Linux(Python 3) или Windows:

Пример для скачивания фотографии дня:

```bash
$ python nasa_last_image_downloader.py
```
![apod](https://user-images.githubusercontent.com/75582238/235646328-79f9b69a-1d62-4eba-ad89-d772a4a46b22.jpg)


## Запуск файла для скачивания фотографий [SpaceX](https://github.com/r-spacex/SpaceX-API)

Запуск на Linux(Python 3) или Windows:

Пример для скачивания последней фотографии:

```bash
$ python epic_image_downloader.py
```

Пример для скачивания фотографий по нужной дате:

```bash
$ python epic_image_downloader.py --date 2023-04-28
```
![epic_1b_20190530011359](https://user-images.githubusercontent.com/75582238/235646350-a1cfc15f-c015-4536-a836-e6146306e787.png)

## Цель проекта
Код был написан для удобства скачивания фотографий космоса
