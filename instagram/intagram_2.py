import instabot
import json

bot = instabot.Bot()
bot.login()

data = {}
with open('followers.json') as f:
    data = json.load(f)

followers = []

for person in data.get("relationships_followers"):
    followers.append(person.get("string_list_data")[0].get("value"))

followers_data = {}

for username in followers:
    user_id = bot.get_user_id_from_username(username)
    follower_count = bot.get_user_followers(user_id)
    print(username + ":" + str(follower_count))
    followers_data.update({username:follower_count})