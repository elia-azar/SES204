import instagram_private_api as ipa
import json
import time
import urllib
import socket

user_name = 'user'
password = 'password'

data = {}
with open('followers.json') as f:
    data = json.load(f)

followers = []

for person in data.get("relationships_followers"):
    followers.append(person.get("string_list_data")[0].get("value"))

followers_data = {}

api = ipa.Client(user_name,password)

while len(followers) != 0:
    try:
        username = followers[0]
        user_info = api.username_info(username)
        follower_count = user_info.get("user").get("follower_count")
        print(username + ":" + str(follower_count))
        followers_data.update({username:follower_count})
        followers.pop(0)
    except ipa.errors.ClientThrottledError as e:
        api.logout()
        api = ipa.Client(user_name,password)
        print(e)
        print("Still processing " + str(len(followers)) + " followers ...")
        time.sleep(10)
        continue
    except urllib.error.HTTPError as e:
        api.logout()
        api = ipa.Client(user_name,password)
        print(e)
        print("Still processing " + str(len(followers)) + " followers ...")
        time.sleep(10)
        continue
    except socket.timeout as e:
        api.logout()
        api = ipa.Client(user_name,password)
        print(e)
        print("Still processing " + str(len(followers)) + " followers ...")
        time.sleep(10)
        continue
