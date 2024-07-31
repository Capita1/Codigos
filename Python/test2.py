import time
mudar = bool(True)
print('Funciona')
a = True
while (True):
    if (a):
        mudar = True
        if mudar == True:
            a = False
    if a == False:
        mudar = False
        if mudar == False:
            a = True
    time.sleep(10/1000)
    print(mudar)

    