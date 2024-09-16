import time
import os
import random

name = input('Digite o que quer que eu escreva:\n')

possiblecharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,'
currentname = ''
currentletter = ''

for eachletter in name:
	while eachletter != currentletter:
		currentletter = random.choice(possiblecharacters)
		print(currentname+currentletter)
		time.sleep(0.05)
	currentname = currentname+currentletter
	currentletter = ' '

os.system('pause')