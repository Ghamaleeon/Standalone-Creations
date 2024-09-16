import os
import colorsys
from PIL import Image

def rgb_to_hsv(rgb):
	r = rgb[0]
	g = rgb[1]
	b = rgb[2]
	return colorsys.rgb_to_hsv(r,g,b)

for folder in ['Input', 'Output']:
	if not os.path.exists(folder):
		os.makedirs(folder)
		print('A pasta "' + folder + '" não foi encontrada, uma nova foi criada.')

for image in os.listdir('Input'):
	imagename = image
	print('Gerando paleta de ' + imagename + '...')
	try:
		image = Image.open('Input/' + imagename)
		pal = []
		
		for x in range(image.width):
			for y in range(image.height):
				if not image.getpixel((x, y)) in pal: pal.append(image.getpixel((x, y)))
				if len(pal) > 255: break
			if len(pal) > 255: break
		pal.sort(key=rgb_to_hsv)
		
		image = Image.new('RGB', (len(pal), 1))
		for color in range(len(pal)): image.putpixel((color, 0), pal[color])
		
		image.save('Output/' + imagename[:-4] + '.png', 'PNG')
		print('Paleta de ' + imagename + ' criada!')
	except: print(imagename + ' falhou.')

print('\nTodas as imagens foram processadas.')
os.system('pause')
