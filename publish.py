from telegram import Bot
from os import walk,getenv
from random import choice
from time import sleep
from argparse import ArgumentParser
from dotenv import load_dotenv, find_dotenv

def publish(folder,chat_id,publish_frequency,api):
    bot = Bot(token=api)
    image_count = 1
    files = []
    sended = []
    for image in walk(folder):
        files.append(image)
        
    while True:
        try:
            file = choice(files[0][2])
            if file in sended:
                continue
            sended.append(file)
            with open(f"{folder}\{file}","rb") as opened_file:
                bot.send_photo(chat_id=chat_id,photo=opened_file)
            
            sleep(publish_frequency)
            image_count+=1
        except KeyboardInterrupt:
            break
        if image_count > len(files[0][2]):
            sended = []
            image_count = 1
            continue
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("folder", type=str, help="Папка, откуда буду отправлены картинки")
    parser.add_argument("chat_id", type=str, help="Айди телеграм канала, куда будут опубликованы картинки")
    args = parser.parse_args()
    load_dotenv(find_dotenv())
    publish(args.folder, args.chat_id, getenv("PUBLISH_FREQ"), getenv("TELEGRAM_API"))