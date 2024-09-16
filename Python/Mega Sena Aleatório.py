import random as rand
import tkinter as tk

def generate_game():
	rolled = rand.sample(range(1, 60), 6)
	rolled.sort()
	label.config(text = rolled)

root = tk.Tk()
root.title("Mega")
root.geometry("200x125")
root.resizable(False, False)

label = tk.Label(root, text = "Gere um jogo!", font = ("Arial", 16))
label.pack(pady = 20)

button = tk.Button(root, text = "Gerar", font = ("Arial", 16), command = generate_game)
button.pack(pady = 10, side = tk.BOTTOM)

root.mainloop()