#!/usr/bin/python3
import matplotlib
matplotlib.use('module://matplotlib-backend-kitty')
import matplotlib.pyplot as plt
import pandas as pd 
import urllib.request, json 

data = json.load(urllib.request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json"))
valor = (data['bpi']['USD']['rate'])

print(valor)

