# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:04:44 2022

@author: josh.smith
"""

from bs4 import BeautifulSoup
import requests
import re
import geocoder

def webscrape(city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    g = geocoder.ip('me')
    city = g.city
    state = g.state
    #city='Nashville'
    print('searching for weather in...%s'%(city))
    city = city+' '+ state +' weather'
    print('searching for weather in...%s'%(city))
    city = city +' weather'
    city=city.replace(' ','+')
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    news_res = requests.get('https://www.allsides.com/')
    res.status_code == requests.codes.ok
    news_res.status_code == requests.codes.ok
    #USED TO HALT A BAD DOWNLOAD
    try:
        res.raise_for_status()
        news_res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    read = BeautifulSoup(res.text,'html.parser')
    read_news = BeautifulSoup(news_res.text,'html.parser')
    try:
        location = read.select('#wob_loc')[0].getText().strip()  
        time = read.select('#wob_dts')[0].getText().strip()       
        info = read.select('#wob_dc')[0].getText().strip() 
        weather = read.select('#wob_tm')[0].getText().strip()
        weather_info =[location, time, info, weather]
    
        counter = 0
        hyper_set=set([])
        title_set = set([])
        #compile list of titles from the entire website
        
        #CHANGE THIS SO IT PICKS RANDOM TITLES FROM THE LIST OF TITLES
        for i in read_news.find_all(class_='news-title'):
            if counter == 5:
                counter = 0
                break
            else:
                counter+=1
                title_set.add(i.getText())
                print(i.getText())
                
        #CODE FOR GETTING A LIST OF HYPERLINKS - MAYBE TRY TO LINK IT WITH THE TITLES
        #THEN PASTE THE LINKS INTO A NOTEPAD?
        # for link in read_news.find_all('a', attrs={'href': re.compile("^https://")}):       
        #     #get the top 5 results
        #     if counter == 5:
        #         break
        #     else:
        #         #look for specific links
        #         if 'https://www.allsides.com/news/' in link.get('href') and link.get('href') != 'https://www.allsides.com/news/rss':
        #             counter +=1      
        #             #add url to unique set
        #             hyper_set.add(link.get('href'))
        #             print(link.get('href'))
        #         else:continue
    except: 
        print('invalid search')
    return(weather_info,title_set)
