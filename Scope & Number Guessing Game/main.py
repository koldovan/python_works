from art import *
import random


def game():
    game_over = False
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print(f"There is no such option.")
        exit()

    while game_over is not True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            game_over = True
        elif attempts == 1:
            game_over = True
            print("You've run out of guesses, you lose.")
            exit()
        elif guess > number and attempts != 0:
            print("Too high.\nGuess again.")
            attempts -= 1
        elif guess < number and attempts != 0:
            print("Too low.\nGuess again.")
            attempts -= 1




print(logo, logo2)
number = random.randint(1, 100)
game()