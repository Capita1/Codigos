#!/usr/bin/python3
import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt
import urllib.request, json, time, datetime

delay=30
x = []
y = []

while(True):
    data = json.load(urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json"))
    h = (str(datetime.datetime.now().time()))[:8]
    btc = data['bpi']['USD']['rate']
    print(f'{h} -> ${btc}') 
    x.append(h)
    y.append(btc)
    
    for s in range(delay):
        time.sleep(1)
        print(f'\t[{s}]',end='\r')
    if (len(x)==5):
        plt.plot(x,y)
        plt.show()

