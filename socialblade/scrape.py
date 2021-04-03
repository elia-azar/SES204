# https://github.com/vastava/data-science-projects/tree/master/content%20cop

import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


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
other =[
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

def sub_scraper(url, var):
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
#     print(res)
    lst = str(res).split('+')
    lst = [test.strip() for test in lst]
    lst = [test.replace('\\n"', '').replace('"', '') for test in lst]
    return lst


def to_df(url, name, var):
    lst = sub_scraper(url, var)
    print(len(lst))
    lst = lst[1:len(lst) - 1]
    df = pd.DataFrame()
    df['Date'] = [x.split(',')[0] for x in lst]
    df['Subs'] = [x.split(',')[1] for x in lst]
    df['Name'] = name
    return df


'''
def checkmonth(check, year, month, day):
    target = date(year, month, day)
    check = date.fromisoformat(check)
    bounds = [target + relativedelta(months=-1), target + relativedelta(months=+1)]
    if check >= bounds[0] and check <= bounds[1]:
        return True
    else: 
        return False
    
def filterdate(date_str, df):
    target = date.fromisoformat(date_str)
    month = target.month
    day   = target.day
    year = target.year
    return df[df['Date'].apply(checkmonth, args=(year, month, day))]
filterdate('2016-09-13', to_df(leafy, 'LeafyIsHere', 'count'))


dates = """2015-12-13
2016-02-02
2016-05-05
2016-08-12
2016-09-13
2017-02-06
2017-10-03""".splitlines()


names = """Jinx
Fine Bros
Keemstar
HowToPRANKItUp
LeafyIsHere
Tana Mongeau
Ricegum""".splitlines()

url_dict = {}



dfs = []
for i in range(len(names)):
    dfs.append(filterdate(dates[i], to_df(url_dict[names[i]], names[i], 'count')))

tot_dfs = []
for i in range(len(names)):
    tot_dfs.append(filterdate(dates[i], to_df(url_dict[names[i]], names[i], 'total')))

for i in range(len(dfs)):
    dfs[i]['Total'] = tot_dfs[i].Subs


pd.concat(dfs).to_csv('contentcop_v2.csv', index=False)

new = {}


cc_view_dfs = []
for key in url_dict.keys():
    if key == 'LeafyIsHere' or key == 'Keemstar':
        temp = to_df(url_dict[key], key, "views")
        temp2 = to_df(new[key], key, "views")
        cc_view_dfs.append(pd.concat([temp, temp2]).drop_duplicates())
    else:
        cc_view_dfs.append(to_df(url_dict[key], key, "views"))



for i in range(len(cc_dfs)):
    cc_dfs[i]['Views'] = cc_view_dfs[i].Subs

pd.concat(cc_dfs).to_csv('contentcop_all_v2.csv', index=False)

'''