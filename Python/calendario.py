import calendar, os
resolucao=('900x480')
fonte=('black')
fundo=('white')
yy = int(input("Ano: "))
mm = int(input("Mês: "))

arquivo=(f'{yy}-{mm}')
print(calendar.month(yy, mm))
calendario = (calendar.month(yy, mm))

os.system(f'magick -size {resolucao} canvas:none -pointsize 72 -draw "fill {fonte} text 25,60 \'{calendario}\'" {arquivo}.png')
os.system(f'magick {arquivo}.png -background {fundo} -flatten -alpha off {arquivo}.png')
