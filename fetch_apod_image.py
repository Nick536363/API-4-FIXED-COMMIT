from requests import get
from save_tools import download_image
from argparse import ArgumentParser
from os import getenv


def main():
    api_key = getenv("APOD_EPIC_API")
    parser = ArgumentParser(description = "Данный файл скачивает фотографии с сервиса NASA APOD (Astronomy Picture of the Day)")
    parser.add_argument("--folder", type=str, default="./", help="Папка, куда будут скачаны картинки")
    parser.add_argument("count", type=int, help="Кол-во скачиваемых картинок")
    args = parser.parse_args()
    url_apod = "https://api_key.nasa.gov/planetary/apod"
    payload = {
        "api_key": api_key,
        "count": args.count
    }
    response_apod = get(url_apod, params=payload)
    response_apod.raise_for_status()
    for element_num, content in enumerate(response_apod.json(), 1):
        filename = f"apod_{element_num}.png"
        apod_link = content["url"]
        download_image(apod_link, args.folder, filename, api_key=api_key)


if __name__ == "__main__":
    main()
