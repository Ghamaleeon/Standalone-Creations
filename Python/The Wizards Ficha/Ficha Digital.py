from tkinter import *
from PIL import ImageTk, Image

def make(element_name,x,y,**kwargs):
	match element_name:
		case 'Menubutton':
			element=Menubutton(window,text=kwargs.get('text'))
			menu=Menu(element,tearoff=False)
			for each in kwargs.get('options', ''):menu.add_radiobutton(label=each,value=each,variable=kwargs.get('variable'))
			element["menu"]=menu
		case _:
			element=eval(element_name+'('+'window,kwargs'+')')
	element.place(x=x,y=y)
	return element

def eget(element):
	new=''.join([each for each in element.get() if each.isdigit()])
	if not element.get()=='':
		sign=element.get()[0]
		if not sign=='-': sign=''
		return int(sign+new)
	return 0
# e.delete(0,END)
# e.insert(0,text)

def update_labels(*args):
	stat = {}
	level = 0
	
	for each in [9,10,100,200,400,600,1000,3200,3800,4500,5700,6800,7900,9000,9600,10000,10800,12000,12900,14500]:
		if eget(exp)>=each: level += 1
	level_label.config(text="Nível: "+str(level))
	
	for each in stat_points:
		if not each in stat: stat[each] = 0
		
		if each in ['hp','mp']: stat[each] += eget(stat_points[each])*2
		else: stat[each] += eget(stat_points[each])//5
	
	for each in stat_bonus:
		if not each in stat: stat[each] = 0
		
		stat[each] += eget(stat_bonus[each])
	
	for each in menus:
		if not selected[each].get()=='':
			menus[each].config(text=selected[each].get())

	match selected['Elemento'].get():
		case "Fogo":
			if level>=1: stat['pdh']+=2
			if level>=4: stat['pdh']+=2
			if level>=6: stat['hp']+=5
			if level>=8: stat['pdh']+=1
			if level>=12: stat['pdh']+=2
			if level>=14: stat['tur']+=1
			if level>=18: stat['pdh']+=2
			if level>=20: stat['hp']+=10
		case "Água":
			if level>=1: stat['mp']+=5
			if level>=4: stat['pdh']+=2
			if level>=5: stat['mp']+=5
			if level>=8: stat['int']+=1
			if level>=10: stat['mp']+=5
			if level>=13: stat['pdh']+=2
			if level>=15: stat['hp']+=5
			if level>=18: stat['pdh']+=2
			if level>=20: stat['mp']+=5
		case "Terra":
			if level>=1: stat['mp']+=5
			if level>=2: stat['hp']+=5
			if level>=4: stat['for']+=1
			if level>=6: stat['res']+=2
			if level>=8: stat['hp']+=5
			if level>=10: stat['res']+=2
			if level>=12: stat['for']+=1
			if level>=14: stat['hp']+=5
			if level>=16: stat['res']+=2
			if level>=18: stat['for']+=1
			if level>=20: stat['res']+=2
			stat['car']+=2
			stat["armf"]+=stat["res"]//5
		case "Ar":
			if level>=1: stat['hab']+=1
			if level>=4: stat['pdh']+=2
			if level>=6: stat['car']-=1
			if level>=8: stat['mp']+=5
			if level>=10: stat['hab']+=2
			if level>=12: stat['car']-=1
			if level>=14: stat['hab']+=2
			if level>=16: stat['pdh']+=2
			if level>=18: stat['mp']+=5
			if level>=20: stat['car']-=4
			stat['tur']+=(level//4)
		case "Luz":
			if level>=1: stat['int']+=1
			if level>=4: stat['mp']+=5
			if level>=6: stat['hab']+=1
			if level>=8: stat['int']+=1
			if level>=10: stat['mp']+=5
			if level>=12: stat['int']+=2
			if level>=14: stat['res']+=1
			if level>=16: stat['int']+=2
			if level>=18: stat['mp']+=5
			if level>=20: stat['int']+=2
		case "Sombra":
			if level>=1: stat['int']+=1
			if level>=2: stat['hab']+=1
			if level>=4: stat['hp']+=5
			if level>=6: stat['int']+=1
			if level>=8: stat['hab']+=1
			if level>=10: stat['int']+=2
			if level>=12: stat['mp']+=5
			if level>=14: stat['hab']+=2
			if level>=16: stat['for']+=1
			if level>=18: stat['int']+=2
			if level>=20: stat['hab']+=2
		case "Relâmpago":
			if level>=1: stat['hab']+=2
			if level>=2: stat['pdh']+=2
			if level>=4: stat['hp']+=5
			if level>=6: stat['int']+=1
			if level>=8: stat['pdh']+=2
			if level>=10: stat['mp']+=5
			if level>=12: stat['pdh']+=2
			if level>=14: stat['hab']+=2
			if level>=16: stat['car']-=2
			if level>=18: stat['pdh']+=2
			if level>=20: stat['tur']+=1
		case "Combustão":
			if level>=1: stat['pdh']+=4
			if level>=2: stat['hp']+=5
			if level>=4: stat['for']+=1
			if level>=6: stat['pdh']+=2
			if level>=8: stat['hp']+=5
			if level>=10: stat['pdh']+=2
			if level>=12: stat['hp']+=5
			if level>=14: stat['mp']+=5
			if level>=16: stat['pdh']+=1
			if level>=18: stat['res']+=2
			if level>=20: stat['pdh']+=1
		case "Gelo":
			if level>=1: stat['pdh']+=2
			if level>=2: stat['int']+=2
			if level>=4: stat['res']+=2
			if level>=6: stat['pdh']+=2
			if level>=8: stat['mp']+=5
			if level>=10: stat['int']+=1
			if level>=12: stat['pdh']+=2
			if level>=14: stat['mp']+=5
			if level>=16: stat['res']+=2
			if level>=18: stat['pdh']+=2
			if level>=20: stat['int']+=2
			stat['car']+=1
		case "Sangue":
			if level>=1: stat['hp']+=10
			if level>=2: stat['pdh']+=4
			if level>=4: stat['int']+=2
			if level>=6: stat['pdh']+=2
			if level>=8: stat['res']+=2
			if level>=10: stat['hp']+=5
			if level>=12: stat['pdh']+=2
			if level>=14: stat['hp']+=10
			if level>=16: stat['int']+=2
			if level>=18: stat['hab']+=2
			if level>=20: stat['pdh']+=2
		case "Ferro":
			if level>=1: stat['res']+=4
			if level>=2: stat['for']+=4
			if level>=4: stat['hp']+=5
			if level>=6: stat['pdh']+=2
			if level>=8: stat['mp']+=5
			if level>=10: stat['res']+=2
			if level>=12: stat['pdh']+=2
			if level>=14: stat['hp']+=5
			if level>=16: stat['for']+=2
			if level>=18: stat['pdh']+=2
			if level>=20: stat['res']+=2
			stat['car']+=3
			stat['pdh']+=(stat['res']//5)
		case "Areia":
			if level>=1: stat['pdh']+=4
			if level>=2: stat['int']+=2
			if level>=3: stat['mp']+=5
			if level>=4: stat['hp']+=5
			if level>=6: stat['pdh']+=2
			if level>=8: stat['hab']+=2
			if level>=10: stat['pdh']+=2
			if level>=12: stat['pdh']+=2
			if level>=13: stat['mp']+=5
			if level>=16: stat['pdh']+=2
			if level>=18: stat['hp']+=5
			if level>=20: stat['hab']+=4
		case "Veneno":
			if level>=1: stat['pdh']+=2
			if level>=2: stat['hp']+=5
			if level>=4: stat['mp']+=5
			if level>=6: stat['hab']+=4
			if level>=8: stat['pdh']+=2
			if level>=10: stat['int']+=1
			if level>=12: stat['hp']+=5
			if level>=13: stat['mp']+=5
			if level>=16: stat['pdh']+=2
			if level>=18: stat['int']+=2
			if level>=20: stat['pdh']+=4
	
	match selected['Raça'].get():
		case "Humano":
			stat['hp']+=5+(level*3)
			stat['mp']+=5+(level*3)
		case "Demônio":
			stat['hp']+=5+(level*4)
			stat['mp']+=4
			stat['armm']+=1+(level//2)
		case "Vampiro":
			stat['hp']+=5+(level//2)
			stat['mp']+=10+(level*4)
			stat['armm']-=3
		case "Asimar":
			stat['hp']+=(level//2)*3
			stat['mp']+=5+(level*2)
			stat['hab']+=2
			stat['armm']-=2
			stat['tur']+=(level//2)
			stat['armf']/=2
		case "Renascido":
			stat['hp']+=10+(level*5)
			stat['hp']+=stat['mp']
			stat['mp']=0
			stat['armm']+=2+(level//2)
	
	stat['armf']-=1
	stat["mob"]+=stat["hab"]//2 + 1
	
	for each in stat_label: stat_label[each].config(text=str(min(stat[each], 9999)))
	print(stat)
	
	return True

window=Tk()
window.title('The Wizards')
window.geometry('550x650')
window.resizable(False,False)
# window.config(bg='black')

stat_points,stat_bonus,stat_label,menus,selected = {},{},{},{},{}

name = ["hp","mp","for","res","int","hab"]
for each in name:
	stat_label[each] = make('Label',52,32*name.index(each)+51,font='arial 16',width=4,text='0')
	if name.index(each) < 6: stat_points[each] = make('Entry',106,32*name.index(each)+55,font='arial 11',width='5',validate='focusout',validatecommand=update_labels)
	stat_bonus[each] = make('Entry',150,32*name.index(each)+57,font="arial 7",width='5',validate='focusout',validatecommand=update_labels)

name = ["tur","pdh","car","armf","armm","mob"]
for each in name:
	stat_label[each] = make('Label',231,32*name.index(each)+51,font='arial 16',width=4,text='0')
	stat_bonus[each] = make('Entry',285,32*name.index(each)+57,font="arial 7",width='5',validate='focusout',validatecommand=update_labels)

arr = [["Humano","Demônio","Vampiro","Asimar","Renascido"],
["Fogo","Água","Terra","Ar","Luz","Sombra","Relâmpago","Combustão","Gelo","Sangue","Ferro","Areia","Veneno"],
["Melhoria", "Artífice", "Medicina", "Liderança", "Alquimista", "Escudeiro", "Atletismo", "Furtividade", "Interrogar", "Percepção", "Sobrevivência"],
["Encantador","Historiador","Artífice","Químico","Poliglota","Bardista","Ligação Animal","Contrabandista","Mestre em Fechaduras","Torcida","Visão Noturna","Audição Aguçada","Olfato Aguçado","Montaria","Mochileiro","Clericato","Inventor","Famoso","Larápio","Coletor"],
["Cultista Insano","Doença Mágica","Desvantagista","Só usa Armas Vivas","Azarado","Exibido","Confusão","Alcoólatra","Código de Honra","Esquecido","Brigão","Procurado","Desordenado","Dependente Químico","Psicopata","Esquizofrênico"]]

name = ['Raça', 'Elemento', 'Perícia', 'Vantagem', 'Desvantagem']
for each in name:
	selected[each] = StringVar()
	selected[each].trace("w",update_labels)
	menus[each] = make('Menubutton',366,32*name.index(each)+69,text=each,options=arr[name.index(each)],variable=selected[each])
del arr

make('Label',16,12,text="Nome:",font="Arial 16")
name = make('Entry',82,16,font='arial 11',width='20')
make('Label',246,12,text="XP:",font="Arial 16")
exp = make('Entry',286,16,font='arial 11',width='5',validate='focusout',validatecommand=update_labels)
level_label = make('Label',330,12,text="Nível: 0",font="Arial 16")

update_labels()

window.mainloop()