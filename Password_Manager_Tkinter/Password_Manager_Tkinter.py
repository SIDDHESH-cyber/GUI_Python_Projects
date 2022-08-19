import random
import os
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password ? :"))
nr_numbers = int(input(f"How many numbers would you like ? :"))
nr_symbols = int(input(f"How many symbols would you like ? :"))

password_list = []

for x in range(0, nr_letters):
    password_list.append(random.choice(letters))# ?____________You Can Use Append
for i in range(0, nr_numbers):
    password_list += random.choice(numbers)# ?____________You Can Use Contectation Of Str
for j in range(0, nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""

for x in password_list:
    password += x

os.system('cls')

print("Wait For A While Generating Strongest Password.")
time.sleep(2)
print("Password Created Sussefully.")
time.sleep(2)

os.system('cls')

print(f"\n\nYour Super Strong Password Is Here________ : {password}\n\n")
