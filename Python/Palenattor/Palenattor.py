import os
from PIL import Image

for folder in ['Palettes','Input','Output']:
	if not os.path.exists(folder):
		os.makedirs(folder)
		print('A pasta "' + folder + '" não foi encontrada, uma nova foi criada.')

palettes = ['Nenhuma.png']
for each in (each for each in os.listdir('Palettes') if each.endswith('.png')): palettes.append(each)
print('Escolha uma das paletas disponíveis: (A escolha padrão é nenhuma)\n')
for each in palettes: print(str(palettes.index(each))+' '+each[:-4])
choice = input('\n')
if not choice.isdigit(): choice = palettes[0]
else: choice = palettes[max(min(int(choice), len(palettes)-1), 0)]

colornum = input('\nQuantas cores a imagem poderá ter?\nMínimo de 1 e máximo de 256. (O valor padrão é 256.)\n\n')
if not colornum.isdigit(): colornum = 256
else: colornum = max(min(int(colornum), 256), 1)

os.system('cls' if os.name == 'nt' else 'clear')
if not choice == palettes[0]:
	rgbValues = []
	pal = Image.open('Palettes/'+choice).convert('RGB')
	print('Carregando paleta...')
	for x in range(pal.width):
		for y in range(pal.height):
			pixel = pal.getpixel((x,y))
			if not pixel in rgbValues:
				rgbValues.append(pixel)
	rgbValues = list(sum(rgbValues, ()))*12
	rgbValues = rgbValues[:768]
	print('Paleta carregada.\n')

for each in os.listdir('Input'):
	print('Processando ' + each + '...')
	try:
		image = Image.open('Input/' + each).convert('RGB')
		if not choice == palettes[0]:
			palimage = Image.new('P', (image.width, image.height))
			palimage.putpalette(rgbValues)
			newimage = image.quantize(palette=palimage,dither=Image.Dither.NONE)
			if colornum < 256: newimage = newimage.quantize(colors=colornum,dither=Image.Dither.NONE)
		if choice == palettes[0]: newimage = image.quantize(colors=colornum,dither=Image.Dither.NONE)
		image = Image.open('Input/' + each)
		if image.mode == 'RGBA':
			newimage = newimage.convert('RGBA')
			for x in range(newimage.width):
				for y in range(newimage.height):
					oldpixel = image.getpixel((x,y))
					pixel = newimage.getpixel((x,y))
					newimage.putpixel((x,y),(pixel[0],pixel[1],pixel[2],oldpixel[3]))
		else: newimage.convert(image.mode)
		newimage.save('Output/' + each[:-4] + '.png', 'PNG')
		print(each + ' teve sucesso.')
	except: print(each + ' falhou.')
print('\nTodas as imagens foram processadas.')
os.system('pause')