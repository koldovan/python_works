
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, len(images) - 1)
player_index = images[player_choice]
print(f"You chose\n{player_index}.")
computer_index = images[computer_choice]
print(f"Computer chose\n{computer_index}")

if player_index == computer_index:
    print("It's a draw.")
elif player_choice == 0 and computer_choice == 1:
    print("You lost.")
elif player_choice == 0 and computer_choice == 2:
    print("You won.")
elif player_choice == 1 and computer_choice == 0:
    print("You won.")
elif player_choice == 1 and computer_choice == 2:
    print("You lost.")
elif player_choice == 2 and computer_choice == 0:
    print("You lost.")
elif player_choice == 2 and computer_choice == 1:
    print("You won.")
