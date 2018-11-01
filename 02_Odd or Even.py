# Version 1 - basic excercise

def odd_or_even():
	"""Determines, whether the input is an odd or even number"""
	while True:
		num = input("Please enter a number: ")

		if num.isnumeric():
			num = int(num)
			if num % 2 == 0:
				print("This is an even number.")
				break
			else:
				print("This is an odd number.")
				break

		else:
			print("Ehm, can you please enter a number?")
			continue

odd_or_even()

# Version 2 - Extra assignment

def odd_or_even2():
	"""Determines, whether the input is an odd or even number & another string when divisible by 4"""
	while True:
		num = input("Please enter a number: ")

		if num.isnumeric():
			num = int(num)
			if num % 4 == 0:
				print("AHA! This number is even and divisible by 4.")
				break
			elif num % 2 == 0:
				print("This is an even number.")
				break
			else:
				print("This is an odd number.")
				break

		else:
			print("Ehm, can you please enter a number?")
			continue

odd_or_even2()

# Version 3 

def nothing_left_division():
	"""Asks for 2 number inputs and divides them. Depending on a remainder, different messages are printed out"""
	while True:
		try:
			num = int(input("Enter first number: "))
			break
		except ValueError:
			print("Not a valid number")
			continue 
	while True:
		try:
			check = int(input("Enter second number: "))
			if check > num:
				print("The second number must be equal or lower than the first one")
				continue
			break
		except ValueError:
			print("Not a valid number")
			continue
	result = (num % check) 

	if result == 0:
		print("Oh, nice one! The numbers divide evenly!")
	else:
		print("Eh, the numbers do not divide evenly! For the numbers to divide evenly, deduct " + str(result) + " from the first number.")
	

nothing_left_division()
