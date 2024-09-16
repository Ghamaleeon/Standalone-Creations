import os
import colorsys
import itertools
from PIL import Image

for folder in ['Output']:
	if not os.path.exists(folder):
		os.makedirs(folder)
		print('A pasta "' + folder + '" não foi encontrada, uma nova foi criada.')

tones = int(input("Quantos tons de cor?\n"))
it = [0]

for each in range(1, tones + 1):
	each = round((255/tones)*each)
	it.append(each)

it = [it, it, it]

try:
	pal = []
	for tup in itertools.product(*it): pal.append(tup)
	pal.sort()
	image = Image.new('RGB', (len(pal), 1))
	for color in range(len(pal)): image.putpixel((color, 0), pal[color])

	image.save('Output/Paleta '+str(len(pal))+'.png', 'PNG')
	print('Paleta de ' + str(len(pal)) + ' cores criada!')
except: print('Houve um erro')

os.system('pause')
