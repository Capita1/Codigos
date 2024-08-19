#!/usr/bin/python3
import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt
import pandas as pd 
import urllib.request, json 
import time, datetime

while (True):
    data = json.load(urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json"))
    h = (datetime.datetime.now().time())
    h = str(h)
    print(f'{h[:8]} -> ${data['bpi']['USD']['rate']}') 
    time.sleep(30)
        
