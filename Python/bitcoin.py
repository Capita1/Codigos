#!/usr/bin/python3
import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import urllib.request, json, time, datetime
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

x = []
y = []

while(True):
    data = json.load(urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json"))
    h = (str(datetime.datetime.now().time()))[:8]
    btc = data['bpi']['USD']['rate']
    print(f'{h} -> ${btc}') 
    time.sleep(1)
#=========================================#      
