linha = ('==========================')
a = input('cima ')
print (linha)
b = input('baixo ')
print (linha)

import time

print ('1000ms = 1 segundo') 
delay = input('delay? (milisegundos) ')
print (linha)
quantidade = input('quantas vezes?')
print (linha)

quantidade = int(quantidade)

while (quantidade > 0):
    print (a)
    time.sleep(int(delay)/1000)
    print (b)
    time.sleep(int(delay)/1000)
    quantidade = quantidade - 1
