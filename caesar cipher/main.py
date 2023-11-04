from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = True

def caesar(user_text, user_shift, user_direction):
    new_text = ""
    if user_direction == 'decode':
            user_shift *= -1
    for symbol in user_text:
        if symbol in alphabet:
            position = alphabet.index(symbol)
            new_position = position + user_shift
            new_text += alphabet[new_position]
        else:
             new_text += symbol
    print(f"The {user_direction}d text is {new_text}.")

while restart == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    new_shift = shift % len(alphabet)
    caesar(user_text=text, user_shift=new_shift, user_direction=direction)
    want_to_restart = input("Do you want to restart? If yes, type 'yes', otherwise type 'no'.\n")

    if want_to_restart == 'yes':
        restart = True
    elif want_to_restart == 'no':
        print("Goodbye.")
        restart = False
    else:
        print(f"There is no {want_to_restart} option, goodbye.\n")
        restart = False