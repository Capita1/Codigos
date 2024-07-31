linha = ('==========================')

import time
num =input('numero ')
quantidade = input('quantas? ')
print (linha)

delay = 0
#vezes tem que ser 1 pra tabuada começar no 1
vezes = 1
quantidade = int(quantidade)

while (quantidade > 0):
    print ((vezes),' x ',(num),'=',int(num)*int(vezes))
    time.sleep(int(delay)/1000)
    quantidade = quantidade - 1
    vezes = vezes + 1
    if quantidade == 0:
        print ('cabo')
        break
    
