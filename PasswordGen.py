# Password Generator Project

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# Asking for the amount of letter, symbols and numbers that the user wants in their password.
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Order not randomised:
password = ""
for _ in range(0, nr_letters): password += random.choice(letters)
for _ in range(0, nr_numbers): password += random.choice(numbers)
for _ in range(0, nr_symbols): password += random.choice(symbols)
print(f"{nr_letters} letter, {nr_numbers} number, {nr_symbols} symbol: {password}")

# Order of characters randomised:
char_list = list(password)
random.shuffle(char_list)
password = "".join(char_list)
print(f"{nr_letters} letter, {nr_numbers} number, {nr_symbols} symbol: {password}")