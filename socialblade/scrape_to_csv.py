#https://github.com/vastava/data-science-projects/tree/master/content%20cop
#Code adapted to our situation

import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd


links = [
"http://web.archive.org/web/20190610195257/https://socialblade.com/youtube/user/pewdiepie/monthly"
,"http://web.archive.org/web/20160323052512/http://socialblade.com/youtube/user/justinbieber/monthly"
,"http://web.archive.org/web/20160704192632/http://socialblade.com/youtube/user/therock/monthly"
,"http://web.archive.org/web/20160817104057/http://socialblade.com/youtube/user/beyonce/monthly"
,"http://web.archive.org/web/20150505024528/http://socialblade.com/youtube/user/jayz/monthly"
,"http://web.archive.org/web/20190820165753/https://socialblade.com/twitter/user/pewdiepie/monthly"
,"http://web.archive.org/web/20170202010002/http://socialblade.com/twitter/user/justinbieber/monthly"
,"http://web.archive.org/web/20201205124155/https://socialblade.com/twitter/user/therock/monthly"
,"http://web.archive.org/web/20170202115033/http://socialblade.com/twitter/user/kimkardashian/monthly"
,"http://web.archive.org/web/20190709073053/https://socialblade.com/twitter/user/cristiano/monthly"
,"http://web.archive.org/web/20210122132351/https://socialblade.com/twitter/user/kyliejenner/monthly"
]
others =[
"http://web.archive.org/web/20191220215306/https://socialblade.com/instagram/user/pewdiepie/monthly"
,"http://web.archive.org/web/20201110193852/https://socialblade.com/twitch/user/pewdiepie/monthly"
,"http://web.archive.org/web/20150111204150/http://socialblade.com/instagram/user/marzia/monthly"
,"http://web.archive.org/web/20170225064447/http://socialblade.com/instagram/user/justinbieber/monthly"
,"http://web.archive.org/web/20170118231432/http://socialblade.com/instagram/user/therock/monthly"
,"http://web.archive.org/web/20160725061249/http://socialblade.com/instagram/user/kimkardashian/monthly"
,"http://web.archive.org/web/20160506132305/http://socialblade.com/instagram/user/cristiano/monthly "
,"http://web.archive.org/web/20160510115320/http://socialblade.com/instagram/user/kyliejenner/monthly "
,"http://web.archive.org/web/20150915031751/http://socialblade.com/instagram/user/khloekardashian/monthly "
,"http://web.archive.org/web/20151008012042/http://socialblade.com/instagram/user/krisjenner/monthly"
,"http://web.archive.org/web/20151023090106/http://socialblade.com/instagram/user/kendalljenner/monthly"
,"http://web.archive.org/web/20150115214147/http://socialblade.com/instagram/user/beyonce/monthly"
,"http://web.archive.org/web/20150309044321/http://socialblade.com/instagram/user/jenselter/monthly"
,"http://web.archive.org/web/20150716165333/http://socialblade.com/instagram/user/kingbach/monthly"
,"http://web.archive.org/web/20150911221051/http://socialblade.com/instagram/user/danbilzerian/monthly"
,"http://web.archive.org/web/20150902004630/http://socialblade.com/instagram/user/amrezy/monthly"
]

def scrape(url, var):
    r = req.get(url)
    print(r.status_code)
    soup = bs(r.text, 'lxml')
    script_divs = soup.find_all('script', {'type': 'text/javascript'})
    res = 0
    for i in range(len(script_divs)):
        if "CSV" in str(script_divs[i]):
            #print(script_divs[i])
            if var == '1':
                res = script_divs[i]
            elif var == '2':
                res = script_divs[i + 1]
            break
    lst = str(res).split('+')
    lst = [test.strip() for test in lst]
    lst = [test.replace('\\n"', '').replace('"', '') for test in lst]
    return lst


def to_df(url, var):
    lst = scrape(url, var)
    #print(len(lst))
    lst = lst[1:len(lst) - 1]
    df = pd.DataFrame()
    df['Date'] = [x.split(',')[0] for x in lst]
    df['Subs'] = [x.split(',')[1] for x in lst]

    return df

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    for link in links:
        name = link.split('/')[8] + "_" + link.split('/')[10]
        df=to_df(link, '2')
        df.to_csv("data/"+name+'.csv', index=False)
    for link in others:
        name = link.split('/')[8] + "_" + link.split('/')[10]
        df=to_df(link, '1')
        df.to_csv("data/"+name+'.csv', index=False)