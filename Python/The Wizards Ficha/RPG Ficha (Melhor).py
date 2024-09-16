from tkinter import *
from PIL import ImageTk, Image

def create_entry(xpos,ypos,size=3,fontstyle="arial 11"):
	entry=Entry(window,font=fontstyle,width=str(size),validate="focusout",validatecommand=update_labels)
	entry.place(x=xpos,y=ypos)
	return entry

def create_image(xpos,ypos,id):
	image=Label(window,image=stat_image[id])
	image.place(x=xpos,y=ypos)
	return image

def create_label(xpos,ypos,ltext="",stat=True):
	if stat: label=Label(window,font="arial 16",text=ltext, width=4)
	else: label=Label(window,font="arial 16",text=ltext)
	label.place(x=xpos,y=ypos)
	return label

def get_entry(id):
	if stat_entry[id].get()!="":
		check=str(stat_entry[id].get())
		if check[:1]=="-" or check[:1]=="+": check=check[1:]
		if check.isdigit(): return int(stat_entry[id].get())
	return 0

def get_bonus(id):
	if stat_bonus[id].get()!="":
		check=str(stat_bonus[id].get())
		if check[:1]=="-" or check[:1]=="+": check=check[1:]
		if check.isdigit(): return int(stat_bonus[id].get())
	return 0

def update_labels(*args):
	stat = {}
	for each in stat_entry:
		stat[each] = 0
		if each in ["hp","mp"]: stat[each] += get_entry(each)*2
		elif each in ["for","int","hab","res"]: stat[each] += get_entry(each)//5
		else: stat[each] += get_entry(each)
		if each in stat_bonus: stat[each] += get_bonus(each)
	stat["armf"] += stat["res"]//5
	for each in stat_label: stat_label[each].config(text=str(min(stat[each], 9999)))
	return True

window=Tk()
window.title("The Wizards")
window.geometry("550x650")
window.resizable(False,False)
#window.config(bg="black")

stat_entry,stat_bonus,stat_label,stat_image={},{},{},{}

name = ["hp","mp","for","int","hab","res","pdh"]
for each in range(len(name)):
	stat_label[name[each]] = create_label(52,36*each+51,"0")
	if name[each] != "pdh":
		stat_entry[name[each]] = create_entry(106,36*each+55)
		stat_bonus[name[each]] = create_entry(134,36*each+57,3,"arial 7")
	else: stat_entry[name[each]] = create_entry(106,36*each+57,3,"arial 7")
	stat_image[name[each]] = ImageTk.PhotoImage(Image.open(name[each]+".png"))
	create_image(16,36*each+48,name[each])
name = ["armf","armm"]
for each in range(len(name)):
	stat_label[name[each]] = create_label(75*each+181,36+51,"0")
	stat_entry[name[each]] = create_entry(75*each+199,72+55,3,"arial 7")
	stat_image[name[each]] = ImageTk.PhotoImage(Image.open(name[each]+".png"))
	create_image(75*each+190,48,name[each])
del name

stat_label["terr"] = create_label(52 + 50, 36 + 55)

window.mainloop()