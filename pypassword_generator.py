#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_list = []
password = ''

# populate pass_list with random letters
for n in range(1, nr_letters+1):
	rand_l = random.randint(0, len(letters)-1)
	pass_list.append(letters[rand_l])

# populate pass_list with random numbers
for n in range(1, nr_numbers+1):
	rand_n = random.randint(0, len(numbers)-1)
	pass_list.append(numbers[rand_n])

# populate pass_list with random symbols
for n in range(1, nr_symbols+1):
	rand_s = random.randint(0, len(symbols)-1)
	pass_list.append(symbols[rand_s])

# shuffle the pass_list
random.shuffle(pass_list)

# generate password as a string
for item in pass_list:
	password += item

print(password)
