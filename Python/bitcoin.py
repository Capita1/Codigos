#!/usr/bin/python3
import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt
import numpy as np
import urllib.request, json, time, datetime

delay=30
x = []
y = []
loop = True

while(loop):
    data = json.load(urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json"))
    h = (str(datetime.datetime.now().time()))[:8]
    btc = float((data['bpi']['USD']['rate'])[:2])*1000+float((data['bpi']['USD']['rate'])[3:])
    print(f'{h} -> ${btc}') 
    x.append(h)
    y.append(btc)
    for s in range(delay):
        time.sleep(1)
        print(f'\t[{30-s}]',end='\r')

    if (x == 5):
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(xlabel='hora', ylabel='USD',
               title='Bitcoin')
        ax.grid()

        fig.savefig("test.png")
        plt.show()
