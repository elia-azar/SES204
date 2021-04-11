import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import savefig

dir = 'data/'

only_youtube = [
    "cyriak",
    "Fluffeetalks",
    "mrpeistar",
    "freddiew2",
    "RobTopGames",
    "themarkofj",
    "Maximilianmus",
    "Maxmoefoepokemon",
    "Mrddlms"
]

famous_everywhere = [
    "pokimane",
    "maangchi",
    "Jazzghost",
    "TypicalGamer",
    "yomama",
    "Cinnamontoastken",
    "dodoeskabak",
    "gotaga",
    "Deligracy"
]

medias = [
    "youtube"
]

df_only_youtube = 0

def print_trend(channels):
    df = 0
    for channel in channels:
        df_channel = pd.read_csv(dir + channel + "_youtube.csv").rename(columns={"Followers": "Subscribers"}).sort_values(by='Date')

        df_channel = df_channel[df_channel.Date.astype(str).str.contains("01$")]
        df_channel['Channel'] = channel

        if type(df) is int:
            df = df_channel
        else:
            df = pd.concat([df, df_channel])

    m=df.pivot_table(index = 'Channel', columns='Date',values='Subscribers').pct_change(axis=1)
    
    return np.array(m.mean(axis=1)*100).reshape((9,1))
    

x1 = print_trend(only_youtube)
x2 = print_trend(famous_everywhere)
x = np.concatenate((x1,x2),axis=1)

plt.title("Average monthly growth for each channel")
plt.hist(x, 9, histtype='bar', label=["only youtube", "multiplatform"])
plt.legend(("only youtube", "multiplatform"))
plt.savefig('images/mean_monthly_growth.png');
