"""
Author usernames: nyagatac
Date: December 3,2021
Assignment/problem number: Programming Examlet 9
Assignment/problem title: Examlet 9
"""
#Part One
def rotateLeft(fruit):
   
	tmp_table = list(fruit)
	fruit.clear()
	for f in tmp_table[::-1]:
		fruit.append(f)

#Part Two

def multiplyGrid(number, grid):
    
	tmp_grid = list(grid)
	grid.clear()

	for lst in tmp_grid:
		for index, item in enumerate(lst):
			lst[index] = item * 5
		grid.append(lst)

#Part Three

def createDictionnary():
	return {
		"pig":"igpay",
		"banana":"ananabay",
		"happy":"appyhay",
		"duck":"uckday",
		"string":"ingstray",
		"floor":"oorflay"
	}

def translate():
	words = createDictionnary()
	while True:
		word = input("What word would you like to translate? ")
		if word == "quit":
			break
		elif word in words.keys():
			print(words[word])
		else:
			print(f"The word {word} is not in the dictionnary.")

#Part Four
class ProduceItem:
	def __init__(self, name, qty, unit, price):
		self.name = name
		self.qty = qty
		self.unit = unit
		self.price = price

	def totalPrice(self):
		return round(self.qty * self.price, 2)

	def __str__(self):
		return f"{self.qty} {self.name}\t\t@ {self.price}/{self.unit}\t\t${self.totalPrice()}"