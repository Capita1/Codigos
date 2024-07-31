vida = 100
attack1 =  10
mana = 100
batalha = 0
confronto = 0


import time, os

linha = ('===================')

nome = input('nome:')
print (linha)
print ('Bom dia',(nome),'. Escolha a classe')
print ('1. dps \n2. tank')
classe = input('escolha: ')
classe = int(classe)
print (linha)


if classe == 1:
    print ('Você escolheu dps')
    attack1 = attack1 + attack1
    
if classe == 2:
    print ('Você escolheu tank')
    vida = vida + vida

print ('OH MEU DEUS ESTÃO ATACANDO MINHA ALDEIA')
time.sleep(0.5)
print ('UM CYCLOP')
time.sleep(0.5)
print ('Vamos lá',(nome))
print (linha)
batalha = 1

cyclop = 300
cyclopD = 5

while batalha == 1:
    print ('O quer fazer?')
    time.sleep(0.5)
    print ('1. Ver status \n2. atacar')
    print (linha)
    confronto = input('escolha: ')
    print (linha)
    batalha = 0

confronto = int(confronto)

if confronto == 1:
    print ('Vida:',(vida),'\nMana:',(mana))
    print (linha)
    batalha = 1

  

