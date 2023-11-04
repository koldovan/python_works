import random
from hangman_art import *
from hangman_words import *
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
position = 0
lives = 6
end_of_game = False


for letter in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
         print(f"You have already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            

    print(f"{' '.join(display)}")
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if lives == 0:
            end_of_game = True
            print("You lose.")
    

