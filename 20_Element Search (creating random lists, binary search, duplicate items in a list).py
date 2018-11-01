
# Version 1 - My own solution
import random
my_list = list(range(1,26))
ordered_sample_list = sorted(random.sample(my_list, k=15))
target = 17

def is_in_list(data, item):
	"""Two inputs: list and an item to search for"""
	for i,j in enumerate(data):
		if data[i] == item:
			print(ordered_sample_list)
			print (i,j)
		elif item not in data:
			print("Too bad")
			break

#is_in_list(ordered_sample_list, target)


#Version 1.2 - # Use randint and append to a list instead

import random
random_num_list = []

while len(random_num_list) < 5000:
	random_num = random.randrange(1,10001)
	if random_num in random_num_list:
		continue
	else: 
		random_num_list.append(random_num)

def is_in_list(x, list):
	"""Function decides, whether the integer x is present in the list"""
	if x in list:
		print (True)
		return True

	else:
		print (False)
		return False

#is_in_list(1, random_num_list)

#Version 1.2 Side task - create a function that prints duplicate values in a list

def repeat(x):
	size = len(x)
	repeated_values = []

	for i in range(size):
		k = i + 1
		for j in range (k, size):
			if x[i] == x[j] and x[i] not in repeated_values:
				repeated_values.append(x[i])
	print(sorted(x))
	print(sorted(repeated_values))
	print(len(repeated_values))

#repeat(random_num_list)

#Note to self - thank you google


# Version 2 - use binary search (Works only on a sorted list!!!)


def binary_search(lst, lst_size, z):
	start = 0
	end = lst_size - 1
	print ("This is the end: " + str(end))
	
	while start <= end:
		mid = (start + end) // 2
		print("The mid index was set to: " + str(mid))
		if z == lst[mid]:
			print("Entered number {} is present at positon: {}".format(z, mid))
			return -1 
		elif z < lst[mid]:
			end = mid - 1
			print ("The end index was set to:" + str(end))
		elif z > lst[mid]:
			start = mid + 1
			print ("The start index was set to:" + str(start))
	print ("Element not found!")
	return -1

while True:
	size = int(input("Enter size of list: "))
	if size > 10000:
		print("Please enter a number lower than 10000")
		continue
	elif size < 10000:
		break
		
first_list = list(range(1,10001))
my_list = sorted(random.sample(first_list, k=size))
print(my_list)
number_to_search = int(input("Enter the number to search: "))

binary_search(my_list, size, number_to_search)






