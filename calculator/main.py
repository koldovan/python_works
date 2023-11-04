from art import *

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

print(logo)
def calculator():
    check = True
    num1 = float(input("What's the first number? "))
    while check:
        for key in operations:
            print(key)
        operation_type = input("Choose the operation: ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations[operation_type]
        answer = calculation_function(num1, num2)
        proceed = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation or anything else to exit.")
        if proceed == "y":
            num1 = answer
        elif proceed == 'n':
            check = False
            calculator()
        else:
            check = False
            print(f"There is no {proceed} option.")
calculator()
