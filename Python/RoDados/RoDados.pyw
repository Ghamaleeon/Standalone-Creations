import random as rand
import time
import winsound
import os
import tkinter as tk
from tkinter import messagebox

def play(soundname):
	winsound.PlaySound(soundname, winsound.SND_ASYNC)

def check_wav(name):
	name = name.split(".")
	if name[len(name) - 1] == "wav":
		return True
	else:
		return False

def special(rolled, maximum):
	if rolled == 1 and maximum == 1:
		label.config(foreground = "yellow")
		button.config(text = "Crit de Schrödinger")
	elif rolled == 999999999:
		label.config(foreground = "green")
		button.config(text = "Mestre dos Dados")
	elif rolled == maximum:
		label.config(foreground = "green")
		try:
			sound = list(filter(check_wav, os.listdir("Sons\\Positivo")))
			sound = str(rand.sample(sound, 1))
			sound = sound[2:-2]
			play("Sons\\Positivo\\" + sound)
		except:
			pass
	elif rolled == 1:
		label.config(foreground = "red")
		try:
			sound = list(filter(check_wav, os.listdir("Sons\\Negativo")))
			sound = str(rand.sample(sound, 1))
			sound = sound[2:-2]
			play("Sons\\Negativo\\" + sound)
		except:
			pass
	elif rolled == 6 and rand.randint(1, 10) == 1:
		label.config(text = "Meia")
	elif rolled == 12 and rand.randint(1, 10) == 1:
		label.config(text = "Dúzia")
	elif rolled == 13 and rand.randint(1, 10) == 1:
		button.config(text = "Viniccius")
	elif rolled == 34:
		button.config(text = "Regra")
	elif rolled == 51:
		match rand.randint(1, 2):
			case 1:
				button.config(text = "Cachaça")
			case 2:
				button.config(text = "Area")
	elif rolled == 66 and maximum == 100:
		button.config(text = "DARK DARKER", font = ("Wingdings", 16))
	elif rolled == 69:
		button.config(text = "<3")
	elif rolled == 71:
		button.config(text = "Dona Clotilde")
	elif rolled == 420:
		button.config(text = "Dia da Erva")
	elif rolled == 621:
		button.config(text = "e")
	elif rolled == 666:
		label.config(foreground = "red")
		button.config(text = "Atrás de você")
	elif rolled == 777:
		button.config(text = "Jackpot?")
	elif rolled == 16700:
		button.config(text = "17.700?")
	elif rolled == 17700:
		button.config(text = "16.700!")

def roll_dice():
	
	try:
		maximum = int(entry.get())
		if maximum <= 999999999:
			rolled = rand.randint(1, maximum)
			i = 0
			label.config(font = ("Arial", 16), foreground = "black")
			button.config(text = "Rodar", font = ("Arial", 16))
			button["state"] = "disabled"
			play("Sons\\Drum_roll")
			while i < 100:
				i += 1
				rolled = rand.randint(1, maximum)
				label.config(text = rolled)
				if i == 100:
					label.config(font = ("Arial", 30))
					button["state"] = "active"
					if extra.get() == 1:
						special(rolled, maximum)
				root.update()
				time.sleep(0.01)
		else:
			messagebox.showerror(title = "Erro", message = "Insira um valor menor!\nMáximo de 9 caracteres")
	except ValueError:
		messagebox.showerror(title = "Erro", message = "Insira um valor legível!\nMaior que 0, sem letras ou símbolos.")

root = tk.Tk()
root.title("RoDados")
root.geometry("200x200")
try:
	root.iconbitmap("RoDados.ico")
except:
	pass
root.resizable(False, False)

label = tk.Label(root, text = "Rode um dado!", font = ("Arial", 16))
label.pack(pady = 20)

button = tk.Button(root, text = "Rodar", font = ("Arial", 16), command = roll_dice)
button.pack(pady = 10, side = tk.BOTTOM)

entry = tk.Entry(root)
entry.pack(pady = 2, side = tk.BOTTOM, anchor = tk.CENTER)

extra = tk.IntVar()
checkbox = tk.Checkbutton(root, text = "Memes", variable = extra)
checkbox.place(x = 70, y = 90)

root.mainloop()
