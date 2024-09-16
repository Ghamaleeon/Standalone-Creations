while equation := input('<- '):
	for char in equation:
		if not char in '1234567890+-*/%&|~^<>=!(). ': equation = equation.replace(char, ' ')
	try: print('-> ' + str(eval(equation)))
	except: print('~> Syntax Error')