import threading
import os
import dotenv
from datetime import datetime
from dotenv import load_dotenv   #for python-dotenv method
from random import randint
from instabot import Bot

load_dotenv()                    #for python-dotenv method

USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

img_folder_path = 'images/'
max = os.listdir(img_folder_path)
print(len(max))



bot = Bot()

bot.login(username = USERNAME, password = PASSWORD)

def main():
    print(len(max))
    upload()
    threading.Timer(300.0, main).start()

def upload():
    try:
        num = randint(1, 75)
        bot.upload_photo(f"code/images/dog{num}.jpg", caption = "woof!")
        print("woof! (done)")

        #view current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        
    except:
        print("error has occured")

if __name__ == '__main__':
    main()
