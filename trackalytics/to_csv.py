import pandas as pd
from datetime import datetime
import os


dir = 'raw_data'

for csvfile in os.scandir(dir):
    if csvfile.is_file():
        filename = csvfile.path

for file in os.scandir(dir):
    if file.is_file():
        filename = file.path
        lines = []
        with open(filename) as f:
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
        new_filename = filename.split('/')[1].split('.')[0]
        df.to_csv("data/"+new_filename+'.csv', index=False)