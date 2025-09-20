import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess a number between 1 and 100: ")
    if not player_input.isdigit():
        print("Sorry, invalid number. Please try again.")
        continue
    player_number = int(player_input)

    if player_number == computer_number:
        print("Good job! You guessed my number is ", computer_number)
        break
    elif player_number > computer_number:
        print("Your number is too high.")
    elif player_number < computer_number:
        print(f"Your number is too low.")
