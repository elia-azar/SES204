import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import savefig
import numpy as np

dir = 'data/'

only_youtube = [
    "1utubaccount",
    "cyriak",
    "Fluffeetalks",
    "Maximilianmus",
    "Maxmoefoepokemon",
    "RobTopGames",
    "schoolboy"
]

famous_everywhere = [
    "anomaly",
    "Deligracy",
    "gameranx",
    "gotaga",
    "Jazzghost",
    "pokimane",
    "Stampylonghead",
    "TheSyndicateProject",
    "Typical_Gamer"
]

medias = [
    "youtube"
]

df_only_youtube = 0

for channel in only_youtube:
    df_channel = pd.read_csv(dir + channel + "_youtube.csv").rename(columns={"Followers": "Subscribers"}).sort_values(by='Date')

    df_channel = df_channel[df_channel.Date.astype(str).str.contains("01$")]
    df_channel['Channel'] = channel

    if type(df_only_youtube) is int:
        df_only_youtube = df_channel
    else:
        df_only_youtube = pd.concat([df_only_youtube, df_channel])


m=df_only_youtube.pivot_table(index = 'Channel', columns='Date',values='Subscribers').pct_change(axis=1)
d={'avg_monthly_growth':m.mean(axis=1)*100,'lowest_monthly_growth':m.min(1)*100,
   'highest_monthly_growth':m.max(1)*100}
final=pd.DataFrame(d)
print(final)


df_famous_everywhere = 0

for channel in famous_everywhere:
    df_channel = pd.read_csv(dir + channel + "_youtube.csv").rename(columns={"Followers": "Subscribers"}).sort_values(by='Date')

    df_channel = df_channel[df_channel.Date.astype(str).str.contains("01$")]
    df_channel['Channel'] = channel

    if type(df_famous_everywhere) is int:
        df_famous_everywhere = df_channel
    else:
        df_famous_everywhere = pd.concat([df_famous_everywhere, df_channel])


m=df_famous_everywhere.pivot_table(index = 'Channel', columns='Date',values='Subscribers').pct_change(axis=1)
d={'avg_monthly_growth':m.mean(axis=1)*100,'lowest_monthly_growth':m.min(1)*100,
   'highest_monthly_growth':m.max(1)*100}
final=pd.DataFrame(d)
print(final)