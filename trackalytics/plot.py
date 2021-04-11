import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import savefig
import numpy as np

dir = 'data/'

people = [
    # "cyriak",
    # "Fluffeetalks",
    # "mrpeistar",
    # "freddiew2",
    # "RobTopGames",
    # "themarkofj",
    # "Maximilianmus",
    # "Maxmoefoepokemon",
    # "Mrddlms"
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
    "youtube",
    "twitch",
    "twitter"
]

for person in people:
    df_youtube = pd.read_csv(dir+person+'_youtube.csv').rename(columns={"Followers": "Youtube"}).sort_values(by='Date')
    df_twitter = pd.read_csv(dir+person+'_twitter.csv').rename(columns={"Followers": "Twitter"}).sort_values(by='Date')
    df_twitch = pd.read_csv(dir+person+'_twitch.csv').rename(columns={"Followers": "Twitch"}).sort_values(by='Date')

    df_youtube.set_index('Date', inplace=True)
    df_twitter.set_index('Date', inplace=True)
    df_twitch.set_index('Date', inplace=True)

    df = df_youtube.merge(df_twitter.merge(df_twitch, how='outer', on='Date'), how='outer', on='Date')
    df = df.dropna()

    mask = np.triu(np.ones_like(df.corr(), dtype=bool))

    svm = sns.heatmap(df.corr(), mask=mask, annot = True,cmap='coolwarm')
    figure = svm.get_figure()
    #figure.savefig('images/'+person+'_correlation.png')
    #figure.savefig('images_youtube_only/'+person+'_correlation.png')
    figure.savefig('images_multiplatform/'+person+'_correlation.png')

    plt.ylabel(person+' Followers')
    plt.xlabel("Date")
    df.to_csv("data/"+person+".csv")
    df.plot()
    plt.xticks(rotation=20)
    #plt.savefig('images/'+person+'.png')
    #plt.savefig('images_youtube_only/'+person+'.png')
    plt.savefig('images_multiplatform/'+person+'.png')

    df=(df-df.min())/(df.max()-df.min())

    plt.ylabel(person+' Followers Normalized')
    plt.xlabel("Date")
    df.plot()
    plt.xticks(rotation=20)
    #plt.savefig('images/'+person+'_scaled.png')
    #plt.savefig('images_youtube_only/'+person+'_scaled.png')
    plt.savefig('images_multiplatform/'+person+'_scaled.png')
