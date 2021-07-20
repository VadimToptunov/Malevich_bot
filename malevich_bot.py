import schedule
import time
from _datetime import datetime
import random
from instabot import Bot
from creds import Creds
from Malevich import avantguard


ag = avantguard.AvantGuard()


def generate_image():
    width = 1200
    height = 1200
    boolean = [True, False]
    return ag.generate_image(width, height, random.choice(boolean), random.choice(boolean),
                                      random.choice(boolean),
                                      random.choice(boolean), random.choice(boolean))


def post_image(file_path):
    credentials = Creds()
    bot = Bot()
    bot.login(username=credentials.LOGIN, password=credentials.PASS)
    image_name = str(file_path)[:-20]
    message = f"<b>Filename:</b> {image_name}\n<b>Time created:</b> {str(datetime.today())}"
    bot.upload_photo(file_path, caption=message)


if __name__ == "__main__":
    image = generate_image()
    schedule.every().day.at("18:00").do(post_image, file_path=image)
    while 1:
        schedule.run_pending()
        time.sleep(360)
