uni_ex=['','Primeiro','Segundo','Terceiro','Quarto','Quinto','Sexto','Sétimo','Oitavo','Nono','Décimo']
dez_ex=['','Décimo','Vigésimo','Trigésimo','Quagragésimo','Quinquagésimo','Sextagésimo','Septuagésimo','Octagésimo','Nonagésimo']
cem_ex=['','Centésimo','Ducentésimo','Tricentésimo','Quadringentésimo','Quingentésimo','Seiscentésimo','Septingentésimo','Octingentésimo','Noningentésimo']
mil_ex=['','Milésimo']

u = int(input('Número: '))
unidade= 0
dezena=0
centena=0

#descobre o valor da unidade
unidade = u
while unidade >= 10:
    unidade -= 10

#descobre o valor da dezena
dezena = u
while dezena >= 100:
    dezena -= 100
dezena -= unidade
dezena /= 10
if False == isinstance(dezena, int):
    dezena = int(dezena)

#descobre o valor da centena
centena = u
while centena >= 1000:
    centena -= 1000
centena -= unidade
centena /= 100
if False == isinstance(centena, int):
    centena = int(centena)

print('============')
print (f'Indice:{centena}{dezena}{unidade}')
print (cem_ex[centena],dez_ex[dezena],uni_ex[unidade])
