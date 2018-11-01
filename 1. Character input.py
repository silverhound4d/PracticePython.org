# Version 1

def remains_till_100():
	"""Function prints how many years left for the person to turn 100"""
	name = input("Please enter your name: ")

	while True:
		try:
			age = int(input("Please enter your age: "))
		except ValueError:
			print("Please enter valid number")
			continue
		else:
			year = str(100 - age)
			print ("Huh, so your name is " + name + " and you will be 100 years old in "+ year +" years.")
			break

remains_till_100()

# Version 2 - using import datetime

import datetime
now = datetime.datetime.now()
def year_when_100():
	"""Function prints in what year we'll turn 100"""
	name = input("Please enter your name: ")

	while True:
		try:
			age = int(input("Please enter your age: "))
		except ValueError:
			print("Please enter valid number")
			continue
		else:
			year = str(now.year - age + 100) 
			print ("Huh, so your name is " + name + " and you will turn 100 in the year "+ year +".")
			break

year_when_100()

# Version 3 - using if/elif

import datetime
now = datetime.datetime.now()

def year_when_100_ver2():
	"""Function prints in what year we'll turn 100 - using if/elif statements"""
	
	name = input("Please enter your name: ")

	while True:
		age = (input("Please enter your age: "))

		if age.isnumeric():
			age = int(age)
			year = str(now.year - age + 100) 
			print (f"Huh, so your name is {name} and you will turn 100 in the year {year}.")
			break
		elif not age.isnumeric():
			print("Please enter valid number")
			continue

year_when_100_ver2()

"""Other conditions might be needed: proper name being entered, people already older(age > 100), floats"""
"""Alternatively, have predefined options - choose from a lis of numbers of 1 - 30"""