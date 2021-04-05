import pandas as pd
from datetime import datetime

filenames = [
    "edsheeran_twitter",
    "edsheeran_youtube",
    "eminem_twitter",
    "eminem_youtube",
    "pewdiepie_twitter",
    "pewdiepie_youtube",
    "pewdiepie_twitch",
    "ramez_khaled_twitter",
    "volkan_korkmaz_twitter",
    "jasonsweeney_twitter",
    "lovetaza_twitter",
    "ninja_twitter",
    "ninja_youtube",
    "ninja_twitch",
    "mrbeast_twitter",
    "mrbeast_youtube"
]

for filename in filenames:
    lines = []
    with open("raw_data/"+filename + ".txt") as f:
        lines = f.readlines()

    date_followers = {
        'Date':[],
        'Followers':[]
    }
    count = 0
    length = len(lines)
    print(length)
    delimiter = "<br>" if "twitter" in filename  else '-'
    for i in range(length):
        if "</tr><tr" in lines[i]:
            count += 1
            day = lines[i+2].split("<td>")[1].split("</td>")[0]
            date = datetime.strptime(day, '%B %d, %Y')
            followers = int(lines[i+4].split("<td>")[1].split(delimiter)[0].strip().replace(',', ''))
            date_followers.get("Date").append(date)
            date_followers.get("Followers").append(followers)


    df = pd.DataFrame.from_dict(date_followers)
    df.drop_duplicates(subset=['Date'])

    df.to_csv("data/"+filename+'.csv', index=False)