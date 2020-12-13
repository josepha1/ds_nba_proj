# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:44:58 2020

@author: Joseph Allen

Description: This Data Science project aims to use NBA Player data in order
             to predict the outcome(s) of the 2020-2021 NBA Season.
"""

from bb_scraper import bb_stat_scraper
import pandas as pd

bb_df = bb_stat_scraper()

bb_df.to_csv('nba_stats.csv', index = False)


