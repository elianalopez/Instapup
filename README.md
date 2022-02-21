# UPDATE :
## The bot is no longer in service since it has been shadow banned by instagram so I am unable to post. 
* This is probably due to the fact that the bot uploads photos in a consistent manner
# Instapup
An Instagram bot that attempts to upload a photo of a dog every 5 minutes!

## Tools

* VSCode
* Python 3.8.5

### Python Libraries & modules

* Instabot
* Beautiful Soup
* dontenv
* requesting
* random
* threading

## Project Overview

### Local Project Structure

![local](project_images/local_structure.png)

#### Local Structure in Depth

##### Code
 A folder that contains bot.py, clean.py, and and image.py.
 
##### bot.py

The instagram bot file that utilizes the instabot library to log in and upload photos on instagram. Photos are randomly chosen and reploaded again every 300 seconds. Photos are lastly discarded, and the files are remainded dog1.jpg.REMOVE_ME 
 
##### clean.py

Would analyze the image folder that bot.py has interacted with and would remove all files that end with .REMOVE_ME. Would remove all files every 300 seconds. 

##### image.py

Utilized the Beautiful Soup library to randomly webscrap images from Google Images.

Search terms are defined in a dictionary and then one is randomly chosen by key term value. 
```Python
SEARCH= {"dog": 1, "dogs":2, "pupper":3, "puppers":4, "puppy":5,"doggo":6, "doggie:":7, "cute dogs":8, "small puppies":9, "puppies":10, "doggies":11}
```

```Python
#A portion of download_images()
 def download_images():
     data = random.choice(list(SEARCH))
     print(f"searching for {data}")
     num_images = randint(1,80)
     print('searching...')
```
After that the number of images for that search term is then chosen out of a maximum of 80 files. 


 ### Heroku Deployment Structure
 
![heroku](project_images/heroku_structure.png)

#### Heroku Structure in Depth

##### Code

 A folder that contains bot.py and a modified combination of clean.py and image.py.
 The combination was due to the limit of 2 free dynos. 
 
 Within the code folder:
 
 * bot.py
 * image.py
 * images
 
##### Procfile
 
 A file that declares what commands Heroku should run.
 
##### requriments.txt

A text file that make sures heroku is able to install all the libraries needed for the program.


Created with this command
```pip freeze > requirements.txt```
 
##### runtime.txt

Lets heroku know what Python version the program is using.
 
## Project Images

<p align="center"><img src="https://raw.githubusercontent.com/elianalopez/Instapup/main/project_images/instapup1.jpeg" width="30%" height="30%"></p>

<br>

<p align="center"><img src="https://raw.githubusercontent.com/elianalopez/Instapup/main/project_images/feed.jpeg" width="30%" height="30%"></p>

<br>

<p align="center"><img src="https://raw.githubusercontent.com/elianalopez/Instapup/main/project_images/instapup.gif" width="30%" height="30%"></p>

