from art import *

print(logo)
first_number = float(input("What's the first number? "))
check = True

def calculate(first_number, next_number):
    if operation == "+":
        return first_number + next_number
    elif operation == "-":
        return first_number - next_number
    elif operation == "*":
        return first_number * next_number
    elif operation == "/":
        return first_number / next_number
    else:
        return f"There is no {operation} operation."

while check:
    operation = input('+\n-\n*\n/\nPick an operation: ')
    next_number = float(input("What's the next number? "))
    result = calculate(first_number, next_number)
    proceed = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if proceed == 'y':
        first_number = result
    elif proceed == 'n':
        check = False
        