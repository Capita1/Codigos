linha = ('==========================')

import time

print (linha)
print ('1000ms = 1 segundo') 
delay = input('delay? (milisegundos) ')
print (linha)
quantidade = input('quantas vezes?')
print (linha)

quantidade = int(quantidade)

while (quantidade > 0):
    print ('|')
    time.sleep(int(delay)/1000)
    print (' |')
    time.sleep(int(delay)/1000)
    print ('   |')
    time.sleep(int(delay)/1000)
    print ('    |')
    time.sleep(int(delay)/1000)
    print ('    |')
    time.sleep(int(delay)/1000)
    print ('   |')
    time.sleep(int(delay)/1000)
    print ('  |')
    time.sleep(int(delay)/1000)
    print (' |')
    time.sleep(int(delay)/1000)
    
    quantidade = quantidade - 1
