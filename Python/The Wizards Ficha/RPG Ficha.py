from tkinter import *
from PIL import ImageTk, Image

def intl(id): return int(stat_label[id].cget("text"))
def inte(id): return int(stat_entry[id].get())
def setl(id,value): stat_label[id].config(text=str(value))
def addl(id,value): setl(id,intl(id)+value)
def getexp():
	if not exp.get()=="" and exp.get().isdigit(): return int(exp.get())
	else: return 0
def create_image(id,xpos,ypos):
	image=Label(window,image=stat_png[id])
	image.place(x=xpos,y=ypos)
def create_label(xpos,ypos,ltext=""):
	if ltext=="": label=Label(window,font="arial 16",width=4,text="0")
	else: label=Label(window,font="arial 16",text=ltext)
	label.place(x=xpos,y=ypos)
	if ltext=="": stat_label.append(label)
def create_entry(xpos,ypos,size=3,textvar=None):
	if textvar==None: entry=Entry(window,font="arial 11",width=str(size),validate="focusout",validatecommand=update_labels)
	else: entry=Entry(window,font="arial 11",width=str(size),validate="focusout",validatecommand=update_labels,textvariable=textvar)
	entry.place(x=xpos,y=ypos)
	if textvar==None: stat_entry.append(entry)
def create_menubutton(xpos,ypos,startstring,vari,options):
	menubutton=Menubutton(window,text=startstring)
	menu=Menu(menubutton,tearoff=False)
	for each in options: menu.add_radiobutton(label=each,value=each,variable=vari)
	menubutton["menu"]=menu
	menubutton.place(x=xpos,y=ypos)
	menus.append(menubutton)
