from requests import get
from save_tools import download_image
from argparse import ArgumentParser
from os import getenv


def main():
    api_key = getenv("APOD_EPIC_API")
    parser = ArgumentParser(description = "Данный файл скачивает фотографии с сервиса NASA EPIC (Earth Polychromatic Imaging Camera)")
    parser.add_argument("--folder", type=str, default="./", help="Папка, куда будут скачаны картинки")
    args = parser.parse_args()
    params = {"api_key": api_key}
    url_epic = "https://api.nasa.gov/EPIC/api/natural/images?"
    responce_epic = get(url_epic, params=params)
    responce_epic.raise_for_status()
    filename = "epic_image"
    for element_num, content in enumerate(responce_epic.json()):
        date = content["date"].split(" ")[0].split("-")
        url_image = f"https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{content["image"]}.png"
        download_image(url_image, args.folder, f"{filename}_{element_num}.png", api_key=api_key)


if __name__ == "__main__":
    main()
