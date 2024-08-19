#!/usr/bin/python3
import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import urllib.request, json, time, datetime
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

data = json.load(urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json"))
h = str(datetime.datetime.now().time())
btc = data['bpi']['USD']['rate']
print(f'{h[:8]} -> ${btc}') 
      
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):
    xs.append(h)
    ys.append(btc)

    xs = xs[-20:]
    ys = ys[-20:]

    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('BTC')
    plt.ylabel('Preço')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
