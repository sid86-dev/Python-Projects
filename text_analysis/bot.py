from instabot import Bot
from rich.console import Console
import os

console = Console()

# bot.upload_photo('download.jfif', caption="Bot testing!")

def get_data(username):
    bot = Bot()
    bot.login(username='avi.ral27', password='fuckboy2021')

    # get followers
    followers = bot.get_user_followers(username)
    all_followers = []
    n = 0
    with open('followers.txt', 'a') as f:
        for follower in followers:
            info = bot.get_username_from_user_id(follower)
            all_followers.append(info)
            f.write(f"{info}>>")
            console.print(f"{n} done")
            n+=1
    
    # console.print(all_followers)

    # get followings
    followings = bot.get_user_following(username)
    all_followings = []
    n = 0
    with open('followings.txt', 'a') as f:
        for follower in followings:
            info = bot.get_username_from_user_id(follower)
            all_followings.append(info)
            f.write(f"{info}>>")
            console.print(f"{n} done")
            n+=1

    process_data(followings=all_followings, followers=all_followers)



def process_data(followings, followers):
    for following in followings:
        if following not in followers:
            console.print(following)



def delete_config():
    dir = "config"

    path = f"{os.getcwd()}\\{dir}"
    
    os.remove(path)
    

get_data("sid86__")
# delete_config()
