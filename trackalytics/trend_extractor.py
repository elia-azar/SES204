import pandas as pd

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
    d={'avg_monthly_growth':m.mean(axis=1)*100,'lowest_monthly_growth':m.min(1)*100,
    'highest_monthly_growth':m.max(1)*100}
    final=pd.DataFrame(d)
    print(final)

print_trend(only_youtube)
print_trend(famous_everywhere)