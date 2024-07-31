def conversao(uni, temp):
    conversoes = ['Invalido', int(temp)*1.8+32, int(temp)-32/1.8, int(temp)+273.15, int(temp)-273.15, int(temp) + 459.67 / 1.8, int(temp)*1.8-459.67]
    return (conversoes[uni])
sele = ['===============','de °C para °F','de °F para °C','de °C para K ','de K para °C ','de °F para K ','de K para °F ']
print (f'1 = {sele[1]}\n2 = {sele[2]}\n3 = {sele[3]}\n4 = {sele[4]}\n5 = {sele[5]}\n6 = {sele[6]}')
unidade = int(input(f'Escolha: '))
if unidade > 0 and unidade < 7:
    temperatura = input(f'{sele[0]}\n{sele[unidade]}\nTemperatura:')
    print (f'{sele[0]}\n{temperatura}{sele[unidade][3]}{sele[unidade][4]} equivalem a {conversao(unidade, temperatura)}{sele[unidade][10]}{sele[unidade][11]}{sele[unidade][12]}')