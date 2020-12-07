# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:53:51 2020

@author: Joseph Allen

Description: This is a web scraper that scrapes player statistical data
             from Basketball-Reference.com
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def bb_stat_scraper():
    
    # NBA season we will be analyzing
    year = 2020
    
    # URL page we will be scraping
    url = 'https://www.basketball-reference.com/leagues/NBA_2020_per_game.html'.format(year)
    
    # This is the HTML from the give URL
    html = urlopen(url)
    
    # Creat a BeautifulSoup object by passing through html
    soup = BeautifulSoup(html, features = 'lxml')
    
    # Use findAll() to get the column headers
    soup.findAll('tr', limit = 2)
    
    # use getText() to extract the text we need to a list
    headers = [th.getText() for th in soup.findAll('tr', limit = 2)[0].findAll('th')]
    
    # Exclude the first column as we will not need the ranking order
    # from Basketball Reference for the analysis
    headers = headers[1:]
    
    # Avoid the first headers row
    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))]
    
    stats = pd.DataFrame(player_stats, columns = headers)
    
    return stats
