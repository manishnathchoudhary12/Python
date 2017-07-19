import urllib.request
import json
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

def pull_game(year, month, day, game):
    
    #URL
    url="http://www.mlb.com/gdcross/components/game/mlb/year_ID1/month_ID2/day_ID3/ID4/inning/inning_all.xml"
    url=url.replace('ID1', year).replace('ID2', month).replace('ID3', day).replace('ID4', game)
    
    #Dictionary
    columns=['break_y','ax','ay','az', 'year', 'batter','game','inning']
    all_col={}
    for column in columns:
        all_col[column] = []
      
    #Scrape Data
    gameURL = urllib.request.urlopen(url).read()
    gameSoup = BeautifulSoup(gameURL,"lxml")
    atBat = gameSoup.find_all('inning')

    for i,inning in enumerate(atBat):
        inning_num = inning['num']
        batters = atBat[i].find_all('atbat')
        for y, batter in enumerate(batters):
            batter_num=batter['num']
            pitches = batters[y].find_all('pitch')
            for pitch in pitches:
                all_col['year']=year
                all_col['batter'].append(batter_num)
                all_col['game']=game
                all_col['inning'].append(inning_num)
                
                try:
                    all_col['break_y'].append(pitch['break_y'])
                    all_col['ax'].append(pitch['ax'])
                    all_col['ay'].append(pitch['ay'])
                    all_col['az'].append(pitch['az'])
                
                except:
                                                             
                    all_col['break_y'].append(0)
                    all_col['ax'].append(0)
                    all_col['ay'].append(0)
                    all_col['az'].append(0)
                                
    all_game = pd.DataFrame.from_dict(all_col)

    return all_game


#Pull data for specified years
years = ['2015']#, '2016']
months = ['04','05','06']#,'07','08','09','10']
days = list(range(6,8))


baseball_data=pd.DataFrame()
for year in years:
    for month in months:
        for day in days:
            if day<10:
                day='0'+str(day)
            else:
                day=str(day)
            #print(year,month,day)
            try:
                temp=day_games(year, month, str(day))
                baseball_data=pd.concat([baseball_data, temp], axis=0)
                time.sleep(3)
                
            except:
                pass

    
baseball_data.head()
#baseball_data.to_csv('C:/GTP/Programming/Baseball/Data/baseball2.csv')