def update_labels(*args):
	level = 0
	for each in [9,10,100,200,400,600,1000,3200,3800,4500,5700,6800,7900,9000,9600,10000,10800,12000,12900,14500]:
		if getexp()>=each: level=level+1
	levellabel.config(text="Nível: "+str(level))
	
	for each in range(9):
		check=str(stat_entry[each].get())
		if check[:1]=="-" or check[:1]=="+": check=check[1:]
		if check.isdigit():
			if each<=1: setl(each,inte(each)*2)
			elif each<=5: setl(each,inte(each)//5)
			else: setl(each,inte(each))
		else: setl(each,0)
	if not selected_race.get()=="": menus[0].config(text=selected_race.get())
	if not selected_element.get()=="": menus[1].config(text=selected_element.get())
	if not selected_advantage.get()=="": menus[2].config(text=selected_advantage.get())
	if not selected_disadvantage.get()=="": menus[3].config(text=selected_disadvantage.get())
	match selected_element.get():
		case "Fogo":
			if level>=1: addl(pdh,2)
			if level>=4: addl(pdh,2)
			if level>=6: addl(vida,5)
			if level>=8: addl(pdh,1)
			if level>=12: addl(pdh,2)
			if level>=14: pass # +1 ação extra
			if level>=18: addl(pdh,2)
			if level>=20: addl(vida,10)
		case "Água":
			if level>=1: addl(mana,5)
			if level>=4: addl(pdh,2)
			if level>=5: addl(mana,5)
			if level>=8: addl(intel,1)
			if level>=10: addl(mana,5)
			if level>=13: addl(pdh,2)
			if level>=15: addl(vida,5)
			if level>=18: addl(pdh,2)
			if level>=20: addl(mana,5)
		case "Terra":
			if level>=1: addl(mana,5)
			if level>=2: addl(vida,5)
			if level>=4: addl(forca,1)
			if level>=6: addl(resis,2)
			if level>=8: addl(vida,5)
			if level>=10: addl(resis,2)
			if level>=12: addl(forca,1)
			if level>=14: addl(vida,5)
			if level>=16: addl(resis,2)
			if level>=18: addl(forca,1)
			if level>=20: addl(resis,2)
		case "Ar":
			if level>=1: addl(habil,1)
			if level>=4: addl(pdh,2)
			if level>=6: pass # -1 tempo de carga
			if level>=8: addl(mana,5)
			if level>=10: addl(habil,2)
			if level>=12: pass # -1 tempo de carga
			if level>=14: addl(habil,2)
			if level>=16: addl(pdh,2)
			if level>=18: addl(mana,5)
			if level>=20: pass # -4 tempo de carga
		case "Luz":
			if level>=1: addl(intel,1)
			if level>=4: addl(mana,5)
			if level>=6: addl(habil,1)
			if level>=8: addl(intel,1)
			if level>=10: addl(mana,5)
			if level>=12: addl(intel,2)
			if level>=14: addl(resis,1)
			if level>=16: addl(intel,2)
			if level>=18: addl(mana,5)
			if level>=20: addl(intel,2)
		case "Sombra":
			if level>=1: addl(intel,1)
			if level>=2: addl(habil,1)
			if level>=4: addl(vida,5)
			if level>=6: addl(intel,1)
			if level>=8: addl(habil,1)
			if level>=10: addl(intel,2)
			if level>=12: addl(mana,5)
			if level>=14: addl(habil,2)
			if level>=16: addl(forca,1)
			if level>=18: addl(intel,2)
			if level>=20: addl(habil,2)
		case "Relâmpago":
			if level>=1: addl(habil,2)
			if level>=2: addl(pdh,2)
			if level>=4: addl(vida,5)
			if level>=6: addl(intel,1)
			if level>=8: addl(pdh,2)
			if level>=10: addl(mana,5)
			if level>=12: addl(pdh,2)
			if level>=14: addl(habil,2)
			if level>=16: pass # -2 tempo de carga
			if level>=18: addl(pdh,2)
			if level>=20: pass # +1 ação extra
		case "Combustão":
			if level>=1: addl(pdh,4)
			if level>=2: addl(vida,5)
			if level>=4: addl(forca,1)
			if level>=6: addl(pdh,2)
			if level>=8: addl(vida,5)
			if level>=10: addl(pdh,2)
			if level>=12: addl(vida,5)
			if level>=14: addl(mana,5)
			if level>=16: addl(pdh,1)
			if level>=18: addl(resis,2)
			if level>=20: addl(pdh,1)
		case "Gelo":
			if level>=1: addl(pdh,2)
			if level>=2: addl(intel,2)
			if level>=4: addl(resis,2)
			if level>=6: addl(pdh,2)
			if level>=8: addl(mana,5)
			if level>=10: addl(intel,1)
			if level>=12: addl(pdh,2)
			if level>=14: addl(mana,5)
			if level>=16: addl(resis,2)
			if level>=18: addl(pdh,2)
			if level>=20: addl(intel,2)
		case "Sangue":
			if level>=1: addl(vida,10)
			if level>=2: addl(pdh,4)
			if level>=4: addl(intel,2)
			if level>=6: addl(pdh,2)
			if level>=8: addl(resis,2)
			if level>=10: addl(vida,5)
			if level>=12: addl(pdh,2)
			if level>=14: addl(vida,10)
			if level>=16: addl(intel,2)
			if level>=18: addl(habil,2)
			if level>=20: addl(pdh,2)
		case "Ferro":
			if level>=1: addl(resis,4)
			if level>=2: addl(forca,4)
			if level>=4: addl(vida,5)
			if level>=6: addl(pdh,2)
			if level>=8: addl(mana,5)
			if level>=10: addl(resis,2)
			if level>=12: addl(pdh,2)
			if level>=14: addl(vida,5)
			if level>=16: addl(forca,2)
			if level>=18: addl(pdh,2)
			if level>=20: addl(resis,2)
		case "Areia":
			if level>=1: addl(pdh,4)
			if level>=2: addl(intel,2)
			if level>=3: addl(mana,5)
			if level>=4: addl(vida,5)
			if level>=6: addl(pdh,2)
			if level>=8: addl(habil,2)
			if level>=10: addl(pdh,2)
			if level>=12: addl(pdh,2)
			if level>=13: addl(mana,5)
			if level>=16: addl(pdh,2)
			if level>=18: addl(vida,5)
			if level>=20: addl(habil,4)
		case "Veneno":
			if level>=1: addl(pdh,2)
			if level>=2: addl(vida,5)
			if level>=4: addl(mana,5)
			if level>=6: addl(habil,4)
			if level>=8: addl(pdh,2)
			if level>=10: addl(intel,1)
			if level>=12: addl(vida,5)
			if level>=13: addl(mana,5)
			if level>=16: addl(pdh,2)
			if level>=18: addl(intel,2)
			if level>=20: addl(pdh,4)
	match selected_race.get():
		case "Humano":
			addl(vida,5+(level*3))
			addl(mana,5+(level*3))
		case "Demônio":
			addl(vida,5+(level*4))
			addl(mana,4)
			addl(fisic,1+(level//2))
		case "Vampiro":
			addl(vida,5+(level//2))
			addl(mana,10+(level*4))
			addl(fisic,-3)
		case "Asimar":
			addl(vida,(level//2)*3)
			addl(mana,5+(level*2))
			addl(habil,2)
			addl(fisic,-2)
		case "Renascido":
			addl(vida,10+(level*5))
			addl(vida,intl(mana))
			setl(mana,"?")
			addl(magic,2+(level//2))
	if selected_element.get()=="Ferro": addl(pdh,intl(resis)//5)
	addl(fisic,intl(resis)//5)
	for each in range(9):
		if not stat_label[each].cget("text")=="?": setl(each,min(intl(each),9999))
	return True

window=Tk()
window.title("The Wizards")
window.geometry("550x650")
window.resizable(False,False)
#window.config(bg="black")

stat_png,stat_label,stat_entry,menus=[],[],[],[]

for each in [
"hp.png",
"mp.png",
"for.png",
"int.png",
"hab.png",
"res.png",
"pdh.png",
"armf.png",
"armm.png"
]: stat_png.append(ImageTk.PhotoImage(Image.open(each)))

vida=0
mana=1
forca=2
intel=3
habil=4
resis=5
pdh=6
fisic=7
magic=8

selected_race,selected_element,selected_advantage,selected_disadvantage,name,exp=StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
selected_race.trace("w",update_labels)
selected_element.trace("w",update_labels)
selected_advantage.trace("w",update_labels)
selected_disadvantage.trace("w",update_labels)

for each in range(7):
	create_image(each,16,36*each+48)
	create_label(52,36*each+51)
	create_entry(106,36*each+55)
for each in range(2):
	create_image(each+7,75*each+190,48)
	create_label(75*each+181,36+51)
	create_entry(75*each+194,72+55)
create_label(16,12,"Nome:")
create_entry(82,16,20,name)
create_label(246,12,"XP:")
create_entry(286,16,5,exp)
levellabel=Label(window,font="arial 16",text="Nível: 0")
levellabel.place(x=330,y=12)

create_menubutton(190,144+17,"Raça",selected_race,["Humano","Demônio","Vampiro","Asimar","Renascido"])
create_menubutton(190,180+17,"Elemento",selected_element,["Fogo","Água","Terra","Ar","Luz","Sombra","Relâmpago","Combustão","Gelo","Sangue","Ferro","Areia","Veneno",])
create_menubutton(190,216+17,"Vantagem",selected_advantage,["Encantador","Historiador","Artífice","Químico","Poliglota","Bardista","Ligação Animal","Contrabandista","Mestre em Fechaduras","Torcida","Visão Noturna","Audição Aguçada","Olfato Aguçado","Montaria","Mochileiro","Clericato","Inventor","Famoso","Larápio","Coletor"])
create_menubutton(190,252+17,"Desvantagem",selected_disadvantage,["Cultista Insano","Doença Mágica","Desvantagista","Só usa Armas Vivas","Azarado","Exibido","Confusão","Alcoólatra","Código de Honra","Esquecido","Brigão","Procurado","Desordenado","Dependente Químico","Psicopata","Esquizofrênico"])

window.mainloop()