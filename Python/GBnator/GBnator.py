import os
import time
from PIL import Image

def GBfy():
	folder = os.listdir("Input")
	print("Found " + str(len(folder)) + " files")
	for images in folder:
		try:
			image = Image.open("Input\\" + images)
			min_val = 255
			max_val = 0
			print(images + " Loading colors...")
			for x in range(image.size[0]):
				for y in range(image.size[1]):
					pixel = image.getpixel((x,y))
					v = max(pixel[0], pixel[1], pixel[2])
					if v < min_val:
						min_val = min(pixel[0], pixel[1], pixel[2])
					if v > max_val:
						max_val = max(pixel[0], pixel[1], pixel[2])
			print(images + " Recoloring...")
			for x in range(image.size[0]):
				for y in range(image.size[1]):
					pixel = image.getpixel((x,y))
					v = max(pixel[0], pixel[1], pixel[2])
					try:
						a = pixel[3]
					except:
						a = None
					newr = 0
					newg = 0
					newb = 0
					
					if v <= (min_val + max_val) / 4:
						newr = 15
						newg = 56
						newb = 15
					elif v <= (min_val + max_val) / 2:
						newr = 48
						newg = 98
						newb = 48
					elif v <= (min_val + max_val) / 1.33:
						newr = 139
						newg = 172
						newb = 15
					else:
						newr = 155
						newg = 188
						newb = 15
					
					if not a == None:
						if not a <= 0:
							image.putpixel((x,y),(newr,newg,newb,a))
					else:
						image.putpixel((x,y),(newr,newg,newb))
					
			image.save("Output\\" + images)
			print(images + " Success")
		except:
			print(images + " Failed")

if not os.path.exists("Input"):
		os.makedirs("Input")
if not os.path.exists("Output"):
		os.makedirs("Output")

GBfy()

print("Done")
time.sleep(2)