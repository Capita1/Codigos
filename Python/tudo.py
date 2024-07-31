import time
def spinner(dly):
    spin=('/','-','\\','|')
    while True:
            for x in range(4):
                time.sleep(dly)
                print(spin[x])
def converTemp():
    convers=['===============','de °C para °F','de °F para °C','de °C para K ','de K para °C ','de °F para K ','de K para °F ']
    unidade = int(input(f'1 = {convers[1]}\n2 = {convers[2]}\n3 = {convers[3]}\n4 = {convers[4]}\n5 = {convers[5]}\n6 = {convers[6]}\nEscolha: '))
    temp=input(f'{convers[0]}\n{convers[unidade]}\nTemperatura:')
    calcs=['Invalido',(int(temp)*9/5)+32,(int(temp)-32)*5/9,int(temp)+273.15,int(temp)-273.15,int(temp)+459.67/1.8,int(temp)*1.8-459.67]
    if unidade > 0 and unidade < 7:
        print (f'{convers[0]}\n{temp}{convers[unidade][3]}{convers[unidade][4]} equivalem a {calcs[unidade]}{convers[unidade][10]}{convers[unidade][11]}{convers[unidade][12]}')
def convertS(s):
	h=s//3600
	m=(s%3600)//60
	s=(s%3600)%60
def convercaoIMC(n,a,p):
    if(M<16):
        i=0
    if(M>16 and 16.99>M):
        i=1
    if(M>17 and 18.49>M):
        i=2
    if(M>18.50 and 24.99>M):
        i=3
    if(M>25 and 29.99>M):
        i=4
    if(M>30 and 34.99>M):
        i=5
    if(M>35 and 39.99>M):
        i=6
    if(M>40):
        i=7
    classificacao=('Baixo peso muito grave','Baixo peso grave','Baixo peso','Peso normal','Sobrepeso','Obesidade grau I','Obesidade grau II','Obesidade grau III')
    print(f"{n} possui índice de massa corporal igual a {round(((p/((a/100)*(a/100)))*100)/100,2)} sendo classificado como {classificacao[i]}")

choice=int(input("1 = gira\n2 = conversão de temperatura\n3 = converter segundo em h:m:s\n4 = conversão do IMC\nEscolha: "))
if choice==1:
    dly=float(input('Delay em segundos:'))
    spinner(dly)
if choice==2:
    converTemp()
if choice==3:
    s = input('segundos: ')
    converS(s)
if choice==4:
    n=input('Seu nome:')
    a=float(input('Sua altura em centimetros:'))
    p=float(input('Seu peso em KG:'))
    convercaoIMC(n,a,p)
