import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []

def win_or_lose(userscore, compscore):
    if userscore > 21:
        print("You lose.")
    elif compscore > 21:
        print("You win.")
    elif userscore == 21 and compscore != 21:
        print("Win, you have BlackJack")
    elif compscore == 21 and userscore != 21:
        print("Lose, opponent has Blackjack.")
    elif userscore > compscore:
        print("You win.")
    elif userscore == compscore:
        print("It's a draw.")
    else:
        print("You lose")

def check_ace():
    for card in your_cards:
        if card == 11 and sum(your_cards) > 21:
            card = 1

def main():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == 'n':
        exit()
    check = True
    your_cards.clear()
    computer_cards.clear()

    # Here we add 2cards to each list, and print the result
    user_score = 0
    comp_score = 0
    for i in range(1, 3):
        user_card = random.choice(cards)
        your_cards.append(user_card)
        user_score = sum(your_cards)
        comp_card = random.choice(cards)
        computer_cards.append(comp_card)
        comp_score = sum(computer_cards)
    print(f"Your cards: {your_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")

    while check:
        get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        f_user_score = sum(your_cards)
        f_comp_score = sum(computer_cards)
        check_ace()

        if get_or_pass == "n":
            check = False
            print(f"Your final hand: {your_cards}, final score: {f_user_score}\nComputer's final hand: {computer_cards}, final score: {f_comp_score}")
            win_or_lose(f_user_score, f_comp_score)
            main()
        elif get_or_pass == "y":
            your_cards.append(new_usercard)
            computer_cards.append(new_compcard)
            f_user_score += new_usercard
            f_comp_score += new_compcard
            print(f"Your cards: {your_cards}, current score: {f_user_score}\nComputer's first card: {computer_cards[0]}")
            if f_user_score > 21 and f_user_score == f_comp_score:
                print(f"Your final hand: {your_cards}, final score: {f_user_score}\nComputer's final hand: {computer_cards}, final score: {f_comp_score}\nIt's a draw.")
                main()
            elif f_user_score > 21:
                print(f"Your final hand: {your_cards}, final score: {f_user_score}\nComputer's final hand: {computer_cards}, final score: {f_comp_score}\nYou went over. You lose 😤")
                check = False
                main()
        else:
            print("You didn't choose a valid option.")


new_usercard = random.choice(cards)
new_compcard = random.choice(cards)
f_user_score = sum(your_cards)
f_comp_score = sum(computer_cards)
main()
