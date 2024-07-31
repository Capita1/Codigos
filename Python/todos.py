import os, time
import sys
import logging

reset = ('REINICIANDO...')
linha = ('=================')

print ('1. vezes \n2. net \n3. porcentagem \n4. loop')
print (linha)
escolha = input('escolha o que quer fazer ')
escolha = int(escolha)
print (linha)

retry = 0
delay = 0

if escolha == 1:
        num = input('numero ')
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
                retry = retry + 1

                
if escolha == 2:
    net = input('velocidade da net?')
    print (linha)
    print(int(net)/8,'Megabytes por segundo')
    print (linha)
    print(int(net)/8*60,'Megabytes por minuto')
    print (linha)
    print(int(net)/8*60*60,'Megabytes por hora')
    print (linha)
    retry = retry + 1


if escolha == 3:
    nm = input('numero que você quer saber a porcentagem')
    cem = input('numero quivalente a 100%')
    print (linha)
    print ((nm),'é',int(nm)*100/int(cem),'% de',(cem))
    print (linha)
    retry = retry + 1


if escolha == 4:
    a = input('cima ')
    print (linha)
    b = input('baixo ')
    print (linha)
    print ('1000ms = 1 segundo')
    dly = input('delay? (milisegundos) ')
    print (linha)
    quanti = input('quantas vezes?')
    print (linha)
    quanti = int(quanti)
    while (quanti > 0):
        print (a)
        time.sleep(int(dly)/1000)
        print (b)
        time.sleep(int(dly)/1000)
        quanti = quanti - 1
        if quanti == 0:
            retry = retry + 1
            break


#essa parte tem que ser a ultima        
if retry == 1:
    cabo = input('aperte qualquer tecla pra sair')
    time.sleep(int(delay)+1)
    print (reset)
    time.sleep(int(delay)+2)
    quit()
    retry = retry - 1
    
