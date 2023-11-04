import os
from art import logo

print(logo,"\nWelcome to the secret auction program.")
proceed = True 
bidders = {}
max_key = ""

def add_bidders():
    bidders[name] = bid

def get_the_winner():
    max_value = max(bidders.values())
    for key, value in bidders.items():
        if value == max_value:
            print(f"The winner is {key} with a bid of ${max_value}")

while proceed == True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    add_bidders()
    if other_bidders == "yes":
        os.system("clear")
    else:
        get_the_winner()
        proceed = False


