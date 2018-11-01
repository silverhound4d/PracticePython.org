
original_list = [1,2,3,4,5,6,7,8,9,10]

def create_new_list(x):
	"""Creates a new list - takes the first and last item from the original list"""
	# Takes a list of numbers as an argument.
	new_list = []
	new_list.append(x[0])
	new_list.append(x[-1])
	print(new_list)

# create_new_list(original_list)


# SAMPLE SOLUTION

a = [1,2,3,4,5,6,7,8,9,10]

def list_ends(any_list):
	new_list = [any_list[0], any_list[len(any_list)-1]]
	# Easier? 
	# new_list = [any_list[0],any_list[-1]]
	print (new_list)

list_ends(a)