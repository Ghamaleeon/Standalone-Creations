file = open("Text.txt", "+")
read = file.readlines()

for line in read:
	if line[-1] == "\n":
		line[:-1]

