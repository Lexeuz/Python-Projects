import os
import art


def clean_console():
    os.system("cls")

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def decision(n1, n2, op):

    if op == "+": return addition(n1, n2)
    elif op == "-": return subtraction(n1, n2)
    elif op == "*": return multiplication(n1, n2)
    elif op == "/": return division(n1, n2)

print(art.logo)

on = True
while on:
    n1 = int(input("What's the first number?: "))
    op = input("+\n-\n*\n/\nPick an operation: ")
    n2 = int(input("What's the next number?: "))
    
    result = 0
    result = decision(n1, n2, op)
    
    if (input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")) == "y":
        continue_calc = True
        while continue_calc:
            n1 = result
            op = input("+\n-\n*\n/\nPick an operation: ")
            n2 = int(input("What's the next number?: "))
            result = decision(n1, n2, op)
            if (input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")) == "y":
                pass
            else:
                clean_console()
                continue_calc = False
                print(art.logo)



