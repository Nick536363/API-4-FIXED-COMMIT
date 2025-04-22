from telegram import Bot
from os import walk,getenv
from random import choice
from time import sleep
from argparse import ArgumentParser
from dotenv import load_dotenv, find_dotenv

def main():
    load_dotenv(find_dotenv())
    tg_api_key = getenv("TELEGRAM_API")
    publish_frequency = getenv("PUBLISH_FREQ")
    parser = ArgumentParser(description="Данный файл публикует картинки в телеграмм канал")
    parser.add_argument("folder", type=str, default=".",help="Папка, откуда буду отправлены картинки")
    parser.add_argument("chat_id", type=str, help="Айди телеграм канала, куда будут опубликованы картинки (без @)")
    args = parser.parse_args()
    bot = Bot(token=tg_api_key)
    image_count = 1
    files = []
    sended = []
    for image in walk(args.folder):
        files.append(image)
        
    while True:
        try:
            file = choice(files[0][2])
            if file in sended:
                continue
            sended.append(file)
            with open(f"{args.folder}\{file}","rb") as opened_file:
                bot.send_photo(chat_id="@"+args.chat_id,photo=opened_file)
            
            sleep(int(publish_frequency))
            image_count+=1
        except KeyboardInterrupt:
            break
        if image_count > len(files[0][2]):
            sended = []
            image_count = 1
            continue


if __name__ == "__main__":
    main()
