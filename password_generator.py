import random
letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
print("welcome to password generator!!!")
nr_letters=int(input("enter number of letters in your password: "))
nr_numbers=int(input("enter number of numbers in your password: "))
nr_symbols=int(input("enter number of symbols in your password: "))

password_list=[]

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password=""
for char in password_list:
    password+=char

print(f"Your password is:{password}")
