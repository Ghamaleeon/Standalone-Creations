def one(array: arr) -> bool: return array.count(19) == 2 and array.count(5) > 2

def two(array: arr) -> bool: return len(array) == 8 and array.count(array[5]) == 3

def three(number: int) -> bool: return number > 4**4 and number % 34 == 4

def four(number: int) -> array:
	array = []
	for each in range(number): array.append(number+(each*2))
	return array

def five(array: arr) -> bool: array[len(array)-2] in array[len(array)-1]

def six(array: arr) -> bool:
	for each in array:
		if not array.index(each) == len(array)-1:
			if each - array[array.index(each)] != -10: return False
	return True

def seven(array: arr, number: int) -> bool: return sum(array[:number]) == number