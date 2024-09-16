import os
import time

def remove_replace():
	remove = input("Remove ")
	replace = input("and replace with ")
	
	files = os.listdir("Input")
	files.sort()
	for file in files:
		if os.path.exists("Input\\" + file):
			name = os.path.splitext(file)[0]
			extension = os.path.splitext(file)[1]
			name = name.replace(remove, replace)
			while name and name[0] == " ":
				name = name[1:]
			while name and name[len(name) - 1] == " ":
				name = name[:-1]
			name = name + extension
			try:
				os.renames("Input\\" + file, "Input\\" + name)
				if not file == name:
					print(file + " Success")
				else:
					print(file + " Didn't Change")
			except:
				print(file + " Failed")

def rename_files():
	rename = input("Rename to ")
	
	files = os.listdir("Input")
	files.sort()
	number = 1
	for file in files:
		if os.path.exists("Input\\" + file):
			extension = os.path.splitext(file)[1]
			new_name = rename + str(number) + extension
			try:
				os.renames("Input\\" + file, "Input\\" + new_name)
				if not file == new_name:
					print(file + " Success")
				else:
					print(file + " Didn't Change")
				number += 1
			except:
				print(file + " Failed")

if not os.path.exists("Input"):
		os.makedirs("Input")
choice = 0
try:
	choice = int(input("Functions:\nReplace = 1  Rename = 2\n\nInstructions:\nPut the files that you want to rename in the folder 'Input'.\nIf the folder didn't exist, it has been created.\nAll files will remain in that folder until you remove them.\n\nTips:\nTo loop the code, input 0 after the first number. Example: 10, 20.\nTo remove, simply don't input anything on 'and replace with '.\nTo rename all files to just the respective number, simply don't input anything on 'Rename to'.\nMost characters will be applied, even spaces.\nSpaces on both ends will be automatically removed. Example: Save .png will become Save.png\n\n"))
except:
	pass

if choice == 1 or choice == 10:
	if choice == 10:
		print("This code will loop indefinitely.\n")
		while 0 == 0:
			remove_replace()
			print("Done\n")
	else:
		remove_replace()
	print("Done")
elif choice == 2 or choice == 20:
	if choice == 20:
		print("This code will loop indefinitely.\n")
		while 0 == 0:
			rename_files()
			print("Done\n")
	else:
		rename_files()
	print("Done")
else:
	print("Invalid option input\n")
time.sleep(2)