import pandas as pd
import os
import matplotlib.pyplot as plt
  
dir = 'data'

people = [
    "kyliejenner",
    #"jayz",
    "kimkardashian",
    "justinbieber",
    "cristiano",
    "krisjenner",
    "therock",
    "danbilzerian",
    "jenselter",
    "marzia",
    "khloekardashian",
    "pewdiepie",
    "beyonce",
    "kendalljenner",
    "kinbach",
    "amrezy"
]

medias = [
    "youtube",
    "instagram",
    "twitter"
]

dfs = {}

for person in people:
    dfs.update({person:[]})

for csvfile in os.scandir(dir):
    if csvfile.is_file():
        filename = csvfile.path
        for person in people:
            if person in filename:
                for media in medias:
                    if media in filename:
                        dfs.get(person).append(pd.read_csv(filename).rename(columns={"Subs": media}))
                        break
                break
        

for key in dfs.keys():
    df_list = dfs.get(key)
    '''
    if len(df_list) == 0:
        continue
    elif len(df_list) == 1:
        df = df_list[0]
    elif len(df_list) == 2:
        df = df_list[0].merge(df_list[1], how='outer', on='Date')
    else:
        df = df_list[0].merge(df_list[1].merge(df_list[2], how='outer', on='Date'), how='outer', on='Date')
    '''
    for df in df_list:
        if 'instagram' in df.columns:
            df.set_index('Date', inplace=True)
            #print(df.info())
            #print(df.describe())
            plt.ylabel('Instagram Followers')
            plt.xlabel("Date")
            df.plot()#.get_figure().savefig(key+'.png')
            plt.xticks(rotation=20)
            plt.savefig(key+'.png')