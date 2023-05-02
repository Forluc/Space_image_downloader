from os.path import splitext
from urllib.parse import urlsplit


def get_img_format(url):
    split_url = urlsplit(url)
    img_format = splitext(split_url.path)
    return img_format[1]
