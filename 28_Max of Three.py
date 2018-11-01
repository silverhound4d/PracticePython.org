
var1 = float(input("Please enter first number: "))
var2 = float(input("Please enter second number: "))
var3 = float(input("Please enter third number: "))

def max_of_three(x,y,z):
	"""Finds the maximum value from 3 inputs, without using max()"""
	if x > y and x > z:
		print (x)
		return x
	elif y > z and y > z:
		print (y)
		return y
	else:
		print(z)
		return y

max_of_three(var1,var2,var3)

#Hahahahhahaa
