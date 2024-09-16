
with open('npcnames-female.txt') as infile, open('npcnames-female2.txt', 'w') as outfile:
	for line in infile:
		for char in line:
			if char in '1234567890+-*/%&|~^<>=!(). ': line = line.replace(char, '')
		outfile.write(line)
